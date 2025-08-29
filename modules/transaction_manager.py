"""
Transaction Manager Module
Handles transaction recording, history management, and mini statement generation.
"""

from datetime import datetime


def add_transaction(account, transaction_type, amount, balance_after):
    """
    Add a new transaction to the account's transaction history.
    
    Args:
        account (dict): User account data
        transaction_type (str): Type of transaction (Deposit, Withdrawal, PIN Change)
        amount (float): Transaction amount
        balance_after (float): Account balance after transaction
    """
    transaction = {
        'date': datetime.now(),
        'type': transaction_type,
        'amount': amount,
        'balance_after': balance_after
    }
    
    # Initialize transaction history if it doesn't exist
    if 'transaction_history' not in account:
        account['transaction_history'] = []
    
    # Add transaction to history
    account['transaction_history'].append(transaction)
    
    # Keep only the last 10 transactions (more than mini statement needs)
    if len(account['transaction_history']) > 10:
        account['transaction_history'] = account['transaction_history'][-10:]


def get_mini_statement(account):
    """
    Get the last 5 transactions for mini statement.
    
    Args:
        account (dict): User account data
        
    Returns:
        list: List of last 5 transactions, most recent first
    """
    if 'transaction_history' not in account:
        return []
    
    # Return last 5 transactions, most recent first
    return account['transaction_history'][-5:][::-1]


def get_transaction_summary(account, days=30):
    """
    Get transaction summary for specified number of days.
    
    Args:
        account (dict): User account data
        days (int): Number of days to look back
        
    Returns:
        dict: Transaction summary with counts and totals
    """
    if 'transaction_history' not in account:
        return {
            'total_transactions': 0,
            'total_deposits': 0,
            'total_withdrawals': 0,
            'deposit_count': 0,
            'withdrawal_count': 0
        }
    
    # Calculate cutoff date
    cutoff_date = datetime.now().replace(day=datetime.now().day - days) if days < datetime.now().day else datetime.now().replace(month=datetime.now().month - 1)
    
    summary = {
        'total_transactions': 0,
        'total_deposits': 0,
        'total_withdrawals': 0,
        'deposit_count': 0,
        'withdrawal_count': 0
    }
    
    for transaction in account['transaction_history']:
        if transaction['date'] >= cutoff_date:
            summary['total_transactions'] += 1
            
            if transaction['type'] == 'Deposit':
                summary['total_deposits'] += transaction['amount']
                summary['deposit_count'] += 1
            elif transaction['type'] == 'Withdrawal':
                summary['total_withdrawals'] += transaction['amount']
                summary['withdrawal_count'] += 1
    
    return summary


def format_transaction_for_display(transaction):
    """
    Format a single transaction for display purposes.
    
    Args:
        transaction (dict): Transaction data
        
    Returns:
        str: Formatted transaction string
    """
    date_str = transaction['date'].strftime("%Y-%m-%d %H:%M")
    amount_str = f"${transaction['amount']:,.2f}" if transaction['amount'] > 0 else "N/A"
    balance_str = f"${transaction['balance_after']:,.2f}"
    
    return f"{date_str} | {transaction['type']:<12} | {amount_str:<10} | Balance: {balance_str}"


def export_transaction_history(account, filename=None):
    """
    Export transaction history to a text file.
    
    Args:
        account (dict): User account data
        filename (str): Optional filename, auto-generated if None
        
    Returns:
        str: Filename of exported file
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"statement_{account['account_number']}_{timestamp}.txt"
    
    try:
        with open(filename, 'w') as file:
            file.write("="*60 + "\n")
            file.write("              TRANSACTION HISTORY EXPORT\n")
            file.write("="*60 + "\n")
            file.write(f"Account Holder: {account['name']}\n")
            file.write(f"Account Number: {account['account_number']}\n")
            file.write(f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Current Balance: ${account['balance']:,.2f}\n")
            file.write("="*60 + "\n\n")
            
            if 'transaction_history' not in account or not account['transaction_history']:
                file.write("No transactions found.\n")
            else:
                file.write(f"{'Date/Time':<20} {'Type':<12} {'Amount':<12} {'Balance':<12}\n")
                file.write("-" * 60 + "\n")
                
                for transaction in reversed(account['transaction_history']):
                    date_str = transaction['date'].strftime("%Y-%m-%d %H:%M:%S")
                    amount_str = f"${transaction['amount']:,.2f}" if transaction['amount'] > 0 else "-"
                    balance_str = f"${transaction['balance_after']:,.2f}"
                    file.write(f"{date_str:<20} {transaction['type']:<12} {amount_str:<12} {balance_str:<12}\n")
            
            file.write("\n" + "="*60 + "\n")
            file.write("End of Statement\n")
            file.write("="*60 + "\n")
        
        return filename
    
    except Exception as e:
        print(f"Error exporting transaction history: {e}")
        return None


def clear_transaction_history(account):
    """
    Clear all transaction history for an account (admin function).
    
    Args:
        account (dict): User account data
    """
    if 'transaction_history' in account:
        account['transaction_history'] = []


def get_last_transaction(account):
    """
    Get the most recent transaction for an account.
    
    Args:
        account (dict): User account data
        
    Returns:
        dict or None: Last transaction or None if no transactions
    """
    if 'transaction_history' not in account or not account['transaction_history']:
        return None
    
    return account['transaction_history'][-1]