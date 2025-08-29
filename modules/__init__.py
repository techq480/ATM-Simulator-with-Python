"""
ATM Simulator Modules Package
==============================

This package contains all the modules for the ATM Simulator application.

Modules:
--------
- authentication: User login and PIN validation
- atm_operations: Core ATM operations (deposit, withdraw, etc.)
- user_interface: User interface components and menus
- validation: Input validation functions
- transaction_manager: Transaction recording and history management
- database: Data storage and account management

Author: ATM Development Team
Date: August 2025
Version: 1.0.0
"""

# Import version information
__version__ = "1.0.0"
__author__ = "ATM Development Team"
__email__ = "support@atmsimulator.edu"

# Module imports for easier access
from .authentication import login_user, authenticate_user
from .atm_operations import ATMOperations
from .user_interface import display_welcome, display_menu, get_user_input
from .validation import validate_account_number, validate_pin, validate_amount
from .transaction_manager import add_transaction, get_mini_statement
from .database import initialize_sample_data, get_account

# Define what gets imported with "from modules import *"
__all__ = [
    'login_user',
    'authenticate_user', 
    'ATMOperations',
    'display_welcome',
    'display_menu',
    'get_user_input',
    'validate_account_number',
    'validate_pin',
    'validate_amount',
    'add_transaction',
    'get_mini_statement',
    'initialize_sample_data',
    'get_account'
]