# Password Strength Checker

**A Multi-Version Python Application for Password Security Analysis**

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive password strength analysis tool with four progressive versions, from basic Python fundamentals to production-ready cybersecurity features. Perfect for learning, portfolio projects, and real-world security assessments.

---

## 🎯 Project Overview

This project demonstrates the evolution of a password strength checker from simple functions to production-grade code, showcasing:

- ✅ **Progressive Learning Path** - From basic to advanced concepts
- ✅ **Software Architecture** - Clean, scalable design patterns
- ✅ **Cybersecurity Concepts** - Real security analysis techniques
- ✅ **Production-Ready Code** - CLI tools, batch processing, exports
- ✅ **Best Practices** - Testing, documentation, type hints

Perfect for **Ausbildung portfolios**, **cybersecurity learning**, and **professional development**.

---

## 📦 Four Versions, One Project

| Version | Complexity | Focus | Best For |
|---------|-----------|-------|----------|
| **[Basic](#-basic-version)** | ⭐ | Functions, loops, conditionals | Python fundamentals |
| **[Intermediate](#-intermediate-version)** | ⭐⭐ | Classes, OOP, architecture | Software design |
| **[Advanced](#-advanced-version)** | ⭐⭐⭐ | Entropy, patterns, security | Cybersecurity concepts |
| **[Pro](#-pro-version)** | ⭐⭐⭐⭐ | CLI, batch, exports | Production tools |

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/antoniofriesen/password-strength-checker.git
cd password-strength-checker

# Create virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# No dependencies needed! Uses Python standard library only
# Optional: Install testing/dev tools
pip install -r requirements.txt
```

### Run the Version Selector

```bash
# Interactive version chooser
python src/main.py
```

### Run Specific Versions Directly

```bash
# Basic version
python src/basic/main.py

# Intermediate version
python src/intermediate/main.py

# Advanced version
python src/advanced/main.py

# Pro version (with CLI)
python src/pro/main.py --help
```

---

## 📚 Version Details

### 🟢 Basic Version

**Focus:** Python Fundamentals

Simple function-based password checker perfect for learning Python basics.

**Features:**
- Length checking (6, 8, 12+ characters)
- Character type detection (lowercase, uppercase, digits, special)
- 8-point scoring system
- Simple feedback messages

**What You Learn:**
- Functions and parameters
- Loops and conditionals
- String manipulation
- Tuple unpacking

**Usage:**
```bash
python src/basic/main.py
```

```python
# Test passwords
123          → WEAK (0-3 points)
Password123  → MEDIUM (4-6 points)
MyP@ssw0rd!  → STRONG (7-8 points)
```

---

### 🔵 Intermediate Version

**Focus:** Object-Oriented Programming

Class-based architecture with separated concerns and modular design.

**Features:**
- All Basic features
- `PasswordChecker` class with modular methods
- `PasswordStrengthApp` class for UI
- Enhanced error handling
- Help system
- Professional code organization

**What You Learn:**
- Class design and OOP principles
- Separation of concerns (UI vs Logic)
- Method organization
- Error handling patterns

**Usage:**
```bash
python src/intermediate/main.py
# Commands: analyze, help, exit
```

**Architecture:**
```
PasswordChecker (Logic)
    ├── analyze_length()
    ├── analyze_lowercase()
    ├── analyze_uppercase()
    ├── analyze_digits()
    └── analyze_special_characters()

PasswordStrengthApp (UI)
    ├── display_header()
    ├── display_help()
    ├── display_results()
    └── run() - main loop
```

---

### 🟣 Advanced Version

**Focus:** Cybersecurity Concepts

Professional security analysis with mathematical foundations and threat detection.

**Features:**
- All Intermediate features
- **Entropy calculation** (bits of randomness)
- **Common password detection** (50+ password database)
- **Pattern recognition** (keyboard patterns, sequences, repetition)
- **100-point scoring system**
- Detailed analytics with progress bars
- Security recommendations
- Crack time estimates
- Demo mode with sample passwords

**What You Learn:**
- Information theory (entropy)
- Security threat modeling
- Pattern recognition algorithms
- Statistical analysis
- Professional security concepts

**Usage:**
```bash
python src/advanced/main.py
# Commands: analyze, help, demo, exit
```

**Security Features:**
```python
# Entropy Calculation
"password123" → 51.7 bits (Fair)
"X9$mK#nP2@vL8*qR" → 96.3 bits (Excellent)

# Pattern Detection
"qwerty123" → Keyboard pattern detected
"password123" → Common password + number suffix
"aaabbb111" → Repetition pattern detected

# Scoring Breakdown
Length:           12/15 points
Character types:  25/25 points
Entropy:          25/30 points
Common password:  -20 points (PENALTY)
Patterns:         -4 points (PENALTY)
Uniqueness:       8.5/10 points
──────────────────────────
Total:            46.5/100 (MEDIUM)
```

---

### 🔴 Pro Version

**Focus:** Production-Ready Tool

Command-line interface with batch processing, exports, and password generation.

**Features:**
- All Advanced features
- **Full CLI with argparse** (like professional tools)
- **Batch processing** (analyze multiple passwords)
- **JSON/CSV export** with metadata
- **Secure password generation** (cryptographically secure)
- **Passphrase generation** (word-based passwords)
- **Statistics tracking** (averages, distributions)
- **Interactive and command modes**
- Type hints and professional code

**What You Learn:**
- CLI design with argparse
- Batch processing and statistics
- File I/O (JSON, CSV)
- Cryptographically secure random (secrets module)
- Production code patterns
- Performance optimization

**Usage:**

```bash
# Interactive mode
python src/pro/main.py -i

# Single password analysis
python src/pro/main.py -p "MyPassword123!" -v

# Batch processing with export
python src/pro/main.py -f passwords.txt -o report.json

# Generate passwords
python src/pro/main.py --generate -c 5 -l 20

# Generate passphrases
python src/pro/main.py --passphrase -c 3 -w 5

# Full help
python src/pro/main.py --help
```

**CLI Examples:**
```bash
# Analyze single password with verbose output
python src/pro/main.py -p "Tr0ub4dor&3" -v

# Batch analyze from file, export to CSV
python src/pro/main.py -f passwords.txt -o report.csv -F csv

# Generate 10 passwords (16 chars, no ambiguous chars)
python src/pro/main.py --generate -c 10 --exclude-ambiguous

# Generate passphrases with underscores
python src/pro/main.py --passphrase -c 5 --separator "_"
```

**Export Formats:**

*JSON Export:*
```json
{
  "metadata": {
    "version": "4.0.0",
    "export_time": "2024-01-15T10:30:00",
    "total_passwords": 100
  },
  "statistics": {
    "average_score": 65.5,
    "average_entropy": 45.2,
    "strength_distribution": {...}
  },
  "results": [...]
}
```

*CSV Export:*
```csv
password_length,strength_level,total_score,percentage,entropy,is_common,patterns_found
12,STRONG,75.5,75.5,52.3,False,None
8,WEAK,35.0,35.0,28.1,True,"keyboard: qwerty"
```

---

## 🎓 Learning Path

### For Beginners (Python Fundamentals)
1. Start with **Basic** version
2. Understand functions, loops, conditionals
3. Learn string manipulation and basic data structures

### For Intermediate Developers (Software Architecture)
1. Study **Intermediate** version
2. Learn OOP principles and class design
3. Understand separation of concerns
4. Practice modular code organization

### For Security Students (Cybersecurity)
1. Dive into **Advanced** version
2. Learn entropy and information theory
3. Understand attack vectors and patterns
4. Study threat modeling concepts

### For Professional Development (Production Code)
1. Master **Pro** version
2. Learn CLI design patterns
3. Practice batch processing and data export
4. Understand production code standards

---

## 📊 Feature Comparison

| Feature | Basic | Intermediate | Advanced | Pro |
|---------|-------|--------------|----------|-----|
| Length checking | ✅ | ✅ | ✅ | ✅ |
| Character diversity | ✅ | ✅ | ✅ | ✅ |
| Class-based design | ❌ | ✅ | ✅ | ✅ |
| Help system | ❌ | ✅ | ✅ | ✅ |
| Entropy calculation | ❌ | ❌ | ✅ | ✅ |
| Common passwords | ❌ | ❌ | ✅ | ✅ |
| Pattern detection | ❌ | ❌ | ✅ | ✅ |
| Demo mode | ❌ | ❌ | ✅ | ❌ |
| CLI arguments | ❌ | ❌ | ❌ | ✅ |
| Batch processing | ❌ | ❌ | ❌ | ✅ |
| JSON/CSV export | ❌ | ❌ | ❌ | ✅ |
| Password generation | ❌ | ❌ | ❌ | ✅ |
| Statistics tracking | ❌ | ❌ | ❌ | ✅ |
| **Scoring System** | 8-point | 8-point | 100-point | 100-point |
| **Lines of Code** | ~100 | ~200 | ~400 | ~800 |

---

## 🏗️ Project Structure

```
password-strength-checker/
├── src/
│   ├── basic/                    # Version 1: Fundamentals
│   │   ├── __init__.py
│   │   └── main.py
│   ├── intermediate/             # Version 2: OOP
│   │   ├── __init__.py
│   │   ├── password_checker.py
│   │   └── main.py
│   ├── advanced/                 # Version 3: Security
│   │   ├── __init__.py
│   │   ├── password_checker.py
│   │   └── main.py
│   ├── pro/                      # Version 4: Production
│   │   ├── __init__.py
│   │   ├── password_checker.py
│   │   └── main.py
│   └── main.py                   # Version selector
├── tests/
│   ├── test_basic.py
│   ├── test_intermediate.py
│   └── test_advanced.py
├── docs/
│   ├── getting_started.md
│   ├── version_comparison.md
│   └── security_concepts.md
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific version tests
pytest tests/test_intermediate.py -v
```

**Test Coverage:**
- Unit tests for all analysis methods
- Edge case testing
- Integration tests
- Type checking with mypy

---

## 🔐 Security Concepts Implemented

### Entropy Calculation
```
Entropy = password_length × log₂(character_set_size)

Example:
"password" → 8 × log₂(26) = 37.6 bits (lowercase only)
"Password123!" → 12 × log₂(68) = 73.2 bits (mixed)
```

### Common Password Detection
- Database of 50+ most common passwords
- Variation detection (password123, password!)
- Prefix matching

### Pattern Recognition
- **Keyboard patterns**: qwerty, asdf, 12345
- **Sequential patterns**: abc, 123, xyz
- **Repetition**: aaa, 111, !!!
- **Number suffixes**: password123

### Attack Vector Analysis
- Dictionary attacks
- Pattern-based attacks
- Brute force considerations
- Crack time estimation

---

## 🎯 Use Cases

### Educational
- Learn Python programming
- Study OOP principles
- Understand cybersecurity concepts
- Practice software architecture

### Portfolio
- Showcase progressive learning
- Demonstrate code evolution
- Show security knowledge
- Present production-ready code

### Professional
- Password policy enforcement
- Security audits
- User education
- Compliance reporting

### Training
- Practical coding examples
- Real-world application
- Professional documentation
- Industry-standard patterns

---

## 💡 Development

### Code Quality

```bash
# Format code
black src/ tests/

# Check style
flake8 src/ tests/

# Type checking
mypy src/
```

### Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📖 Documentation

- **[Getting Started Guide](docs/getting_started.md)** - Installation and setup
- **[Version Comparison](docs/version_comparison.md)** - Detailed version differences
- **[Security Concepts](docs/security_concepts.md)** - Cybersecurity explanations
- **[API Documentation](docs/api.md)** - Code reference (coming soon)

---

## 🔒 Security Notes

⚠️ **Important:**
- This tool is for **educational and assessment purposes**
- Never store actual passwords in plain text
- Use for password policy evaluation and user education
- In production, always use proper password hashing (bcrypt, Argon2)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by real-world password strength checkers
- Built for cybersecurity learning
- Follows NIST password guidelines
- Implements OWASP best practices

---

## 🗺️ Roadmap

- [x] Basic version with fundamentals
- [x] Intermediate version with OOP
- [x] Advanced version with security features
- [x] Pro version with CLI and exports
- [ ] Web interface (Flask/FastAPI)
- [ ] REST API endpoints
- [ ] HaveIBeenPwned integration
- [ ] Password manager integration
- [ ] Multi-language support
- [ ] GUI application (Tkinter/PyQt)

---

## 📧 Contact

**Antonio Friesen**
- GitHub: [@antoniofriesen](https://github.com/antoniofriesen)
- Project: [password-strength-checker](https://github.com/antoniofriesen/password-strength-checker)

---

## ⭐ Support

If you find this project helpful:
- ⭐ Star the repository
- 🐛 Report bugs via issues
- 💡 Suggest features
- 🤝 Contribute code

---

**Made with ❤️ for learning, security, and professional development**

*Perfect for portfolios and cybersecurity career development* 🔐