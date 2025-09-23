"""
Password Strength Checker - Main Application
Entry point for the password strength checking application.

This file handles user interaction and delegates password analysis
to the specialized PasswordChecker class.
"""

from password_checker import PasswordChecker


class PasswordStrengthApp:
    """
    Main application class for the password strength checker.

    Handles user interface and coordinates with the PasswordChecker.
    Separating UI from logic makes the code more maintainable.
    """

    def __init__(self):
        """Initialize the application with a password checker instance."""
        self.checker = PasswordChecker()

    def display_header(self):
        """Display the application header."""
        print("=" * 50)
        print("         PASSWORD STRENGTH CHECKER")
        print("=" * 50)
        print("Type 'exit' to quit")
        print("Type 'help' for more information\n")

    def display_help(self):
        """Display help information about password criteria."""
        print("\n" + "=" * 40)
        print("PASSWORD STRENGTH CRITERIA:")
        print("=" * 40)
        print("📏 Length:")
        print("   • 12+ characters = 3 points (Excellent)")
        print("   • 8-11 characters = 2 points (Good)")
        print("   • 6-7 characters = 1 point (Acceptable)")
        print("   • <6 characters = 0 points (Too short)")
        print("\n🔤 Character Types (1 point each):")
        print("   • Lowercase letters (a-z)")
        print("   • Uppercase letters (A-Z)")
        print("   • Numbers (0-9)")
        print("   • Special characters (2 points)")
        print("\n💪 Strength Levels:")
        print("   • 7-8 points = STRONG")
        print("   • 4-6 points = MEDIUM")
        print("   • 0-3 points = WEAK")
        print("=" * 40 + "\n")

    def display_analysis_results(self, password, strength, score, feedback):
        """
        Display the password analysis results in a formatted way.

        Args:
            password (str): The analyzed password (for length info only)
            strength (str): Strength level (WEAK/MEDIUM/STRONG)
            score (int): Numeric score
            feedback (list): List of feedback messages
        """
        print(f"\n{'='*50}")
        print(f"PASSWORD ANALYSIS RESULTS")
        print(f"{'='*50}")
        print(f"Password length: {len(password)} characters")
        print(f"Strength level: {strength}")
        print(f"Total score: {score}/8 points")
        print(f"\nDetailed feedback:")

        for item in feedback:
            print(f"  {item}")

        # Add security tip based on strength
        print(f"\n💡 Security tip:")
        if strength == "WEAK":
            print("   This password could be cracked quickly. Consider using")
            print("   a longer password with mixed character types.")
        elif strength == "MEDIUM":
            print("   This password is decent but could be stronger.")
            print("   Consider adding more characters or special symbols.")
        else:
            print("   This is a strong password! Good security practice.")

        print("=" * 50)

    def get_user_input(self):
        """
        Get password input from user with proper prompting.

        Returns:
            str: User input (password or command)
        """
        return input("Enter a password to analyze: ").strip()

    def run(self):
        """
        Main application loop.

        Handles user interaction, input processing, and result display.
        """
        self.display_header()

        while True:
            user_input = self.get_user_input()

            # Handle exit command
            if user_input.lower() == 'exit':
                print("\nThank you for using Password Strength Checker! 👋")
                print("Remember: Strong passwords protect your digital life!")
                break

            # Handle help command
            elif user_input.lower() == 'help':
                self.display_help()
                continue

            # Handle empty input
            elif not user_input:
                print("⚠️  Please enter a password to analyze.\n")
                continue

            # Analyze the password
            try:
                strength, score, feedback = self.checker.check_password_strength(user_input)
                self.display_analysis_results(user_input, strength, score, feedback)

            except Exception as e:
                print(f"❌ An error occurred during analysis: {e}")
                print("Please try again with a different password.\n")


def main():
    """
    Entry point of the application.

    Creates and runs the main application instance.
    """
    app = PasswordStrengthApp()
    app.run()


if __name__ == "__main__":
    main()