"""
Database Module
Handles data storage and initialization for user accounts.
Simulates a database with in-memory storage for the ATM system.
"""

from datetime import datetime, timedelta
import json
import os


def initialize_sample_data():
    """
    Initialize sample account data for testing the ATM system.
    
    Returns:
        dict: Dictionary containing sample user accounts
    """
    # Sample accounts with different scenarios
    accounts = {
        '123456789': {
            'account_number': '123456789',
            'name': 'John Smith',
            'pin': '1234',
            'balance': 1500.00,
            'failed_attempts': 0,
            'locked': False,
            'transaction_history': [
                {
                    'date': datetime.now() - timedelta(days=5),
                    'type': 'Deposit',
                    'amount': 500.00,
                    'balance_after': 1000.00
                },
                {
                    'date': datetime.now() - timedelta(days=3),
                    'type': 'Withdrawal',
                    'amount': 200.00,
                    'balance_after': 800.00
                },
                {
                    'date': datetime.now() - timedelta(days=1),
                    'type': 'Deposit',
                    'amount': 700.00,
                    'balance_after': 1500.00
                }
            ]
        },
        '987654321': {
            'account_number': '987654321',
            'name': 'Jane Doe',
            'pin': '5678',
            'balance': 2750.50,
            'failed_attempts': 0,
            'locked': False,
            'transaction_history': [
                {
                    'date': datetime.now() - timedelta(days=7),
                    'type': 'Deposit',
                    'amount': 1000.00,
                    'balance_after': 2000.00
                },
                {
                    'date': datetime.now() - timedelta(days=4),
                    'type': 'Withdrawal',
                    'amount': 250.00,
                    'balance_after': 1750.00
                },
                {
                    'date': datetime.now() - timedelta(days=2),
                    'type': 'Deposit',
                    'amount': 1000.50,
                    'balance_after': 2750.50
                }
            ]
        },
        '555666777': {
            'account_number': '555666777',
            'name': 'Bob Johnson',
            'pin': '9999',
            'balance': 50.00,
            'failed_attempts': 0,
            'locked': False,
            'transaction_history': [
                {
                    'date': datetime.now() - timedelta(days=10),
                    'type': 'Deposit',
                    'amount': 100.00,
                    'balance_after': 100.00
                },
                {
                    'date': datetime.now() - timedelta(days=6),
                    'type': 'Withdrawal',
                    'amount': 50.00,
                    'balance_after': 50.00
                }
            ]
        },
        '111222333': {
            'account_number': '111222333',
            'name': 'Alice Brown',
            'pin': '0000',
            'balance': 5000.00,
            'failed_attempts': 2,  # Account with failed attempts
            'locked': False,
            'transaction_history': []
        },
        '444555666': {
            'account_number': '444555666',
            'name': 'Charlie Wilson',
            'pin': '1111',
            'balance': 750.25,
            'failed_attempts': 3,
            'locked': True,  # Locked account for testing
            'transaction_history': []
        }
    }
    
    return accounts


def save_account_data(accounts, filename='accounts.json'):
    """
    Save account data to a JSON file.
    
    Args:
        accounts (dict): Dictionary of user accounts
        filename (str): Name of the file to save to
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Convert datetime objects to strings for JSON serialization
        accounts_copy = {}
        for acc_num, account in accounts.items():
            accounts_copy[acc_num] = account.copy()
            
            if 'transaction_history' in accounts_copy[acc_num]:
                for transaction in accounts_copy[acc_num]['transaction_history']:
                    if isinstance(transaction['date'], datetime):
                        transaction['date'] = transaction['date'].isoformat()
        
        with open(filename, 'w') as file:
            json.dump(accounts_copy, file, indent=4)
        
        return True
    
    except Exception as e:
        print(f"Error saving account data: {e}")
        return False


def load_account_data(filename='accounts.json'):
    """
    Load account data from a JSON file.
    
    Args:
        filename (str): Name of the file to load from
        
    Returns:
        dict: Dictionary of user accounts, or None if file doesn't exist
    """
    try:
        if not os.path.exists(filename):
            return None
        
        with open(filename, 'r') as file:
            accounts = json.load(file)
        
        # Convert date strings back to datetime objects
        for account in accounts.values():
            if 'transaction_history' in account:
                for transaction in account['transaction_history']:
                    if isinstance(transaction['date'], str):
                        transaction['date'] = datetime.fromisoformat(transaction['date'])
        
        return accounts
    
    except Exception as e:
        print(f"Error loading account data: {e}")
        return None


def create_new_account(account_number, name, pin, initial_balance=0.00):
    """
    Create a new user account.
    
    Args:
        account_number (str): Unique account number
        name (str): Account holder's name
        pin (str): 4-digit PIN
        initial_balance (float): Starting balance
        
    Returns:
        dict: New account data
    """
    return {
        'account_number': account_number,
        'name': name,
        'pin': pin,
        'balance': initial_balance,
        'failed_attempts': 0,
        'locked': False,
        'transaction_history': []
    }


def get_account(accounts, account_number):
    """
    Retrieve account data by account number.
    
    Args:
        accounts (dict): Dictionary of all accounts
        account_number (str): Account number to search for
        
    Returns:
        dict or None: Account data if found, None otherwise
    """
    return accounts.get(account_number)


def account_exists(accounts, account_number):
    """
    Check if an account exists.
    
    Args:
        accounts (dict): Dictionary of all accounts
        account_number (str): Account number to check
        
    Returns:
        bool: True if account exists, False otherwise
    """
    return account_number in accounts


def update_account(accounts, account_number, updated_data):
    """
    Update account data.
    
    Args:
        accounts (dict): Dictionary of all accounts
        account_number (str): Account number to update
        updated_data (dict): Updated account data
        
    Returns:
        bool: True if successful, False if account not found
    """
    if account_number in accounts:
        accounts[account_number].update(updated_data)
        return True
    return False


def delete_account(accounts, account_number):
    """
    Delete an account (admin function).
    
    Args:
        accounts (dict): Dictionary of all accounts
        account_number (str): Account number to delete
        
    Returns:
        bool: True if successful, False if account not found
    """
    if account_number in accounts:
        del accounts[account_number]
        return True
    return False


def get_all_accounts(accounts):
    """
    Get all account numbers and names (admin function).
    
    Args:
        accounts (dict): Dictionary of all accounts
        
    Returns:
        list: List of tuples (account_number, name)
    """
    return [(acc_num, acc['name']) for acc_num, acc in accounts.items()]


def backup_accounts(accounts, backup_filename=None):
    """
    Create a backup of all account data.
    
    Args:
        accounts (dict): Dictionary of all accounts
        backup_filename (str): Optional backup filename
        
    Returns:
        str or None: Backup filename if successful, None otherwise
    """
    if backup_filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"accounts_backup_{timestamp}.json"
    
    return backup_filename if save_account_data(accounts, backup_filename) else None