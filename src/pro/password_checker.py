"""
Pro Password Checker Module
Production-ready password analysis with enterprise features

This module includes all Advanced features plus:
- Password generation
- Batch processing
- Export capabilities
- Performance optimizations
- Enhanced reporting
"""

import math
import re
import secrets
import string
import json
from collections import Counter
from datetime import datetime
from typing import Dict, List, Tuple, Optional


class ProPasswordChecker:
    """
    Professional-grade password strength analysis.

    Extends Advanced features with production capabilities:
    - Batch processing
    - Detailed reporting
    - Export functionality
    - Performance optimized
    """

    def __init__(self, custom_common_passwords: Optional[set] = None):
        """
        Initialize the pro password checker.

        Args:
            custom_common_passwords: Optional custom password database
        """
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.min_length_weak = 6
        self.min_length_medium = 8
        self.min_length_strong = 12

        # Common passwords database (can be extended)
        self.common_passwords = custom_common_passwords or {
            "password", "123456", "12345678", "qwerty", "abc123", "monkey",
            "1234567890", "letmein", "trustno1", "dragon", "baseball", "111111",
            "iloveyou", "master", "sunshine", "ashley", "bailey", "passw0rd",
            "shadow", "123123", "654321", "superman", "qazwsx", "michael",
            "football", "password1", "admin", "welcome", "login", "test",
            "charlie", "jordan", "freedom", "family", "robert", "thomas",
            "hockey", "ranger", "daniel", "pantera", "tigger", "doctor",
            "gateway", "guestgue", "internet", "service", "eternal",
            "smiles", "local", "biteme", "2000", "chelsea", "access",
            "yankees", "987654321", "dallas", "austin", "thunder", "taylor"
        }

        # Keyboard patterns
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

        # Statistics for batch processing
        self.analysis_count = 0
        self.batch_statistics = {
            'total_analyzed': 0,
            'strength_distribution': {
                'VERY WEAK': 0,
                'WEAK': 0,
                'MEDIUM': 0,
                'STRONG': 0,
                'EXCELLENT': 0
            },
            'average_score': 0.0,
            'average_entropy': 0.0,
            'common_password_count': 0,
            'pattern_detected_count': 0
        }

    def calculate_entropy(self, password: str) -> Tuple[float, int, str]:
        """Calculate password entropy (bits of randomness)."""
        if not password:
            return 0.0, 0, "❌ Empty password has no entropy"

        char_set_size = 0
        char_types = []

        if any(c.islower() for c in password):
            char_set_size += 26
            char_types.append("lowercase")

        if any(c.isupper() for c in password):
            char_set_size += 26
            char_types.append("uppercase")

        if any(c.isdigit() for c in password):
            char_set_size += 10
            char_types.append("digits")

        if any(c in self.special_chars for c in password):
            char_set_size += len(self.special_chars)
            char_types.append("special characters")

        entropy = len(password) * math.log2(char_set_size) if char_set_size > 0 else 0.0

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

    def check_common_passwords(self, password: str) -> Tuple[bool, str]:
        """Check if password is in common/weak passwords database."""
        password_lower = password.lower()

        if password_lower in self.common_passwords:
            return True, "❌ This is a common password - easily cracked!"

        base_password = re.sub(r'[0-9!@#$%^&*()_+-=\[\]{}|;:,.<>?]*$', '', password_lower)
        if base_password in self.common_passwords:
            return True, f"❌ Based on common password '{base_password}' - still weak!"

        for common in self.common_passwords:
            if len(common) >= 4 and password_lower.startswith(common):
                return True, f"❌ Starts with common password '{common}' - predictable!"

        return False, "✅ Not found in common passwords database"

    def detect_patterns(self, password: str) -> Tuple[List[str], int, List[str]]:
        """Detect keyboard patterns and sequences in password."""
        password_lower = password.lower()
        patterns_found = []
        feedback = []
        penalty = 0

        for pattern in self.keyboard_patterns:
            if pattern in password_lower:
                patterns_found.append(f"keyboard: {pattern}")
                penalty += 2
                feedback.append(f"❌ Contains keyboard pattern: '{pattern}'")

        for pattern in self.sequential_patterns:
            if pattern in password_lower:
                patterns_found.append(f"sequence: {pattern}")
                penalty += 2
                feedback.append(f"❌ Contains sequential pattern: '{pattern}'")

        repeated_pattern = re.search(r'(.)\1{2,}', password)
        if repeated_pattern:
            repeated_char = repeated_pattern.group(1)
            repeated_count = len(repeated_pattern.group(0))
            patterns_found.append(f"repetition: {repeated_char}x{repeated_count}")
            penalty += min(repeated_count, 4)
            feedback.append(f"❌ Contains repeated character: '{repeated_char}' x{repeated_count}")

        number_suffix = re.search(r'\d{3,}$', password)
        if number_suffix:
            numbers = number_suffix.group(0)
            if self._is_simple_sequence(numbers):
                patterns_found.append(f"number suffix: {numbers}")
                penalty += 1
                feedback.append(f"⚠️  Simple number sequence at end: '{numbers}'")

        if not patterns_found:
            feedback.append("✅ No obvious patterns detected")

        return patterns_found, penalty, feedback

    def _is_simple_sequence(self, numbers: str) -> bool:
        """Check if numbers form a simple sequence."""
        if len(numbers) < 3:
            return False

        ascending = all(int(numbers[i]) == int(numbers[i - 1]) + 1
                        for i in range(1, len(numbers)))
        descending = all(int(numbers[i]) == int(numbers[i - 1]) - 1
                         for i in range(1, len(numbers)))

        return ascending or descending

    def calculate_advanced_score(self, password: str) -> Tuple[float, int, Dict[str, str]]:
        """Advanced scoring algorithm incorporating all security factors."""
        score_breakdown = {}
        total_score = 0.0
        max_possible = 100

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

        total_score += length_score
        score_breakdown['length'] = f"{length_score}/15"

        diversity_score = 0
        if any(c.islower() for c in password):
            diversity_score += 5
        if any(c.isupper() for c in password):
            diversity_score += 5
        if any(c.isdigit() for c in password):
            diversity_score += 5
        if any(c in self.special_chars for c in password):
            diversity_score += 10

        total_score += diversity_score
        score_breakdown['character_types'] = f"{diversity_score}/25"

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

        is_common, _ = self.check_common_passwords(password)
        common_penalty = -20 if is_common else 0
        total_score += common_penalty
        score_breakdown['common_password'] = f"{common_penalty}/0" + (" (PENALTY)" if common_penalty < 0 else "")

        patterns, pattern_penalty, _ = self.detect_patterns(password)
        pattern_penalty = -min(pattern_penalty, 10)
        total_score += pattern_penalty
        score_breakdown['patterns'] = f"{pattern_penalty}/0" + (" (PENALTY)" if pattern_penalty < 0 else "")

        uniqueness_score = min(len(set(password)) / len(password) * 10, 10) if password else 0
        total_score += uniqueness_score
        score_breakdown['uniqueness'] = f"{uniqueness_score:.1f}/10"

        total_score = max(0, min(total_score, max_possible))

        return total_score, max_possible, score_breakdown

    def get_strength_level(self, score: float) -> str:
        """Convert score to strength level."""
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

    def analyze_password(self, password: str, update_stats: bool = True) -> Dict:
        """
        Complete professional password analysis.

        Args:
            password: Password to analyze
            update_stats: Whether to update batch statistics

        Returns:
            dict: Comprehensive analysis results
        """
        # Calculate all metrics
        entropy, char_set_size, entropy_feedback = self.calculate_entropy(password)
        is_common, common_feedback = self.check_common_passwords(password)
        patterns, pattern_penalty, pattern_feedback = self.detect_patterns(password)
        total_score, max_score, score_breakdown = self.calculate_advanced_score(password)
        strength_level = self.get_strength_level(total_score)

        # Compile feedback
        all_feedback = [entropy_feedback, common_feedback] + pattern_feedback

        # Generate recommendations
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

        result = {
            'password_length': len(password),
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
            'timestamp': datetime.now().isoformat()
        }

        # Update statistics if requested
        if update_stats:
            self._update_statistics(result)

        return result

    def _update_statistics(self, result: Dict):
        """Update batch processing statistics."""
        self.batch_statistics['total_analyzed'] += 1
        self.batch_statistics['strength_distribution'][result['strength_level']] += 1

        # Update running averages
        n = self.batch_statistics['total_analyzed']
        old_avg_score = self.batch_statistics['average_score']
        old_avg_entropy = self.batch_statistics['average_entropy']

        self.batch_statistics['average_score'] = (old_avg_score * (n - 1) + result['total_score']) / n
        self.batch_statistics['average_entropy'] = (old_avg_entropy * (n - 1) + result['entropy']) / n

        if result['is_common']:
            self.batch_statistics['common_password_count'] += 1

        if result['patterns_found']:
            self.batch_statistics['pattern_detected_count'] += 1

    def analyze_batch(self, passwords: List[str]) -> List[Dict]:
        """
        Analyze multiple passwords at once.

        Args:
            passwords: List of passwords to analyze

        Returns:
            List of analysis results
        """
        results = []
        for password in passwords:
            result = self.analyze_password(password, update_stats=True)
            results.append(result)

        return results

    def get_batch_statistics(self) -> Dict:
        """Get statistics from batch processing."""
        return self.batch_statistics.copy()

    def reset_statistics(self):
        """Reset batch statistics."""
        self.batch_statistics = {
            'total_analyzed': 0,
            'strength_distribution': {
                'VERY WEAK': 0,
                'WEAK': 0,
                'MEDIUM': 0,
                'STRONG': 0,
                'EXCELLENT': 0
            },
            'average_score': 0.0,
            'average_entropy': 0.0,
            'common_password_count': 0,
            'pattern_detected_count': 0
        }

    def export_to_json(self, results: List[Dict], filepath: str):
        """
        Export analysis results to JSON file.

        Args:
            results: List of analysis results
            filepath: Output file path
        """
        export_data = {
            'metadata': {
                'version': '4.0.0',
                'export_time': datetime.now().isoformat(),
                'total_passwords': len(results)
            },
            'statistics': self.get_batch_statistics(),
            'results': results
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)

    def export_to_csv(self, results: List[Dict], filepath: str):
        """
        Export analysis results to CSV file.

        Args:
            results: List of analysis results
            filepath: Output file path
        """
        import csv

        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            if not results:
                return

            fieldnames = ['password_length', 'strength_level', 'total_score',
                          'percentage', 'entropy', 'is_common', 'patterns_found',
                          'timestamp']

            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()

            for result in results:
                # Flatten patterns list for CSV
                result_copy = result.copy()
                result_copy['patterns_found'] = ', '.join(result['patterns_found']) if result[
                    'patterns_found'] else 'None'
                writer.writerow(result_copy)


class PasswordGenerator:
    """
    Secure password generator using cryptographically secure random.

    Generates strong passwords based on configurable criteria.
    """

    def __init__(self):
        """Initialize the password generator."""
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def generate(self,
                 length: int = 16,
                 use_lowercase: bool = True,
                 use_uppercase: bool = True,
                 use_digits: bool = True,
                 use_special: bool = True,
                 exclude_ambiguous: bool = False) -> str:
        """
        Generate a secure random password.

        Args:
            length: Password length
            use_lowercase: Include lowercase letters
            use_uppercase: Include uppercase letters
            use_digits: Include digits
            use_special: Include special characters
            exclude_ambiguous: Exclude ambiguous characters (0, O, l, 1, etc.)

        Returns:
            str: Generated password
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")

        # Build character pool
        char_pool = ""
        required_chars = []

        lowercase = self.lowercase
        uppercase = self.uppercase
        digits = self.digits
        special = self.special

        if exclude_ambiguous:
            lowercase = lowercase.replace('l', '').replace('o', '')
            uppercase = uppercase.replace('I', '').replace('O', '')
            digits = digits.replace('0', '').replace('1', '')
            special = special.replace('|', '')

        if use_lowercase:
            char_pool += lowercase
            required_chars.append(secrets.choice(lowercase))

        if use_uppercase:
            char_pool += uppercase
            required_chars.append(secrets.choice(uppercase))

        if use_digits:
            char_pool += digits
            required_chars.append(secrets.choice(digits))

        if use_special:
            char_pool += special
            required_chars.append(secrets.choice(special))

        if not char_pool:
            raise ValueError("At least one character type must be selected")

        # Generate remaining characters
        remaining_length = length - len(required_chars)
        remaining_chars = [secrets.choice(char_pool) for _ in range(remaining_length)]

        # Combine and shuffle
        password_chars = required_chars + remaining_chars
        password_list = list(password_chars)

        # Secure shuffle
        for i in range(len(password_list) - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            password_list[i], password_list[j] = password_list[j], password_list[i]

        return ''.join(password_list)

    def generate_multiple(self, count: int, **kwargs) -> List[str]:
        """
        Generate multiple passwords.

        Args:
            count: Number of passwords to generate
            **kwargs: Arguments passed to generate()

        Returns:
            List of generated passwords
        """
        return [self.generate(**kwargs) for _ in range(count)]

    def generate_passphrase(self, word_count: int = 4, separator: str = '-') -> str:
        """
        Generate a passphrase using random words.

        Args:
            word_count: Number of words in passphrase
            separator: Separator between words

        Returns:
            str: Generated passphrase
        """
        # Simple word list (in production, use a proper dictionary)
        word_list = [
            "correct", "horse", "battery", "staple", "dragon", "wizard",
            "castle", "forest", "mountain", "ocean", "thunder", "lightning",
            "phoenix", "griffin", "crystal", "shadow", "mystic", "cosmic",
            "nebula", "quantum", "stellar", "lunar", "solar", "eclipse"
        ]

        words = [secrets.choice(word_list) for _ in range(word_count)]
        return separator.join(words)