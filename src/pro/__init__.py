"""
Password Strength Checker - Pro Version Package

This package contains the professional-grade version with:
- All Advanced features
- Command-line interface (CLI) with arguments
- Batch processing capabilities
- JSON/CSV export functionality
- Password generation
- Breach database integration (placeholder)
- Performance optimizations
- Logging and reporting
"""

from .password_checker import ProPasswordChecker, PasswordGenerator

__version__ = "4.0.0"
__author__ = "Your Name"
__license__ = "MIT"

__all__ = ["ProPasswordChecker", "PasswordGenerator"]