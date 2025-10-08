"""
Password Checker Module - Intermediate Version
Core password analysis functionality with OOP design

This module contains the main password analysis logic,
separated from the user interface for better organization.
"""


class PasswordChecker:
    """
    A class to handle password strength analysis.

    Separating logic into a class makes it easier to:
    - Add configuration options
    - Maintain state if needed
    - Unit test individual methods
    - Extend functionality
    """

    def __init__(self):
        """Initialize the password checker with default settings."""
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.min_length_weak = 6
        self.min_length_medium = 8
        self.min_length_strong = 12

    def analyze_length(self, password):
        """
        Analyze password length and assign points.

        Args:
            password (str): Password to analyze

        Returns:
            tuple: (points, feedback_message)
        """
        length = len(password)

        if length >= self.min_length_strong:
            return 3, "✅ Excellent length (12+ characters)"
        elif length >= self.min_length_medium:
            return 2, "✅ Good length (8+ characters)"
        elif length >= self.min_length_weak:
            return 1, "⚠️  Acceptable length, but could be longer"
        else:
            return 0, "❌ Too short! Use at least 6 characters"

    def analyze_lowercase(self, password):
        """Check for lowercase letters."""
        if any(c.islower() for c in password):
            return 1, "✅ Contains lowercase letters"
        else:
            return 0, "❌ Add lowercase letters (a-z)"

    def analyze_uppercase(self, password):
        """Check for uppercase letters."""
        if any(c.isupper() for c in password):
            return 1, "✅ Contains uppercase letters"
        else:
            return 0, "❌ Add uppercase letters (A-Z)"

    def analyze_digits(self, password):
        """Check for numeric digits."""
        if any(c.isdigit() for c in password):
            return 1, "✅ Contains numbers"
        else:
            return 0, "❌ Add numbers (0-9)"

    def analyze_special_characters(self, password):
        """Check for special characters."""
        if any(c in self.special_chars for c in password):
            return 2, "✅ Contains special characters"  # Worth more points!
        else:
            return 0, "❌ Add special characters (!@#$%^&*)"

    def calculate_strength_level(self, score):
        """
        Convert numeric score to strength level.

        Args:
            score (int): Total score from all criteria

        Returns:
            str: Strength level (WEAK, MEDIUM, STRONG)
        """
        if score >= 7:
            return "STRONG"
        elif score >= 4:
            return "MEDIUM"
        else:
            return "WEAK"

    def check_password_strength(self, password):
        """
        Main method to analyze password strength.

        Args:
            password (str): Password to analyze

        Returns:
            tuple: (strength_level, total_score, feedback_list)
        """
        total_score = 0
        feedback = []

        # Analyze each criterion
        criteria_methods = [
            self.analyze_length,
            self.analyze_lowercase,
            self.analyze_uppercase,
            self.analyze_digits,
            self.analyze_special_characters
        ]

        # Run each analysis method
        for method in criteria_methods:
            points, message = method(password)
            total_score += points
            feedback.append(message)

        # Determine overall strength
        strength_level = self.calculate_strength_level(total_score)

        return strength_level, total_score, feedback