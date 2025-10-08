"""
Advanced Password Strength Checker - Main Application
Enhanced UI for advanced password analysis features

This version includes:
- Detailed entropy analysis
- Common password detection
- Pattern recognition
- Advanced scoring system
- Comprehensive security recommendations
"""

from password_checker import AdvancedPasswordChecker


class AdvancedPasswordStrengthApp:
    """
    Advanced application with enhanced security analysis features.
    """

    def __init__(self):
        """Initialize the advanced application."""
        self.checker = AdvancedPasswordChecker()

    def display_header(self):
        """Display the enhanced application header."""
        print("=" * 60)
        print("    ADVANCED PASSWORD STRENGTH ANALYZER")
        print("    🔐 Cybersecurity-Grade Analysis 🔐")
        print("=" * 60)
        print("Commands:")
        print("  • 'exit' - Quit the application")
        print("  • 'help' - Show detailed help")
        print("  • 'demo' - Run demonstration with sample passwords")
        print()

    def display_help(self):
        """Display comprehensive help about advanced analysis."""
        print("\n" + "=" * 60)
        print("ADVANCED PASSWORD ANALYSIS FEATURES")
        print("=" * 60)

        print("🔢 ENTROPY CALCULATION:")
        print("   • Measures password randomness in bits")
        print("   • Formula: length × log2(character_set_size)")
        print("   • 60+ bits = Excellent, 40+ = Good, 25+ = Fair")

        print("\n🚫 COMMON PASSWORD DETECTION:")
        print("   • Checks against database of weak passwords")
        print("   • Detects variations (password123, password!)")
        print("   • Identifies common prefixes")

        print("\n🔍 PATTERN RECOGNITION:")
        print("   • Keyboard patterns (qwerty, asdf)")
        print("   • Sequential patterns (123, abc)")
        print("   • Character repetition (aaa, 111)")
        print("   • Simple number suffixes")

        print("\n📊 ADVANCED SCORING (0-100 points):")
        print("   • Length: 0-15 points")
        print("   • Character diversity: 0-25 points")
        print("   • Entropy: 0-30 points")
        print("   • Common password penalty: -20 points")
        print("   • Pattern penalty: up to -10 points")
        print("   • Uniqueness bonus: 0-10 points")

        print("\n💪 STRENGTH LEVELS:")
        print("   • 80-100: EXCELLENT")
        print("   • 65-79:  STRONG")
        print("   • 45-64:  MEDIUM")
        print("   • 25-44:  WEAK")
        print("   • 0-24:   VERY WEAK")

        print("=" * 60 + "\n")

    def display_demo(self):
        """Run demonstration with sample passwords."""
        print("\n" + "=" * 60)
        print("DEMONSTRATION - SAMPLE PASSWORD ANALYSIS")
        print("=" * 60)

        demo_passwords = [
            ("123456", "Very common weak password"),
            ("password123", "Common password with simple suffix"),
            ("qwerty123", "Keyboard pattern with numbers"),
            ("MyPassword!", "Decent but predictable"),
            ("Tr0ub4dor&3", "Strong with good entropy"),
            ("correct horse battery staple", "Passphrase example"),
            ("X9$mK#nP2@vL8*qR", "Random strong password")
        ]

        for password, description in demo_passwords:
            print(f"\n--- Testing: '{password}' ({description}) ---")
            result = self.checker.check_password_strength_advanced(password)
            self.display_compact_results(result)

        print("=" * 60 + "\n")

    def display_compact_results(self, result):
        """Display compact results for demo mode."""
        strength = result['strength_level']
        score = result['total_score']
        percentage = result['percentage']
        entropy = result['entropy']

        print(f"Strength: {strength} | Score: {score}/100 ({percentage:.1f}%) | Entropy: {entropy:.1f} bits")

        # Show major issues only
        if result['is_common']:
            print("  ❌ Common password detected!")
        if result['patterns_found']:
            print(f"  ⚠️  Patterns: {', '.join(result['patterns_found'][:2])}")

    def display_detailed_results(self, password, result):
        """Display comprehensive analysis results."""
        print(f"\n{'=' * 80}")
        print(f"COMPREHENSIVE PASSWORD ANALYSIS")
        print(f"{'=' * 80}")

        # Basic info
        strength = result['strength_level']
        score = result['total_score']
        max_score = result['max_score']
        percentage = result['percentage']

        print(f"Password length: {result['length']} characters")
        print(f"Strength level: {strength}")
        print(f"Overall score: {score}/{max_score} points ({percentage:.1f}%)")

        # Progress bar visualization
        progress = int(percentage / 5)  # Scale to 20 characters
        bar = "█" * progress + "░" * (20 - progress)
        print(f"Progress: [{bar}] {percentage:.1f}%")

        # Detailed scoring breakdown
        print(f"\n📊 SCORE BREAKDOWN:")
        for category, score_info in result['score_breakdown'].items():
            print(f"   • {category.replace('_', ' ').title()}: {score_info}")

        # Security metrics
        print(f"\n🔐 SECURITY METRICS:")
        print(f"   • Entropy: {result['entropy']:.1f} bits (character set size: {result['char_set_size']})")
        print(f"   • Common password: {'Yes ❌' if result['is_common'] else 'No ✅'}")
        print(f"   • Patterns found: {len(result['patterns_found'])}")
        if result['patterns_found']:
            for pattern in result['patterns_found'][:3]:  # Show first 3
                print(f"     - {pattern}")

        # Detailed feedback
        print(f"\n📝 DETAILED ANALYSIS:")
        for feedback in result['feedback']:
            print(f"   {feedback}")

        # Security recommendations
        if result['recommendations']:
            print(f"\n💡 SECURITY RECOMMENDATIONS:")
            for rec in result['recommendations']:
                print(f"   {rec}")
        else:
            print(f"\n🎉 EXCELLENT! This password meets all security criteria.")

        # Security tip based on strength
        print(f"\n🛡️  SECURITY ASSESSMENT:")
        if strength == "VERY WEAK":
            print("   This password could be cracked in seconds. Immediate change required!")
        elif strength == "WEAK":
            print("   This password is vulnerable to attacks. Please strengthen it.")
        elif strength == "MEDIUM":
            print("   This password is acceptable but could be stronger for sensitive accounts.")
        elif strength == "STRONG":
            print("   This is a strong password suitable for most accounts.")
        else:  # EXCELLENT
            print("   Outstanding! This password provides excellent security.")

        # Estimated crack time (simplified)
        self.display_crack_time_estimate(result['entropy'])

        print("=" * 80)

    def display_crack_time_estimate(self, entropy):
        """Display simplified crack time estimate based on entropy."""
        print(f"\n⏱️  ESTIMATED CRACK TIME (brute force):")

        if entropy < 20:
            print("   • Seconds to minutes")
        elif entropy < 30:
            print("   • Minutes to hours")
        elif entropy < 40:
            print("   • Hours to days")
        elif entropy < 50:
            print("   • Days to months")
        elif entropy < 60:
            print("   • Months to years")
        else:
            print("   • Centuries (assuming current technology)")

        print("   Note: Advanced attacks may be faster than brute force")

    def get_user_input(self):
        """Get password input from user."""
        return input("\nEnter a password to analyze: ").strip()

    def run(self):
        """Main application loop with enhanced features."""
        self.display_header()

        while True:
            user_input = self.get_user_input()

            # Handle commands
            if user_input.lower() == 'exit':
                print("\n🔐 Thank you for using Advanced Password Analyzer!")
                print("Stay secure! 🛡️")
                break

            elif user_input.lower() == 'help':
                self.display_help()
                continue

            elif user_input.lower() == 'demo':
                self.display_demo()
                continue

            elif not user_input:
                print("⚠️  Please enter a password to analyze.")
                continue

            # Perform advanced analysis
            try:
                result = self.checker.check_password_strength_advanced(user_input)
                self.display_detailed_results(user_input, result)

            except Exception as e:
                print(f"❌ Analysis error: {e}")
                print("Please try again with a different password.")


def main():
    """Entry point for the advanced password analyzer."""
    app = AdvancedPasswordStrengthApp()
    app.run()


if __name__ == "__main__":
    main()