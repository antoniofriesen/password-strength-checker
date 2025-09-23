"""
Unit Tests for Password Checker Module

These tests ensure our password analysis logic works correctly.
Each tests focuses on one specific aspect of the functionality.

Run with: python3 -m pytest tests/test_password_checker.py -v
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from password_checker import PasswordChecker


class TestPasswordChecker(unittest.TestCase):
    """
    Test suite for PasswordChecker class.

    Each tests method checks one specific functionality.
    Tests should be independent and can run in any order.
    """

    def setUp(self):
        """
        Set up tests fixtures before each tests method.

        This runs before EVERY tests method, giving each tests
        a fresh PasswordChecker instance to work with.
        """
        self.checker = PasswordChecker()

    def tearDown(self):
        """
        Clean up after each tests method.

        This runs after every tests. Not needed here, but
        good practice to include for future use.
        """
        pass

    # ========== LENGTH ANALYSIS TESTS ==========

    def test_analyze_length_excellent(self):
        """Test length analysis for passwords >= 12 characters."""
        points, message = self.checker.analyze_length("verylongpassword123")

        self.assertEqual(points, 3)
        self.assertIn("Excellent length", message)
        self.assertIn("✅", message)

    def test_analyze_length_good(self):
        """Test length analysis for passwords 8-11 characters."""
        points, message = self.checker.analyze_length("goodpass")

        self.assertEqual(points, 2)
        self.assertIn("Good length", message)
        self.assertIn("✅", message)

    def test_analyze_length_acceptable(self):
        """Test length analysis for passwords 6-7 characters."""
        points, message = self.checker.analyze_length("okay12")

        self.assertEqual(points, 1)
        self.assertIn("Acceptable", message)
        self.assertIn("⚠️", message)

    def test_analyze_length_too_short(self):
        """Test length analysis for passwords < 6 characters."""
        points, message = self.checker.analyze_length("bad")

        self.assertEqual(points, 0)
        self.assertIn("Too short", message)
        self.assertIn("❌", message)

    def test_analyze_length_edge_cases(self):
        """Test edge cases for length analysis."""
        # Empty password
        points, _ = self.checker.analyze_length("")
        self.assertEqual(points, 0)

        # Exactly at boundaries
        points, _ = self.checker.analyze_length("123456")  # exactly 6
        self.assertEqual(points, 1)

        points, _ = self.checker.analyze_length("12345678")  # exactly 8
        self.assertEqual(points, 2)

        points, _ = self.checker.analyze_length("123456789012")  # exactly 12
        self.assertEqual(points, 3)

    # ========== CHARACTER TYPE TESTS ==========

    def test_analyze_lowercase_present(self):
        """Test lowercase detection when present."""
        points, message = self.checker.analyze_lowercase("Password123")

        self.assertEqual(points, 1)
        self.assertIn("Contains lowercase", message)
        self.assertIn("✅", message)

    def test_analyze_lowercase_absent(self):
        """Test lowercase detection when absent."""
        points, message = self.checker.analyze_lowercase("PASSWORD123")

        self.assertEqual(points, 0)
        self.assertIn("Add lowercase", message)
        self.assertIn("❌", message)

    def test_analyze_uppercase_present(self):
        """Test uppercase detection when present."""
        points, message = self.checker.analyze_uppercase("Password123")

        self.assertEqual(points, 1)
        self.assertIn("Contains uppercase", message)
        self.assertIn("✅", message)

    def test_analyze_uppercase_absent(self):
        """Test uppercase detection when absent."""
        points, message = self.checker.analyze_uppercase("password123")

        self.assertEqual(points, 0)
        self.assertIn("Add uppercase", message)
        self.assertIn("❌", message)

    def test_analyze_digits_present(self):
        """Test digit detection when present."""
        points, message = self.checker.analyze_digits("Password123")

        self.assertEqual(points, 1)
        self.assertIn("Contains numbers", message)
        self.assertIn("✅", message)

    def test_analyze_digits_absent(self):
        """Test digit detection when absent."""
        points, message = self.checker.analyze_digits("Password")

        self.assertEqual(points, 0)
        self.assertIn("Add numbers", message)
        self.assertIn("❌", message)

    def test_analyze_special_characters_present(self):
        """Test special character detection when present."""
        points, message = self.checker.analyze_special_characters("Password123!")

        self.assertEqual(points, 2)  # Special chars worth 2 points
        self.assertIn("Contains special", message)
        self.assertIn("✅", message)

    def test_analyze_special_characters_absent(self):
        """Test special character detection when absent."""
        points, message = self.checker.analyze_special_characters("Password123")

        self.assertEqual(points, 0)
        self.assertIn("Add special", message)
        self.assertIn("❌", message)

    def test_special_characters_variety(self):
        """Test various special characters are recognized."""
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

        for char in special_chars:
            password = f"Pass123{char}"
            points, _ = self.checker.analyze_special_characters(password)
            self.assertEqual(points, 2, f"Character '{char}' not recognized as special")

    # ========== STRENGTH CALCULATION TESTS ==========

    def test_calculate_strength_level_strong(self):
        """Test strength calculation for strong passwords."""
        self.assertEqual(self.checker.calculate_strength_level(8), "STRONG")
        self.assertEqual(self.checker.calculate_strength_level(7), "STRONG")

    def test_calculate_strength_level_medium(self):
        """Test strength calculation for medium passwords."""
        self.assertEqual(self.checker.calculate_strength_level(6), "MEDIUM")
        self.assertEqual(self.checker.calculate_strength_level(5), "MEDIUM")
        self.assertEqual(self.checker.calculate_strength_level(4), "MEDIUM")

    def test_calculate_strength_level_weak(self):
        """Test strength calculation for weak passwords."""
        self.assertEqual(self.checker.calculate_strength_level(3), "WEAK")
        self.assertEqual(self.checker.calculate_strength_level(2), "WEAK")
        self.assertEqual(self.checker.calculate_strength_level(1), "WEAK")
        self.assertEqual(self.checker.calculate_strength_level(0), "WEAK")

    # ========== INTEGRATION TESTS ==========

    def test_check_password_strength_weak_password(self):
        """Test complete analysis of a weak password."""
        strength, score, feedback = self.checker.check_password_strength("123")

        self.assertEqual(strength, "WEAK")
        self.assertLess(score, 4)
        self.assertIsInstance(feedback, list)
        self.assertEqual(len(feedback), 5)  # Should have 5 feedback items

    def test_check_password_strength_medium_password(self):
        """Test complete analysis of a medium strength password."""
        strength, score, feedback = self.checker.check_password_strength("Password123")

        self.assertEqual(strength, "MEDIUM")
        self.assertGreaterEqual(score, 4)
        self.assertLess(score, 7)
        self.assertIsInstance(feedback, list)

    def test_check_password_strength_strong_password(self):
        """Test complete analysis of a strong password."""
        strength, score, feedback = self.checker.check_password_strength("MyStrongP@ssw0rd123!")

        self.assertEqual(strength, "STRONG")
        self.assertGreaterEqual(score, 7)
        self.assertIsInstance(feedback, list)

    def test_check_password_strength_empty_password(self):
        """Test analysis of empty password."""
        strength, score, feedback = self.checker.check_password_strength("")

        self.assertEqual(strength, "WEAK")
        self.assertEqual(score, 0)
        self.assertIsInstance(feedback, list)

    def test_check_password_strength_unicode_password(self):
        """Test analysis of password with unicode characters."""
        # Test with unicode characters
        strength, score, feedback = self.checker.check_password_strength("Pässwörd123!")

        # Should still work with unicode
        self.assertIn(strength, ["WEAK", "MEDIUM", "STRONG"])
        self.assertIsInstance(score, int)
        self.assertIsInstance(feedback, list)

    # ========== CONFIGURATION TESTS ==========

    def test_checker_initialization(self):
        """Test that PasswordChecker initializes with correct defaults."""
        checker = PasswordChecker()

        # Test default configuration
        self.assertEqual(checker.min_length_weak, 6)
        self.assertEqual(checker.min_length_medium, 8)
        self.assertEqual(checker.min_length_strong, 12)
        self.assertIsInstance(checker.special_chars, str)
        self.assertGreater(len(checker.special_chars), 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)