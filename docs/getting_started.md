# Installation Guide

## 📋 Prerequisites

- **Python 3.11 or higher** (Tested on 3.11.16)
- **pip** package manager
- **Git** (for cloning the repository)

### Check Your Python Version

```bash
python --version
# or
python3 --version
```

Should show: `Python 3.11.x` or higher

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/password-strength-checker.git
cd password-strength-checker
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# Activate it (Windows)
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install all dependencies (including dev tools)
pip install -r requirements.txt

# OR install minimal (no dependencies needed for basic functionality!)
# All versions work with Python standard library only
```

### 4. Run the Application

```bash
# Option A: Use version selector
python src/main.py

# Option B: Run specific version directly
python src/basic/main.py
python src/intermediate/main.py
python src/advanced/main.py
python src/pro/main.py
```

---

## 📦 Installation Options

### Option 1: Minimal Installation (Recommended for Learning)

**No external dependencies needed!** All versions use only Python standard library.

```bash
# Just clone and run
git clone https://github.com/YOUR_USERNAME/password-strength-checker.git
cd password-strength-checker
python src/main.py
```

### Option 2: Development Installation (For Contributing)

Install testing and development tools:

```bash
# Install testing framework
pip install pytest pytest-cov coverage

# Install code quality tools
pip install black flake8 mypy isort
```

### Option 3: Full Installation (Everything)

```bash
# Install all dependencies from requirements.txt
pip install -r requirements.txt
```

---

## 🧪 Verify Installation

### Test Basic Functionality

```bash
# Run version selector
python src/main.py

# Select version 1 (Basic) and test with password: MyP@ssw0rd123
```

### Run Tests (if you installed pytest)

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### Check Code Quality (if you installed dev tools)

```bash
# Format code
black src/ tests/

# Check code style
flake8 src/ tests/

# Type checking
mypy src/
```

---

## 🔧 Troubleshooting

### Issue: "No module named 'pytest'"

**Solution:** Either install pytest or run without tests
```bash
pip install pytest
# OR just use the app without running tests
```

### Issue: "Python version too old"

**Solution:** Install Python 3.11+
```bash
# macOS (with Homebrew)
brew install python@3.11

# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install python3.11

# Windows
# Download from python.org
```

### Issue: Virtual environment not activating

**Solution:** Make sure you're in the project directory
```bash
cd password-strength-checker
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### Issue: Import errors when running versions

**Solution:** Make sure you're in the project root directory
```bash
# Your terminal should show
~/password-strength-checker/

# Then run
python src/main.py
```

---

## 🌍 Platform-Specific Notes

### macOS

```bash
# If you have multiple Python versions
python3.11 -m venv .venv
source .venv/bin/activate
```

### Linux

```bash
# May need python3 instead of python
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
# Use backslashes for paths
python -m venv .venv
.venv\Scripts\activate
```

---

## 📚 What Gets Installed

### Core Application
- **Nothing!** Uses only Python standard library
- Works immediately after cloning

### Development Tools (Optional)
- `pytest` - Testing framework
- `black` - Code formatter
- `flake8` - Style checker
- `mypy` - Type checker

### Why No Dependencies?

This project is designed to:
- ✅ Be lightweight and portable
- ✅ Work immediately without installation
- ✅ Teach Python fundamentals
- ✅ Show professional architecture without complexity

---

## ✅ Next Steps

After installation:

1. **Try the Basic version** to understand fundamentals
2. **Explore Intermediate** to learn OOP
3. **Study Advanced** for cybersecurity concepts
4. **Master Pro** for production-ready code

### Quick Test Commands

```bash
# Test each version
python src/basic/main.py
python src/intermediate/main.py
python src/advanced/main.py

# Try Pro version CLI
python src/pro/main.py --generate -c 3
python src/pro/main.py --help
```

---

## 🆘 Need Help?

- Check the main [README.md](README.md) for usage examples
- Review version-specific documentation in `docs/`
- Open an issue on GitHub
- Check Python version: `python --version`
- Verify you're in project root: `pwd` or `cd`

---

## 🎓 For new Developers

### Recommended Setup

1. Use PyCharm or VS Code
2. Create virtual environment
3. Install only pytest for testing
4. Keep it simple - no unnecessary dependencies

### For Portfolio/GitHub

Your project works **immediately** without dependencies:
- Shows professional architecture
- No complex setup required
- Easy for others to try
- Perfect for demonstrations

---

**Happy coding! 🚀**