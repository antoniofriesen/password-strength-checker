"""
Password Strength Checker Package

This package provides tools for analyzing and evaluating password strength
based on industry-standard security criteria.

Main components:
- PasswordChecker: Core analysis functionality
- PasswordStrengthApp: User interface and application logic
"""

from .password_checker import PasswordChecker

__version__ = "1.0.0"
__author__ = "Antonio Friesen"
__email__ = "antonio.friesen1982@gmail.com"

# Package metadata
__all__ = ["PasswordChecker"]