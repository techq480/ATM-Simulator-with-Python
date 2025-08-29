"""
Authentication Module for ATM Simulator
Handles user login, PIN validation, and account locking functionality.
"""

from modules.validation import validate_account_number, validate_pin
from modules.user_interface import get_user_input
import time


def authenticate_user(account, entered_pin):
    """
    Authenticate user by checking PIN.
    
    Args:
        account (dict): User account data
        entered_pin (str): PIN entered by user
        
    Returns:
        bool: True if authentication successful, False otherwise
    """
    return account['pin'] == entered_pin and not account['locked']


def handle_failed_attempt(account):
    """
    Handle failed login attempt by incrementing attempt counter.
    
    Args:
        account (dict): User account data
        
    Returns:
        bool: True if account should be locked, False otherwise
    """
    account['failed_attempts'] += 1
    remaining_attempts = 3 - account['failed_attempts']
    
    if account['failed_attempts'] >= 3:
        account['locked'] = True
        return True
    
    print(f"\n❌ Incorrect PIN. You have {remaining_attempts} attempt(s) remaining.")
    return False


def reset_failed_attempts(account):
    """
    Reset failed attempts counter upon successful login.
    
    Args:
        account (dict): User account data
    """
    account['failed_attempts'] = 0


def login_user(accounts):
    """
    Handle complete user login process.
    
    Args:
        accounts (dict): Dictionary of all user accounts
        
    Returns:
        dict or None: User account data if successful, None if locked
    """
    print("\n" + "="*50)
    print("           🏧 ATM LOGIN SYSTEM 🏧")
    print("="*50)
    
    # Get and validate account number
    while True:
        account_number = get_user_input("Enter your account number: ").strip()
        
        if not validate_account_number(account_number):
            continue
            
        if account_number not in accounts:
            print("❌ Account not found. Please check your account number.")
            continue
            
        break
    
    account = accounts[account_number]
    
    # Check if account is already locked
    if account['locked']:
        print("❌ This account is locked due to multiple failed attempts.")
        print("Please contact bank support for assistance.")
        return None
    
    print(f"\n👋 Hello, {account['name']}!")
    
    # PIN validation loop
    while account['failed_attempts'] < 3:
        pin = get_user_input("Enter your 4-digit PIN: ", mask=True)
        
        if not validate_pin(pin):
            continue
            
        if authenticate_user(account, pin):
            reset_failed_attempts(account)
            print("✅ Login successful!")
            time.sleep(1)
            return account
        else:
            if handle_failed_attempt(account):
                return None
    
    return None