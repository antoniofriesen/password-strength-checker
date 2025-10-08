"""
Advanced Password Checker Module
Enhanced password analysis with cybersecurity-focused features

This module includes:
- Entropy calculation (mathematical randomness measurement)
- Common password detection
- Pattern recognition (keyboard patterns, sequences)
- Advanced scoring algorithms
"""

import math
import re
from collections import Counter


class AdvancedPasswordChecker:
    """
    Advanced password strength analysis with cybersecurity concepts.

    This class implements professional-grade password analysis including
    entropy calculations, pattern detection, and common password checking.
    """

    def __init__(self):
        """Initialize the advanced password checker with security datasets."""
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.min_length_weak = 6
        self.min_length_medium = 8
        self.min_length_strong = 12

        # Common passwords database (top weak passwords)
        self.common_passwords = {
            "password", "123456", "12345678", "qwerty", "abc123", "monkey",
            "1234567890", "letmein", "trustno1", "dragon", "baseball", "111111",
            "iloveyou", "master", "sunshine", "ashley", "bailey", "passw0rd",
            "shadow", "123123", "654321", "superman", "qazwsx", "michael",
            "football", "password1", "admin", "welcome", "login", "test",
            "charlie", "jordan", "freedom", "family", "robert", "thomas",
            "hockey", "ranger", "daniel", "pantera", "tigger", "doctor",
            "gateway", "guestgue", "internet", "service", "eternal", "eternal",
            "smiles", "local", "biteme", "2000", "chelsea", "access",
            "yankees", "987654321", "dallas", "austin", "thunder", "taylor"
        }

        # Keyboard patterns for pattern detection
        self.keyboard_patterns = [
            "qwerty", "qwertyuiop", "asdfgh", "asdfghjkl", "zxcvbn", "zxcvbnm",
            "1234567890", "0987654321", "abcdefgh", "zyxwvuts"
        ]

        # Sequential patterns
        self.sequential_patterns = [
            "abcd", "bcde", "cdef", "defg", "efgh", "fghi", "ghij", "hijk",
            "ijkl", "jklm", "klmn", "lmno", "mnop", "nopq", "opqr", "pqrs",
            "qrst", "rstu", "stuv", "tuvw", "uvwx", "vwxy", "wxyz",
            "1234", "2345", "3456", "4567", "5678", "6789", "7890"
        ]

    def calculate_entropy(self, password):
        """
        Calculate password entropy (bits of randomness).

        Entropy measures how unpredictable a password is.
        Higher entropy = harder to crack.

        Args:
            password (str): Password to analyze

        Returns:
            tuple: (entropy_bits, character_set_size, feedback_message)
        """
        if not password:
            return 0, 0, "❌ Empty password has no entropy"

        # Determine character set size
        char_set_size = 0
        char_types = []

        if any(c.islower() for c in password):
            char_set_size += 26  # a-z
            char_types.append("lowercase")

        if any(c.isupper() for c in password):
            char_set_size += 26  # A-Z
            char_types.append("uppercase")

        if any(c.isdigit() for c in password):
            char_set_size += 10  # 0-9
            char_types.append("digits")

        if any(c in self.special_chars for c in password):
            char_set_size += len(self.special_chars)
            char_types.append("special characters")

        # Calculate theoretical maximum entropy
        # Entropy = log2(character_set_size ^ password_length)
        # Simplified: Entropy = password_length * log2(character_set_size)
        if char_set_size > 0:
            entropy = len(password) * math.log2(char_set_size)
        else:
            entropy = 0

        # Create feedback message
        char_types_str = ", ".join(char_types)
        if entropy >= 60:
            feedback = f"🔒 Excellent entropy: {entropy:.1f} bits ({char_types_str})"
        elif entropy >= 40:
            feedback = f"🔐 Good entropy: {entropy:.1f} bits ({char_types_str})"
        elif entropy >= 25:
            feedback = f"⚠️  Fair entropy: {entropy:.1f} bits ({char_types_str})"
        else:
            feedback = f"❌ Low entropy: {entropy:.1f} bits ({char_types_str})"

        return entropy, char_set_size, feedback

    def check_common_passwords(self, password):
        """
        Check if password is in common/weak passwords database.

        Args:
            password (str): Password to check

        Returns:
            tuple: (is_common, feedback_message)
        """
        password_lower = password.lower()

        # Direct match
        if password_lower in self.common_passwords:
            return True, "❌ This is a common password - easily cracked!"

        # Check variations (password123, password!, etc.)
        base_password = re.sub(r'[0-9!@#$%^&*()_+-=\[\]{}|;:,.<>?]*$', '', password_lower)
        if base_password in self.common_passwords:
            return True, f"❌ Based on common password '{base_password}' - still weak!"

        # Check if it starts with common password
        for common in self.common_passwords:
            if len(common) >= 4 and password_lower.startswith(common):
                return True, f"❌ Starts with common password '{common}' - predictable!"

        return False, "✅ Not found in common passwords database"

    def detect_patterns(self, password):
        """
        Detect keyboard patterns and sequences in password.

        Args:
            password (str): Password to analyze

        Returns:
            tuple: (patterns_found, pattern_score_penalty, feedback_list)
        """
        password_lower = password.lower()
        patterns_found = []
        feedback = []
        penalty = 0

        # Check keyboard patterns
        for pattern in self.keyboard_patterns:
            if pattern in password_lower:
                patterns_found.append(f"keyboard: {pattern}")
                penalty += 2
                feedback.append(f"❌ Contains keyboard pattern: '{pattern}'")

        # Check sequential patterns
        for pattern in self.sequential_patterns:
            if pattern in password_lower:
                patterns_found.append(f"sequence: {pattern}")
                penalty += 2
                feedback.append(f"❌ Contains sequential pattern: '{pattern}'")

        # Check repeated characters (aaa, 111, etc.)
        repeated_pattern = re.search(r'(.)\1{2,}', password)
        if repeated_pattern:
            repeated_char = repeated_pattern.group(1)
            repeated_count = len(repeated_pattern.group(0))
            patterns_found.append(f"repetition: {repeated_char}x{repeated_count}")
            penalty += min(repeated_count, 4)  # Cap penalty at 4
            feedback.append(f"❌ Contains repeated character: '{repeated_char}' x{repeated_count}")

        # Check simple number sequences at end (password123)
        number_suffix = re.search(r'\d{3,}$', password)
        if number_suffix:
            numbers = number_suffix.group(0)
            if self._is_simple_sequence(numbers):
                patterns_found.append(f"number suffix: {numbers}")
                penalty += 1
                feedback.append(f"⚠️  Simple number sequence at end: '{numbers}'")

        # Positive feedback if no patterns
        if not patterns_found:
            feedback.append("✅ No obvious patterns detected")

        return patterns_found, penalty, feedback

    def _is_simple_sequence(self, numbers):
        """Check if numbers form a simple sequence (123, 456, 321, etc.)"""
        if len(numbers) < 3:
            return False

        # Check ascending sequence
        ascending = all(int(numbers[i]) == int(numbers[i - 1]) + 1
                        for i in range(1, len(numbers)))

        # Check descending sequence
        descending = all(int(numbers[i]) == int(numbers[i - 1]) - 1
                         for i in range(1, len(numbers)))

        return ascending or descending

    def calculate_advanced_score(self, password):
        """
        Advanced scoring algorithm incorporating all security factors.

        Args:
            password (str): Password to score

        Returns:
            tuple: (total_score, max_possible_score, score_breakdown)
        """
        score_breakdown = {}
        total_score = 0
        max_possible = 100  # New 100-point scale

        # 1. Basic criteria (40 points possible)
        basic_score = 0

        # Length scoring (0-15 points)
        length = len(password)
        if length >= 16:
            length_score = 15
        elif length >= 12:
            length_score = 12
        elif length >= 8:
            length_score = 8
        elif length >= 6:
            length_score = 4
        else:
            length_score = 0

        basic_score += length_score
        score_breakdown['length'] = f"{length_score}/15"

        # Character diversity (0-25 points)
        diversity_score = 0
        if any(c.islower() for c in password):
            diversity_score += 5
        if any(c.isupper() for c in password):
            diversity_score += 5
        if any(c.isdigit() for c in password):
            diversity_score += 5
        if any(c in self.special_chars for c in password):
            diversity_score += 10  # Worth more

        basic_score += diversity_score
        score_breakdown['character_types'] = f"{diversity_score}/25"

        total_score += basic_score

        # 2. Entropy scoring (0-30 points)
        entropy, _, _ = self.calculate_entropy(password)
        if entropy >= 70:
            entropy_score = 30
        elif entropy >= 50:
            entropy_score = 25
        elif entropy >= 35:
            entropy_score = 20
        elif entropy >= 25:
            entropy_score = 15
        elif entropy >= 15:
            entropy_score = 10
        else:
            entropy_score = 5

        total_score += entropy_score
        score_breakdown['entropy'] = f"{entropy_score}/30 ({entropy:.1f} bits)"

        # 3. Common password check (0/-20 points)
        is_common, _ = self.check_common_passwords(password)
        common_penalty = -20 if is_common else 0
        total_score += common_penalty
        score_breakdown['common_password'] = f"{common_penalty}/0" + (" (PENALTY)" if common_penalty < 0 else "")

        # 4. Pattern detection (0/-10 points)
        patterns, pattern_penalty, _ = self.detect_patterns(password)
        pattern_penalty = -min(pattern_penalty, 10)  # Cap penalty
        total_score += pattern_penalty
        score_breakdown['patterns'] = f"{pattern_penalty}/0" + (" (PENALTY)" if pattern_penalty < 0 else "")

        # 5. Uniqueness bonus (0-10 points)
        uniqueness_score = min(len(set(password)) / len(password) * 10, 10) if password else 0
        total_score += uniqueness_score
        score_breakdown['uniqueness'] = f"{uniqueness_score:.1f}/10"

        # Ensure score stays within bounds
        total_score = max(0, min(total_score, max_possible))

        return total_score, max_possible, score_breakdown

    def get_strength_level_advanced(self, score):
        """Convert advanced score to strength level."""
        if score >= 80:
            return "EXCELLENT"
        elif score >= 65:
            return "STRONG"
        elif score >= 45:
            return "MEDIUM"
        elif score >= 25:
            return "WEAK"
        else:
            return "VERY WEAK"

    def check_password_strength_advanced(self, password):
        """
        Complete advanced password analysis.

        Args:
            password (str): Password to analyze

        Returns:
            dict: Comprehensive analysis results
        """
        # Calculate all metrics
        entropy, char_set_size, entropy_feedback = self.calculate_entropy(password)
        is_common, common_feedback = self.check_common_passwords(password)
        patterns, pattern_penalty, pattern_feedback = self.detect_patterns(password)
        total_score, max_score, score_breakdown = self.calculate_advanced_score(password)
        strength_level = self.get_strength_level_advanced(total_score)

        # Compile comprehensive feedback
        all_feedback = []
        all_feedback.append(entropy_feedback)
        all_feedback.append(common_feedback)
        all_feedback.extend(pattern_feedback)

        # Security recommendations
        recommendations = []
        if len(password) < 12:
            recommendations.append("🔹 Use at least 12 characters")
        if not any(c.isupper() for c in password):
            recommendations.append("🔹 Add uppercase letters")
        if not any(c.islower() for c in password):
            recommendations.append("🔹 Add lowercase letters")
        if not any(c.isdigit() for c in password):
            recommendations.append("🔹 Add numbers")
        if not any(c in self.special_chars for c in password):
            recommendations.append("🔹 Add special characters")
        if entropy < 40:
            recommendations.append("🔹 Increase randomness - avoid predictable patterns")
        if is_common:
            recommendations.append("🔹 Avoid common passwords and variations")

        return {
            'strength_level': strength_level,
            'total_score': total_score,
            'max_score': max_score,
            'percentage': (total_score / max_score) * 100,
            'entropy': entropy,
            'char_set_size': char_set_size,
            'is_common': is_common,
            'patterns_found': patterns,
            'pattern_penalty': pattern_penalty,
            'score_breakdown': score_breakdown,
            'feedback': all_feedback,
            'recommendations': recommendations,
            'length': len(password)
        }