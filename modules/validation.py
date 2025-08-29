"""
Validation Module
Handles all input validation for the ATM system including account numbers,
PINs, amounts, and menu choices.
"""

import re
from modules.user_interface import display_error


def validate_account_number(account_number):
    """
    Validate account number format and length.
    
    Args:
        account_number (str): Account number to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not account_number:
        display_error("Account number cannot be empty.")
        return False
        
    if not account_number.isdigit():
        display_error("Account number must contain only digits.")
        return False
        
    if len(account_number) < 6 or len(account_number) > 12:
        display_error("Account number must be between 6 and 12 digits.")
        return False
        
    return True


def validate_pin(pin):
    """
    Validate PIN format - must be exactly 4 digits.
    
    Args:
        pin (str): PIN to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not pin:
        display_error("PIN cannot be empty.")
        return False
        
    if not pin.isdigit():
        display_error("PIN must contain only digits.")
        return False
        
    if len(pin) != 4:
        display_error("PIN must be exactly 4 digits.")
        return False
        
    return True


def validate_amount(amount_str):
    """
    Validate monetary amount input.
    
    Args:
        amount_str (str): Amount string to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not amount_str:
        display_error("Amount cannot be empty.")
        return False
        
    # Remove common currency symbols and spaces
    cleaned_amount = amount_str.replace('$', '').replace(',', '').strip()
    
    try:
        amount = float(cleaned_amount)
        
        if amount < 0:
            display_error("Amount cannot be negative.")
            return False
            
        if amount == 0:
            display_error("Amount must be greater than zero.")
            return False
            
        # Check for reasonable maximum amount (prevent very large transactions)
        if amount > 10000:
            display_error("Amount cannot exceed $10,000 per transaction.")
            return False
            
        # Check for too many decimal places
        decimal_places = len(str(amount).split('.')[-1]) if '.' in str(amount) else 0
        if decimal_places > 2:
            display_error("Amount cannot have more than 2 decimal places.")
            return False
            
        return True
        
    except ValueError:
        display_error("Please enter a valid numeric amount.")
        return False


def validate_menu_choice(choice):
    """
    Validate menu choice input.
    
    Args:
        choice (str): Menu choice to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not choice:
        display_error("Please select an option.")
        return False
        
    if not choice.isdigit():
        display_error("Please enter a valid number.")
        return False
        
    choice_num = int(choice)
    if choice_num < 1 or choice_num > 6:
        display_error("Please select a number between 1 and 6.")
        return False
        
    return True


def validate_name(name):
    """
    Validate name input for account creation.
    
    Args:
        name (str): Name to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not name or not name.strip():
        display_error("Name cannot be empty.")
        return False
        
    if len(name.strip()) < 2:
        display_error("Name must be at least 2 characters long.")
        return False
        
    if len(name.strip()) > 50:
        display_error("Name cannot exceed 50 characters.")
        return False
        
    # Check for valid characters (letters, spaces, hyphens, apostrophes)
    if not re.match(r"^[a-zA-Z\s\-']+$", name.strip()):
        display_error("Name can only contain letters, spaces, hyphens, and apostrophes.")
        return False
        
    return True


def sanitize_input(user_input):
    """
    Sanitize user input by removing potentially harmful characters.
    
    Args:
        user_input (str): Input to sanitize
        
    Returns:
        str: Sanitized input
    """
    if not user_input:
        return ""
        
    # Remove null bytes and control characters
    sanitized = ''.join(char for char in user_input if ord(char) >= 32 or char in '\t\n')
    
    # Limit length to prevent buffer overflow attempts
    return sanitized[:1000]


def is_valid_transaction_amount(amount, current_balance, transaction_type="withdrawal"):
    """
    Validate transaction amount against account balance and limits.
    
    Args:
        amount (float): Transaction amount
        current_balance (float): Current account balance
        transaction_type (str): Type of transaction ('withdrawal' or 'deposit')
        
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if transaction_type == "withdrawal":
        if amount > current_balance:
            return False, f"Insufficient funds. Available balance: ${current_balance:,.2f}"
            
        # ATM daily withdrawal limit
        if amount > 1000:
            return False, "Daily withdrawal limit is $1,000."
            
    elif transaction_type == "deposit":
        # ATM deposit limit
        if amount > 5000:
            return False, "Daily deposit limit is $5,000."
    
    return True, ""