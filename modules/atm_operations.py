"""
ATM Operations Module
Handles all ATM operations including balance inquiry, deposits, withdrawals,
PIN changes, and transaction history.
"""

from datetime import datetime
from modules.validation import validate_amount, validate_pin
from modules.user_interface import get_user_input
from modules.transaction_manager import add_transaction, get_mini_statement


class ATMOperations:
    """
    Class to handle all ATM operations for a specific user account.
    """
    
    def __init__(self, account):
        """
        Initialize ATM operations for a specific account.
        
        Args:
            account (dict): User account data
        """
        self.account = account
        
    def view_balance(self):
        """
        Display current account balance.
        """
        print("\n" + "="*40)
        print("         💰 BALANCE INQUIRY 💰")
        print("="*40)
        print(f"Account Holder: {self.account['name']}")
        print(f"Current Balance: ${self.account['balance']:,.2f}")
        print("="*40)
        
    def deposit_money(self):
        """
        Handle money deposit operation.
        """
        print("\n" + "="*40)
        print("          💵 DEPOSIT MONEY 💵")
        print("="*40)
        
        while True:
            amount_str = get_user_input("Enter deposit amount: $")
            
            if not validate_amount(amount_str):
                continue
                
            amount = float(amount_str)
            
            if amount <= 0:
                print("❌ Deposit amount must be greater than zero.")
                continue
                
            # Process deposit
            old_balance = self.account['balance']
            self.account['balance'] += amount
            
            # Record transaction
            add_transaction(
                self.account,
                transaction_type="Deposit",
                amount=amount,
                balance_after=self.account['balance']
            )
            
            print(f"\n✅ Deposit successful!")
            print(f"Amount Deposited: ${amount:,.2f}")
            print(f"Previous Balance: ${old_balance:,.2f}")
            print(f"Current Balance: ${self.account['balance']:,.2f}")
            break
            
    def withdraw_money(self):
        """
        Handle money withdrawal operation.
        """
        print("\n" + "="*40)
        print("          💸 WITHDRAW MONEY 💸")
        print("="*40)
        print(f"Available Balance: ${self.account['balance']:,.2f}")
        
        while True:
            amount_str = get_user_input("Enter withdrawal amount: $")
            
            if not validate_amount(amount_str):
                continue
                
            amount = float(amount_str)
            
            if amount <= 0:
                print("❌ Withdrawal amount must be greater than zero.")
                continue
                
            if amount > self.account['balance']:
                print(f"❌ Insufficient funds. Available balance: ${self.account['balance']:,.2f}")
                continue
                
            # Process withdrawal
            old_balance = self.account['balance']
            self.account['balance'] -= amount
            
            # Record transaction
            add_transaction(
                self.account,
                transaction_type="Withdrawal",
                amount=amount,
                balance_after=self.account['balance']
            )
            
            print(f"\n✅ Withdrawal successful!")
            print(f"Amount Withdrawn: ${amount:,.2f}")
            print(f"Previous Balance: ${old_balance:,.2f}")
            print(f"Current Balance: ${self.account['balance']:,.2f}")
            break
            
    def change_pin(self):
        """
        Handle PIN change operation.
        """
        print("\n" + "="*40)
        print("           🔐 CHANGE PIN 🔐")
        print("="*40)
        
        # Verify current PIN
        current_pin = get_user_input("Enter current PIN: ", mask=True)
        
        if not validate_pin(current_pin):
            return
            
        if current_pin != self.account['pin']:
            print("❌ Current PIN is incorrect.")
            return
            
        # Get new PIN
        while True:
            new_pin = get_user_input("Enter new 4-digit PIN: ", mask=True)
            
            if not validate_pin(new_pin):
                continue
                
            if new_pin == self.account['pin']:
                print("❌ New PIN cannot be the same as current PIN.")
                continue
                
            # Confirm new PIN
            confirm_pin = get_user_input("Confirm new PIN: ", mask=True)
            
            if new_pin != confirm_pin:
                print("❌ PINs do not match. Please try again.")
                continue
                
            # Update PIN
            self.account['pin'] = new_pin
            
            # Record transaction
            add_transaction(
                self.account,
                transaction_type="PIN Change",
                amount=0,
                balance_after=self.account['balance']
            )
            
            print("✅ PIN changed successfully!")
            break
            
    def mini_statement(self):
        """
        Display mini statement with last 5 transactions.
        """
        print("\n" + "="*60)
        print("                📄 MINI STATEMENT 📄")
        print("="*60)
        print(f"Account Holder: {self.account['name']}")
        print(f"Account Number: {self.account['account_number']}")
        print(f"Current Balance: ${self.account['balance']:,.2f}")
        print("-" * 60)
        
        statement = get_mini_statement(self.account)
        
        if not statement:
            print("No recent transactions found.")
        else:
            print(f"{'Date/Time':<20} {'Type':<12} {'Amount':<12} {'Balance':<12}")
            print("-" * 60)
            for transaction in statement:
                date_str = transaction['date'].strftime("%Y-%m-%d %H:%M:%S")
                amount_str = f"${transaction['amount']:,.2f}" if transaction['amount'] > 0 else "-"
                balance_str = f"${transaction['balance_after']:,.2f}"
                print(f"{date_str:<20} {transaction['type']:<12} {amount_str:<12} {balance_str:<12}")
        
        print("="*60)
        
    def exit_program(self):
        """
        Handle program exit with thank you message.
        """
        print("\n" + "="*50)
        print("Thank you for using our ATM service!")
        print(f"Goodbye, {self.account['name']}!")
        print("Have a great day! 😊")
        print("="*50)