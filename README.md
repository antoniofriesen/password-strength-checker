# Password Strength Checker

A Python application to evaluate and analyze password strength using various security criteria and best practices.

## Features

- **Comprehensive Password Analysis**: Evaluates passwords based on multiple security factors
- **Strength Scoring**: Provides detailed scoring and feedback
- **Security Recommendations**: Offers suggestions to improve password security
- **Multiple Input Methods**: Supports single password checks and batch processing
- **Customizable Rules**: Configurable strength criteria

## Installation

### Prerequisites

- Python 3.11.16 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/antoniofriesen/password-strength-checker.git
cd password-strength-checker
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python3 src/main.py
```

### Command Line Interface

```bash
# Check a single password
python3 src/main.py --password "your_password_here"

# Check multiple passwords from a file
python3 src/main.py --file passwords.txt

# Get detailed analysis
python3 src/main.py --password "your_password" --verbose
```

## Password Strength Criteria

The application evaluates passwords based on:

- **Length**: Minimum recommended length (8+ characters)
- **Character Diversity**: 
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- **Pattern Detection**: Identifies common patterns and sequences
- **Dictionary Attacks**: Checks against common password lists
- **Personal Information**: Detects potential personal data usage
- **Entropy Calculation**: Measures password randomness

## Strength Levels

- 🔴 **Weak (0-2)**: High risk, easily compromised
- 🟡 **Moderate (3-5)**: Acceptable but could be stronger
- 🟢 **Strong (6-8)**: Good security level
- 🔵 **Very Strong (9-10)**: Excellent security

## Project Structure

```
password-strength-checker/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── password_checker.py  # Core password analysis logic
│   ├── scoring.py           # Scoring algorithms
│   ├── validators.py        # Password validation rules
│   └── utils.py             # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_password_checker.py
│   ├── test_scoring.py
│   └── test_validators.py
├── data/
│   └── common_passwords.txt  # Common password dictionary
├── requirements.txt
├── README.md
└── .gitignore
```

## Development

### Running Tests

```bash
python3 -m pytest tests/
```

### Code Style

This project follows PEP 8 style guidelines. Format code with:

```bash
black src/ tests/
flake8 src/ tests/
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Security Considerations

⚠️ **Important Security Notes:**

- This tool is for educational and security assessment purposes
- Never store actual passwords in plain text
- Use this tool to evaluate password policies and user education
- Consider implementing proper password hashing in production systems

## Dependencies

- `argparse`: Command-line interface
- `re`: Pattern matching and validation
- `math`: Entropy calculations
- `json`: Configuration and data handling

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Roadmap

- [ ] Web interface implementation
- [ ] Integration with password managers
- [ ] Multi-language support
- [ ] Advanced pattern detection
- [ ] Breach database integration
- [ ] Custom rule configuration GUI

## Support

If you encounter any issues or have suggestions, please [open an issue](https://github.com/YOUR_USERNAME/password-strength-checker/issues) on GitHub.

---

**Disclaimer**: This tool is for educational purposes. Always follow your organization's security policies and use proper security practices when handling passwords.