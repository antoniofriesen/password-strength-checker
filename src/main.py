"""
Password Strength Checker - Version Selector
Launch any version of the password strength checker

This launcher allows you to choose which version to run:
- Basic: Simple checker for learning fundamentals
- Intermediate: Enhanced with OOP architecture
- Advanced: Full security analysis with entropy & patterns
- Pro: Professional-grade (coming soon)
"""

import sys
import os


def display_welcome():
    """Display welcome banner."""
    print("=" * 70)
    print(" " * 15 + "PASSWORD STRENGTH CHECKER")
    print(" " * 20 + "Version Selector")
    print("=" * 70)
    print()


def display_versions():
    """Display available versions with descriptions."""
    versions = {
        "1": {
            "name": "Basic",
            "path": "basic.main",
            "description": "Simple character-based analysis",
            "features": [
                "✓ Length checking",
                "✓ Character type detection",
                "✓ 8-point scoring",
                "✓ Simple feedback"
            ],
            "best_for": "Learning Python basics & fundamentals"
        },
        "2": {
            "name": "Intermediate",
            "path": "intermediate.main",
            "description": "Object-oriented architecture",
            "features": [
                "✓ All Basic features",
                "✓ Class-based design",
                "✓ Modular methods",
                "✓ Enhanced UI with help",
                "✓ Better error handling"
            ],
            "best_for": "Learning OOP & software architecture"
        },
        "3": {
            "name": "Advanced",
            "path": "advanced.main",
            "description": "Cybersecurity-grade analysis",
            "features": [
                "✓ All Intermediate features",
                "✓ Entropy calculation",
                "✓ Common password detection",
                "✓ Pattern recognition",
                "✓ 100-point scoring",
                "✓ Detailed analytics",
                "✓ Demo mode"
            ],
            "best_for": "Learning cybersecurity concepts"
        },
        "4": {
            "name": "Pro",
            "path": "pro.main",
            "description": "Production-grade CLI tool",
            "features": [
                "✓ All Advanced features",
                "✓ Password generation",
                "✓ Passphrase generation",
                "✓ CLI with arguments",
                "✓ Batch processing",
                "✓ JSON/CSV export",
                "✓ Statistics tracking"
            ],
            "best_for": "Production use & portfolio showcase"
        }
    }

    print("📦 AVAILABLE VERSIONS:\n")

    for num, info in versions.items():
        status = info.get('status', '✅ Available')
        print(f"{num}. {info['name']} - {info['description']}")
        print(f"   Status: {status}")
        print(f"   Best for: {info['best_for']}")
        print(f"   Features:")
        for feature in info['features']:
            print(f"      {feature}")
        print()

    return versions


def get_user_choice(versions):
    """Get version choice from user."""
    while True:
        print("=" * 70)
        choice = input("Select version (1-4) or 'q' to quit: ").strip().lower()

        if choice == 'q':
            print("\nGoodbye! 👋")
            sys.exit(0)

        if choice in versions:
            # Check if version is available
            if 'status' in versions[choice] and '🚧' in versions[choice]['status']:
                print(f"\n⚠️  {versions[choice]['name']} version is still in development.")
                print("Please choose another version.\n")
                continue
            return choice
        else:
            print("\n❌ Invalid choice. Please select 1-4 or 'q' to quit.\n")


def launch_version(version_info):
    """Launch the selected version."""
    print(f"\n🚀 Launching {version_info['name']} version...")
    print("=" * 70)
    print()

    try:
        # Import and run the selected version
        module_path = version_info['path']

        # Dynamic import
        module_parts = module_path.split('.')
        module = __import__(f"src.{module_parts[0]}.{module_parts[1]}",
                           fromlist=[module_parts[1]])

        # Run the main function
        module.main()

    except ImportError as e:
        print(f"❌ Error: Could not load {version_info['name']} version.")
        print(f"Details: {e}")
        print("\nMake sure the version files exist in the correct directory:")
        print(f"  src/{module_parts[0]}/{module_parts[1]}.py")
        print()
    except Exception as e:
        print(f"❌ Error running {version_info['name']} version: {e}")
        print()


def display_quick_start():
    """Display quick start information."""
    print("\n💡 QUICK START:")
    print("   • Choose a version based on your learning goals")
    print("   • Start with Basic if you're new to Python")
    print("   • Try Advanced to learn cybersecurity concepts")
    print("   • Each version builds on the previous one")
    print()


def display_direct_launch_info():
    """Show how to launch versions directly."""
    print("📌 TIP: You can also launch versions directly:")
    print("   python src/basic/main.py")
    print("   python src/intermediate/main.py")
    print("   python src/advanced/main.py")
    print("   python src/pro/main.py")
    print()


def main():
    """Main launcher function."""
    # Add src directory to path for imports
    sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

    display_welcome()
    display_quick_start()

    versions = display_versions()

    display_direct_launch_info()

    choice = get_user_choice(versions)
    launch_version(versions[choice])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user. Goodbye! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)