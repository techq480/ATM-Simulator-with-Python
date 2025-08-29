"""
GUI Interface Module
Handles all user interface elements using Tkinter for graphical interface.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import getpass

class ATMInterface:
    def __init__(self, root, accounts):
        """
        Initialize the ATM GUI interface.
        
        Args:
            root: Tkinter root window
            accounts (dict): Dictionary of all user accounts
        """
        self.root = root
        self.root.title("ATM Simulator")
        self.root.geometry("600x500")
        self.setup_styles()
        
        # Main container
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Current screen tracking
        self.current_screen = None
        self.accounts = accounts
        self.current_account = None
        self.atm = None
        
    def setup_styles(self):
        """Configure custom styles for widgets."""
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=10)
        style.configure('TLabel', font=('Arial', 12))
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        
    def display_login(self):
        """Display login screen."""
        self.clear_screen()
        
        title = ttk.Label(self.main_frame, text="🏧 ATM LOGIN 🏧",
                         style='Title.TLabel')
        title.pack(pady=20)
        
        # Account number entry
        ttk.Label(self.main_frame, text="Account Number:").pack()
        self.account_entry = ttk.Entry(self.main_frame)
        self.account_entry.pack(pady=5)
        
        # PIN entry
        ttk.Label(self.main_frame, text="PIN:").pack()
        self.pin_entry = ttk.Entry(self.main_frame, show="*")
        self.pin_entry.pack(pady=5)
        
        # Login button
        login_btn = ttk.Button(self.main_frame, text="Login",
                             command=self.handle_login)
        login_btn.pack(pady=20)
        
    def handle_login(self):
        """Handle login attempt."""
        account_number = self.account_entry.get().strip()
        pin = self.pin_entry.get()
        
        if not account_number or not pin:
            self.display_error("Please enter both account number and PIN")
            return
            
        if account_number not in self.accounts:
            self.display_error("Account not found")
            return
            
        account = self.accounts[account_number]
        
        if account['locked']:
            self.display_error("Account locked. Please contact support.")
            return
            
        if account['pin'] != pin:
            account['failed_attempts'] += 1
            if account['failed_attempts'] >= 3:
                account['locked'] = True
                self.display_error("Account locked due to multiple failed attempts")
            else:
                remaining = 3 - account['failed_attempts']
                self.display_error(f"Incorrect PIN. {remaining} attempts remaining")
            return
            
        # Successful login
        account['failed_attempts'] = 0
        self.current_account = account
        from modules.atm_operations import ATMOperations
        self.atm = ATMOperations(account)
        self.display_menu()

    def display_welcome(self):
        """Display welcome screen."""
        self.clear_screen()
        
        title = ttk.Label(self.main_frame, text="🏦 WELCOME TO ATM 🏦", 
                         style='Title.TLabel')
        title.pack(pady=20)
        
        info = ttk.Label(self.main_frame, 
                        text="Secure Banking System\n\n"
                             "📍 Location: Main Branch ATM\n"
                             "🕒 Available 24/7\n"
                             "🔒 Secure & Encrypted")
        info.pack(pady=20)
        
        start_btn = ttk.Button(self.main_frame, text="Start", 
                              command=self.display_login)
        start_btn.pack(pady=20)
        
    def display_menu(self):
        """Display main ATM menu options."""
        self.clear_screen()
        
        title = ttk.Label(self.main_frame, text="🏧 ATM MAIN MENU 🏧", 
                         style='Title.TLabel')
        title.pack(pady=20)
        
        # Menu buttons
        menu_options = [
            ("💰 View Balance", self.view_balance),
            ("💵 Deposit Money", self.deposit_money),
            ("💸 Withdraw Money", self.withdraw_money),
            ("🔐 Change PIN", self.change_pin),
            ("📄 Mini Statement", self.mini_statement),
            ("🚪 Exit", self.exit_atm)
        ]
        
        for text, command in menu_options:
            btn = ttk.Button(self.main_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=5)
            
    def clear_screen(self):
        """Clear all widgets from the main frame."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def view_balance(self):
        """Display current account balance."""
        self.clear_screen()
        
        title = ttk.Label(self.main_frame, text="💰 BALANCE INQUIRY 💰", 
                         style='Title.TLabel')
        title.pack(pady=20)
        
        account = self.atm.account
        info = ttk.Label(self.main_frame, 
                        text=f"Account Holder: {account['name']}\n"
                             f"Current Balance: ${account['balance']:,.2f}")
        info.pack(pady=20)
        
        back_btn = ttk.Button(self.main_frame, text="Back to Menu",
                            command=self.display_menu)
        back_btn.pack(pady=20, padx=20, fill=tk.X)
        
    def deposit_money(self):
        """Handle money deposit operation."""
        self.clear_screen()
        
        title = ttk.Label(self.main_frame, text="💵 DEPOSIT MONEY 💵", 
                         style='Title.TLabel')
        title.pack(pady=20)
        
        amount = self.get_user_input("Enter deposit amount: $")
        if not amount:
            return
            
        try:
            amount = float(amount)
            if amount <= 0:
                self.display_error("Deposit amount must be greater than zero.")
                return
                
            # Process deposit
            old_balance = self.atm.account['balance']
            self.atm.account['balance'] += amount
            
            # Record transaction
            from modules.transaction_manager import add_transaction
            add_transaction(
                self.atm.account,
                transaction_type="Deposit",
                amount=amount,
                balance_after=self.atm.account['balance']
            )
            
            self.display_success(
                f"Deposit successful!\n\n"
                f"Amount Deposited: ${amount:,.2f}\n"
                f"Previous Balance: ${old_balance:,.2f}\n"
                f"Current Balance: ${self.atm.account['balance']:,.2f}"
            )
            self.display_menu()
            
        except ValueError:
            self.display_error("Invalid amount entered.")
            
    def withdraw_money(self):
        """Handle money withdrawal operation."""
        self.clear_screen()
        
        title = ttk.Label(self.main_frame, text="💸 WITHDRAW MONEY 💸", 
                         style='Title.TLabel')
        title.pack(pady=20)
        
        balance = ttk.Label(self.main_frame, 
                          text=f"Available Balance: ${self.atm.account['balance']:,.2f}")
        balance.pack(pady=10)
        
        amount = self.get_user_input("Enter withdrawal amount: $")
        if not amount:
            return
            
        try:
            amount = float(amount)
            if amount <= 0:
                self.display_error("Withdrawal amount must be greater than zero.")
                return
                
            if amount > self.atm.account['balance']:
                self.display_error(
                    f"Insufficient funds. Available balance: ${self.atm.account['balance']:,.2f}")
                return
                
            # Process withdrawal
            old_balance = self.atm.account['balance']
            self.atm.account['balance'] -= amount
            
            # Record transaction
            from modules.transaction_manager import add_transaction
            add_transaction(
                self.atm.account,
                transaction_type="Withdrawal",
                amount=amount,
                balance_after=self.atm.account['balance']
            )
            
            self.display_success(
                f"Withdrawal successful!\n\n"
                f"Amount Withdrawn: ${amount:,.2f}\n"
                f"Previous Balance: ${old_balance:,.2f}\n"
                f"Current Balance: ${self.atm.account['balance']:,.2f}"
            )
            self.display_menu()
            
        except ValueError:
            self.display_error("Invalid amount entered.")
            
    def change_pin(self):
        """Handle PIN change operation."""
        self.clear_screen()
        
        title = ttk.Label(self.main_frame, text="🔐 CHANGE PIN 🔐", 
                         style='Title.TLabel')
        title.pack(pady=20)
        
        # Verify current PIN
        current_pin = self.get_user_input("Enter current PIN: ", mask=True)
        if not current_pin:
            return
            
        if current_pin != self.atm.account['pin']:
            self.display_error("Current PIN is incorrect.")
            return
            
        # Get new PIN
        new_pin = self.get_user_input("Enter new 4-digit PIN: ", mask=True)
        if not new_pin:
            return
            
        if new_pin == self.atm.account['pin']:
            self.display_error("New PIN cannot be the same as current PIN.")
            return
            
        # Confirm new PIN
        confirm_pin = self.get_user_input("Confirm new PIN: ", mask=True)
        if not confirm_pin:
            return
            
        if new_pin != confirm_pin:
            self.display_error("PINs do not match. Please try again.")
            return
            
        # Update PIN
        self.atm.account['pin'] = new_pin
        
        # Record transaction
        from modules.transaction_manager import add_transaction
        add_transaction(
            self.atm.account,
            transaction_type="PIN Change",
            amount=0,
            balance_after=self.atm.account['balance']
        )
        
        self.display_success("PIN changed successfully!")
        self.display_menu()
        
    def mini_statement(self):
        """Display mini statement with last 5 transactions."""
        self.clear_screen()
        
        title = ttk.Label(self.main_frame, text="📄 MINI STATEMENT 📄", 
                         style='Title.TLabel')
        title.pack(pady=20)
        
        account = self.atm.account
        info = ttk.Label(self.main_frame, 
                        text=f"Account Holder: {account['name']}\n"
                             f"Account Number: {account['account_number']}\n"
                             f"Current Balance: ${account['balance']:,.2f}")
        info.pack(pady=10)
        
        from modules.transaction_manager import get_mini_statement
        statement = get_mini_statement(account)
        
        if not statement:
            ttk.Label(self.main_frame, text="No recent transactions found.").pack()
        else:
            # Create a frame for the statement table
            table_frame = ttk.Frame(self.main_frame)
            table_frame.pack(fill=tk.BOTH, expand=True, pady=10)
            
            # Create a treeview widget for the statement
            tree = ttk.Treeview(table_frame, columns=('Date', 'Type', 'Amount', 'Balance'), show='headings')
            tree.heading('Date', text='Date/Time')
            tree.heading('Type', text='Type')
            tree.heading('Amount', text='Amount')
            tree.heading('Balance', text='Balance')
            
            # Add transactions to the treeview
            for transaction in statement:
                date_str = transaction['date'].strftime("%Y-%m-%d %H:%M")
                amount_str = f"${transaction['amount']:,.2f}" if transaction['amount'] > 0 else "-"
                balance_str = f"${transaction['balance_after']:,.2f}"
                tree.insert('', tk.END, values=(date_str, transaction['type'], amount_str, balance_str))
            
            tree.pack(fill=tk.BOTH, expand=True)
        
        back_btn = ttk.Button(self.main_frame, text="Back to Menu",
                            command=self.display_menu)
        back_btn.pack(pady=20, padx=20, fill=tk.X)
        
    def exit_atm(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()
    
    def display_error(self, message):
        """Display error message."""
        messagebox.showerror("Error", message)
        
    def display_success(self, message):
        """Display success message."""
        messagebox.showinfo("Success", message)
        
    def display_info(self, message):
        """Display information message."""
        messagebox.showinfo("Information", message)
        
    def display_warning(self, message):
        """Display warning message."""
        messagebox.showwarning("Warning", message)
        
    def get_user_input(self, prompt, mask=False):
        """Get user input with optional masking."""
        if mask:
            return simpledialog.askstring("Input", prompt, show='*')
        return simpledialog.askstring("Input", prompt)
        
    def confirm_action(self, message):
        """Ask user for confirmation."""
        return messagebox.askyesno("Confirm", message)
        
    def pause_for_user(self):
        """Pause execution until user continues."""
        messagebox.showinfo("Continue", "Click OK to continue")

def run_gui(accounts):
    """Run the ATM GUI application."""
    root = tk.Tk()
    app = ATMInterface(root, accounts)
    app.display_welcome()
    root.mainloop()
