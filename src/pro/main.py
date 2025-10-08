"""
Pro Password Strength Checker - Main Application
Production-ready CLI with advanced features

Features:
- Command-line arguments
- Batch processing
- JSON/CSV export
- Password generation
- Statistics and reporting
- Multiple operation modes
"""

import argparse
import sys
from pathlib import Path
from typing import List
from password_checker import ProPasswordChecker, PasswordGenerator


class ProPasswordApp:
    """
    Professional CLI application for password analysis.
    """

    def __init__(self):
        """Initialize the pro application."""
        self.checker = ProPasswordChecker()
        self.generator = PasswordGenerator()

    def analyze_single(self, password: str, verbose: bool = False):
        """Analyze a single password."""
        result = self.checker.analyze_password(password)
        self.display_result(result, verbose)

    def analyze_file(self, filepath: str, output: str = None, format: str = 'json', verbose: bool = False):
        """Analyze passwords from a file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                passwords = [line.strip() for line in f if line.strip()]

            print(f"📂 Analyzing {len(passwords)} passwords from '{filepath}'...")
            print()

            results = self.checker.analyze_batch(passwords)

            # Display summary
            self.display_batch_summary(results)

            # Export if requested
            if output:
                self.export_results(results, output, format)

            # Display individual results if verbose
            if verbose:
                print("\n" + "=" * 80)
                print("INDIVIDUAL RESULTS:")
                print("=" * 80)
                for i, result in enumerate(results, 1):
                    print(f"\n--- Password {i} ---")
                    self.display_result(result, compact=True)

        except FileNotFoundError:
            print(f"❌ Error: File '{filepath}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error analyzing file: {e}")
            sys.exit(1)

    def generate_passwords(self, count: int = 1, length: int = 16,
                           no_special: bool = False, no_uppercase: bool = False,
                           exclude_ambiguous: bool = False):
        """Generate secure passwords."""
        print(f"🔐 Generating {count} secure password(s)...\n")

        passwords = self.generator.generate_multiple(
            count=count,
            length=length,
            use_special=not no_special,
            use_uppercase=not no_uppercase,
            exclude_ambiguous=exclude_ambiguous
        )

        for i, pwd in enumerate(passwords, 1):
            print(f"Password {i}: {pwd}")

            # Analyze generated password
            result = self.checker.analyze_password(pwd, update_stats=False)
            print(f"  Strength: {result['strength_level']} ({result['total_score']:.0f}/100)")
            print(f"  Entropy: {result['entropy']:.1f} bits")
            print()

    def generate_passphrase(self, count: int = 1, words: int = 4, separator: str = '-'):
        """Generate passphrase."""
        print(f"📝 Generating {count} passphrase(s)...\n")

        for i in range(count):
            passphrase = self.generator.generate_passphrase(word_count=words, separator=separator)
            print(f"Passphrase {i + 1}: {passphrase}")

            # Analyze generated passphrase
            result = self.checker.analyze_password(passphrase, update_stats=False)
            print(f"  Strength: {result['strength_level']} ({result['total_score']:.0f}/100)")
            print(f"  Entropy: {result['entropy']:.1f} bits")
            print()

    def display_result(self, result: dict, verbose: bool = False, compact: bool = False):
        """Display analysis result."""
        if compact:
            # Compact display for batch processing
            print(f"Length: {result['password_length']} | "
                  f"Strength: {result['strength_level']} | "
                  f"Score: {result['total_score']:.0f}/100 | "
                  f"Entropy: {result['entropy']:.1f} bits")
            if result['is_common']:
                print("  ⚠️  Common password detected")
            if result['patterns_found']:
                print(f"  ⚠️  Patterns: {', '.join(result['patterns_found'][:2])}")
        else:
            # Full display
            print("=" * 80)
            print("PASSWORD ANALYSIS RESULT")
            print("=" * 80)
            print(f"Length: {result['password_length']} characters")
            print(f"Strength: {result['strength_level']}")
            print(f"Score: {result['total_score']:.1f}/{result['max_score']} ({result['percentage']:.1f}%)")

            # Progress bar
            progress = int(result['percentage'] / 5)
            bar = "█" * progress + "░" * (20 - progress)
            print(f"Progress: [{bar}] {result['percentage']:.1f}%")

            if verbose:
                print(f"\n📊 SCORE BREAKDOWN:")
                for category, score in result['score_breakdown'].items():
                    print(f"  • {category.replace('_', ' ').title()}: {score}")

                print(f"\n🔐 SECURITY METRICS:")
                print(f"  • Entropy: {result['entropy']:.1f} bits")
                print(f"  • Character set size: {result['char_set_size']}")
                print(f"  • Common password: {'Yes ❌' if result['is_common'] else 'No ✅'}")
                print(f"  • Patterns detected: {len(result['patterns_found'])}")

                if result['patterns_found']:
                    for pattern in result['patterns_found']:
                        print(f"    - {pattern}")

                print(f"\n📝 FEEDBACK:")
                for feedback in result['feedback']:
                    print(f"  {feedback}")

                if result['recommendations']:
                    print(f"\n💡 RECOMMENDATIONS:")
                    for rec in result['recommendations']:
                        print(f"  {rec}")

            print("=" * 80)

    def display_batch_summary(self, results: List[dict]):
        """Display summary statistics for batch analysis."""
        stats = self.checker.get_batch_statistics()

        print("\n" + "=" * 80)
        print("BATCH ANALYSIS SUMMARY")
        print("=" * 80)
        print(f"Total passwords analyzed: {stats['total_analyzed']}")
        print(f"Average score: {stats['average_score']:.1f}/100")
        print(f"Average entropy: {stats['average_entropy']:.1f} bits")
        print(f"Common passwords found: {stats['common_password_count']}")
        print(f"Passwords with patterns: {stats['pattern_detected_count']}")

        print(f"\n📊 STRENGTH DISTRIBUTION:")
        for level, count in stats['strength_distribution'].items():
            percentage = (count / stats['total_analyzed'] * 100) if stats['total_analyzed'] > 0 else 0
            bar_length = int(percentage / 5)
            bar = "█" * bar_length
            print(f"  {level:12}: {count:3} ({percentage:5.1f}%) {bar}")

        print("=" * 80)

    def export_results(self, results: List[dict], output: str, format: str):
        """Export results to file."""
        try:
            if format.lower() == 'json':
                self.checker.export_to_json(results, output)
                print(f"\n✅ Results exported to JSON: {output}")
            elif format.lower() == 'csv':
                self.checker.export_to_csv(results, output)
                print(f"\n✅ Results exported to CSV: {output}")
            else:
                print(f"❌ Unsupported format: {format}")
        except Exception as e:
            print(f"❌ Error exporting results: {e}")

    def interactive_mode(self):
        """Run in interactive mode."""
        print("=" * 80)
        print("    PRO PASSWORD STRENGTH ANALYZER - INTERACTIVE MODE")
        print("    🔐 Production-Grade Security Analysis 🔐")
        print("=" * 80)
        print("\nCommands:")
        print("  analyze <password>  - Analyze a password")
        print("  generate [length]   - Generate a password")
        print("  passphrase [words]  - Generate a passphrase")
        print("  stats              - Show statistics")
        print("  reset              - Reset statistics")
        print("  help               - Show this help")
        print("  exit               - Quit")
        print()

        while True:
            try:
                user_input = input("pro> ").strip()

                if not user_input:
                    continue

                parts = user_input.split()
                command = parts[0].lower()

                if command == 'exit':
                    print("\n🔐 Thank you for using Pro Password Analyzer!")
                    break

                elif command == 'help':
                    self.show_help()

                elif command == 'analyze':
                    if len(parts) < 2:
                        print("Usage: analyze <password>")
                    else:
                        password = ' '.join(parts[1:])
                        self.analyze_single(password, verbose=True)

                elif command == 'generate':
                    length = int(parts[1]) if len(parts) > 1 else 16
                    self.generate_passwords(count=1, length=length)

                elif command == 'passphrase':
                    words = int(parts[1]) if len(parts) > 1 else 4
                    self.generate_passphrase(count=1, words=words)

                elif command == 'stats':
                    stats = self.checker.get_batch_statistics()
                    if stats['total_analyzed'] == 0:
                        print("No passwords analyzed yet.")
                    else:
                        print("\n📊 SESSION STATISTICS:")
                        print(f"Total analyzed: {stats['total_analyzed']}")
                        print(f"Average score: {stats['average_score']:.1f}/100")
                        print(f"Average entropy: {stats['average_entropy']:.1f} bits")
                        print(f"Common passwords: {stats['common_password_count']}")
                        print(f"Patterns detected: {stats['pattern_detected_count']}")

                elif command == 'reset':
                    self.checker.reset_statistics()
                    print("✅ Statistics reset.")

                else:
                    print(f"Unknown command: {command}")
                    print("Type 'help' for available commands.")

            except KeyboardInterrupt:
                print("\n\nUse 'exit' to quit.")
            except Exception as e:
                print(f"❌ Error: {e}")

    def show_help(self):
        """Show detailed help."""
        print("\n" + "=" * 80)
        print("PRO PASSWORD ANALYZER - HELP")
        print("=" * 80)
        print("\nINTERACTIVE COMMANDS:")
        print("  analyze <password>     - Analyze password strength")
        print("  generate [length]      - Generate secure password (default: 16)")
        print("  passphrase [words]     - Generate passphrase (default: 4 words)")
        print("  stats                  - Show session statistics")
        print("  reset                  - Reset statistics")
        print("  help                   - Show this help")
        print("  exit                   - Exit application")

        print("\nCLI USAGE:")
        print("  python main.py -p <password>              - Analyze single password")
        print("  python main.py -f <file> -o <output>      - Batch analyze from file")
        print("  python main.py --generate -c 5            - Generate 5 passwords")
        print("  python main.py --passphrase -c 3          - Generate 3 passphrases")

        print("\nFEATURES:")
        print("  ✓ Entropy calculation (mathematical randomness)")
        print("  ✓ Common password detection")
        print("  ✓ Pattern recognition (keyboard, sequences)")
        print("  ✓ Batch processing with statistics")
        print("  ✓ JSON/CSV export")
        print("  ✓ Secure password generation")
        print("  ✓ Passphrase generation")
        print("=" * 80 + "\n")


def create_parser():
    """Create command-line argument parser."""
    parser = argparse.ArgumentParser(
        description='Pro Password Strength Analyzer - Production-grade security tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -p "MyPassword123!"                    # Analyze single password
  %(prog)s -f passwords.txt -o report.json        # Batch analysis with JSON export
  %(prog)s -f passwords.txt -o report.csv -F csv  # Batch analysis with CSV export
  %(prog)s --generate -c 5 -l 20                  # Generate 5 passwords (20 chars each)
  %(prog)s --passphrase -c 3 -w 5                 # Generate 3 passphrases (5 words each)
  %(prog)s -i                                     # Interactive mode
        """
    )

    # Operation modes
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('-p', '--password',
                            help='Analyze a single password')
    mode_group.add_argument('-f', '--file',
                            help='Analyze passwords from file (one per line)')
    mode_group.add_argument('--generate', action='store_true',
                            help='Generate secure password(s)')
    mode_group.add_argument('--passphrase', action='store_true',
                            help='Generate passphrase(s)')
    mode_group.add_argument('-i', '--interactive', action='store_true',
                            help='Run in interactive mode')

    # Analysis options
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Show detailed analysis')

    # Output options
    parser.add_argument('-o', '--output',
                        help='Output file for batch analysis results')
    parser.add_argument('-F', '--format', choices=['json', 'csv'], default='json',
                        help='Output format (default: json)')

    # Generation options
    parser.add_argument('-c', '--count', type=int, default=1,
                        help='Number of passwords/passphrases to generate (default: 1)')
    parser.add_argument('-l', '--length', type=int, default=16,
                        help='Password length (default: 16)')
    parser.add_argument('-w', '--words', type=int, default=4,
                        help='Number of words in passphrase (default: 4)')
    parser.add_argument('--no-special', action='store_true',
                        help='Exclude special characters')
    parser.add_argument('--no-uppercase', action='store_true',
                        help='Exclude uppercase letters')
    parser.add_argument('--exclude-ambiguous', action='store_true',
                        help='Exclude ambiguous characters (0, O, l, 1, etc.)')
    parser.add_argument('--separator', default='-',
                        help='Passphrase word separator (default: -)')

    return parser


def main():
    """Main entry point for Pro Password Analyzer."""
    parser = create_parser()
    args = parser.parse_args()

    app = ProPasswordApp()

    try:
        # Interactive mode
        if args.interactive:
            app.interactive_mode()

        # Single password analysis
        elif args.password:
            app.analyze_single(args.password, verbose=args.verbose)

        # File batch analysis
        elif args.file:
            app.analyze_file(args.file, output=args.output,
                             format=args.format, verbose=args.verbose)

        # Password generation
        elif args.generate:
            app.generate_passwords(count=args.count, length=args.length,
                                   no_special=args.no_special,
                                   no_uppercase=args.no_uppercase,
                                   exclude_ambiguous=args.exclude_ambiguous)

        # Passphrase generation
        elif args.passphrase:
            app.generate_passphrase(count=args.count, words=args.words,
                                    separator=args.separator)

        # Default: show help and enter interactive mode
        else:
            parser.print_help()
            print("\n" + "=" * 80)
            print("No arguments provided. Entering interactive mode...")
            print("=" * 80 + "\n")
            app.interactive_mode()

    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()