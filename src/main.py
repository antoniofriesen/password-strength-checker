"""
Password Strength Checker - Initial Version
Cybersecurity Learning Project

Starting simple: a function that analyzes basic password criteria
and returns whether it's weak, medium, or strong.
"""


def check_password_strength(password):
    """
    Analyzes password strength with basic criteria.

    Args:
        password (str): The password to be analyzed

    Returns:
        tuple: (strength, score, explanation)
    """

    score = 0
    feedback = []

    # Criterion 1: Length
    if len(password) >= 12:
        score += 3
        feedback.append("✅ Excellent length (12+ characters)")
    elif len(password) >= 8:
        score += 2
        feedback.append("✅ Good length (8+ characters)")
    elif len(password) >= 6:
        score += 1
        feedback.append("⚠️  Acceptable length, but could be longer")
    else:
        feedback.append("❌ Too short! Use at least 6 characters")

    # Criterion 2: Lowercase letters
    if any(c.islower() for c in password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Add lowercase letters (a-z)")

    # Criterion 3: Uppercase letters
    if any(c.isupper() for c in password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")

    # Criterion 4: Numbers
    if any(c.isdigit() for c in password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Add numbers (0-9)")

    # Criterion 5: Special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        score += 2
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Add special characters (!@#$%^&*)")

    if score >= 7:
        strength = "STRONG"
    elif score >= 4:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    return strength, score, feedback


def main():
    """
    Main function - simple interface for testing
    """
    print("=== PASSWORD STRENGTH CHECKER ===")
    print("Type 'exit' to quit\n")

    while True:
        password = input("Enter a password to analyze: ")

        if password.lower() == 'exit':
            print("Goodbye! 👋")
            break

        strength, score, feedback = check_password_strength(password)

        print(f"\n--- PASSWORD ANALYSIS ---")
        print(f"Strength: {strength}")
        print(f"Score: {score}/8 points")
        print(f"\nDetails:")
        for item in feedback:
            print(f"  {item}")
        print("-" * 40)


if __name__ == "__main__":
    main()