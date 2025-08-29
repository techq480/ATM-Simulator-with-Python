# ATM-Simulator-with-Python
🏦 Professional ATM Banking Simulator built with Python - Features secure authentication, transaction history, account management, and modular architecture following banking industry standards.
A comprehensive ATM (Automated Teller Machine) simulator built entirely in Python that replicates real-world banking operations. This educational project demonstrates advanced programming concepts including modular design, secure authentication, input validation, and transaction management.

🎯 Perfect for learning banking software development, Python programming best practices, and secure application design.

# ATM Simulator - Python Banking Application

## 📋 Overview

This ATM Simulator is a comprehensive Python application that mimics the functionality of a real banking ATM system. It provides a secure, user-friendly interface for banking operations with robust validation, transaction history, and security features.

## ✨ Features

### Core Functionality
- **Secure Login System** - Account number and PIN authentication
- **Balance Inquiry** - View current account balance
- **Money Deposit** - Add funds to account with validation
- **Money Withdrawal** - Withdraw funds with balance checks
- **PIN Change** - Secure PIN modification with verification
- **Mini Statement** - View last 5 transactions with date/time
- **Transaction History** - Complete record of all account activities

### Security Features
- **Account Locking** - Locks account after 3 incorrect PIN attempts
- **Input Validation** - Comprehensive validation for all inputs
- **PIN Masking** - Hidden PIN entry for security
- **Transaction Limits** - Daily withdrawal and deposit limits

### Technical Features
- **Modular Design** - Well-structured, maintainable code
- **Error Handling** - Robust try-catch mechanisms
- **PEP 8 Compliant** - Follows Python style guidelines
- **Comprehensive Documentation** - Clear comments and docstrings

## 📁 File Structure

```
atm_simulator/
│
├── main.py                          # Main program entry point
│
├── modules/
│   ├── __init__.py                  # Module initialization
│   ├── authentication.py           # Login and PIN validation
│   ├── atm_operations.py           # Core ATM operations
│   ├── user_interface.py           # UI components and menus
│   ├── validation.py               # Input validation functions
│   ├── transaction_manager.py      # Transaction recording/history
│   └── database.py                 # Data storage and management
│
├── README.md                       # This documentation file
├── requirements.txt                # Python dependencies
└── accounts.json                   # Account data (created at runtime)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Installation Steps

1. **Download/Clone the project files**
   ```bash
   # Create project directory
   mkdir atm_simulator
   cd atm_simulator
   ```

2. **Create the modules directory**
   ```bash
   mkdir modules
   touch modules/__init__.py
   ```

3. **Add all Python files to their respective locations**
   - Place `main.py` in the root directory
   - Place all module files in the `modules/` directory

4. **Make the main file executable (optional)**
   ```bash
   chmod +x main.py
   ```

## 🏃‍♂️ Running the Application

### Command Line Execution
```bash
python main.py
```

### Alternative Execution Methods
```bash
# If you have Python 3 specifically
python3 main.py

# Direct execution (if made executable)
./main.py
```

## 👤 Test Accounts

The application comes with pre-configured test accounts:

| Account Number | PIN  | Name          | Balance    | Status  | Notes                    |
|----------------|------|---------------|------------|---------|--------------------------|
| 123456789      | 1234 | John Smith    | $1,500.00  | Active  | Has transaction history  |
| 987654321      | 5678 | Jane Doe      | $2,750.50  | Active  | Has transaction history  |
| 555666777      | 9999 | Bob Johnson   | $50.00     | Active  | Low balance account      |
| 111222333      | 0000 | Alice Brown   | $5,000.00  | Active  | 2 failed attempts        |
| 444555666      | 1111 | Charlie Wilson| $750.25    | Locked  | Account locked (testing) |

## 🎮 Usage Instructions

### 1. Starting the Application
- Run the program using `python main.py`
- You'll see a welcome screen with system information

### 2. Logging In
- Enter your account number (6-12 digits)
- Enter your 4-digit PIN (input will be masked)
- You have 3 attempts before the account locks

### 3. Using the ATM Menu
Once logged in, you'll see the main menu:

```
🏧 ATM MAIN MENU 🏧
1. 💰 View Balance
2. 💵 Deposit Money
3. 💸 Withdraw Money
4. 🔐 Change PIN
5. 📄 Mini Statement (Last 5 Transactions)
6. 🚪 Exit
```

### 4. Performing Operations

#### View Balance (Option 1)
- Displays current account balance
- Shows account holder name
- No additional input required

#### Deposit Money (Option 2)
- Enter amount to deposit
- Amount must be positive and ≤ $5,000 (daily limit)
- Transaction is recorded with date/time

#### Withdraw Money (Option 3)
- Enter amount to withdraw
- System checks for sufficient funds
- Maximum withdrawal: $1,000 per day
- Transaction is recorded with date/time

#### Change PIN (Option 4)
- Enter current PIN for verification
- Enter new 4-digit PIN
- Confirm new PIN
- PIN change is recorded in transaction history

#### Mini Statement (Option 5)
- Shows last 5 transactions
- Displays date/time, transaction type, amount, and resulting balance
- Sorted by most recent first

#### Exit (Option 6)
- Safely exits the program
- Displays thank you message

## 🔧 Technical Details

### Input Validation Rules

#### Account Numbers
- Must be 6-12 digits long
- Only numeric characters allowed
- Cannot be empty

#### PINs
- Must be exactly 4 digits
- Only numeric characters allowed
- Cannot be empty

#### Transaction Amounts
- Must be positive numbers
- Maximum 2 decimal places
- Cannot exceed daily limits:
  - Deposits: $5,000
  - Withdrawals: $1,000
- Cannot exceed account balance (for withdrawals)

### Security Features

#### Account Locking
- Account locks after 3 consecutive failed PIN attempts
- Locked accounts cannot be accessed
- Failed attempts reset upon successful login

#### PIN Security
- PINs are masked during input
- PIN validation occurs before any operations
- PIN changes require current PIN verification

### Transaction Management

#### Transaction Types
- **Deposit**: Money added to account
- **Withdrawal**: Money removed from account
- **PIN Change**: Security update (amount = 0)

#### Transaction Storage
- Last 10 transactions stored per account
- Mini statement shows last 5 transactions
- Each transaction includes:
  - Date and time
  - Transaction type
  - Amount (if applicable)
  - Resulting account balance

## 🐛 Troubleshooting

### Common Issues

#### "Module not found" Error
```bash
# Ensure you're in the correct directory
cd atm_simulator

# Check if modules directory exists
ls -la modules/

# Verify __init__.py exists in modules directory
ls -la modules/__init__.py
```

#### Permission Denied (Unix/Linux/Mac)
```bash
# Make the file executable
chmod +x main.py

# Or run with python explicitly
python main.py
```

#### Account Locked Message
- Use a different test account
- Restart the program to reset failed attempts
- Check the test accounts table for account status

### Error Messages and Solutions

| Error Message | Cause | Solution |
|---------------|-------|----------|
| "Account not found" | Invalid account number | Use test accounts from the table above |
| "Account is locked" | 3 failed PIN attempts | Use a different account or restart program |
| "Insufficient funds" | Withdrawal > balance | Check balance first, withdraw smaller amount |
| "Daily limit exceeded" | Transaction exceeds limits | Split large transactions across multiple days |

## 🔄 Extending the Application

### Adding New Features
The modular design makes it easy to add features:

1. **New ATM Operations**: Add methods to `ATMOperations` class
2. **Additional Validation**: Extend `validation.py` module
3. **Enhanced UI**: Modify `user_interface.py` for new displays
4. **Data Persistence**: Enhance `database.py` for file/database storage

### Code Style Guidelines
- Follow PEP 8 Python style guide
- Use descriptive variable and function names
- Add docstrings to all functions and classes
- Include type hints where appropriate
- Add comprehensive error handling

## 📊 Sample Outputs

See the companion file `sample_outputs.md` for detailed examples of:
- Successful login sequences
- Failed login attempts and account locking
- All ATM operations with various scenarios
- Mini statement displays
- Error handling demonstrations

## 🤝 Support

For technical support or questions:
1. Check the troubleshooting section above
2. Review the sample outputs for expected behavior
3. Verify your Python installation and version
4. Ensure all module files are in the correct directory structure

## 📄 License

MIT License

Copyright (c) 2025 ATM Simulator Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---

**Last Updated**: August 2025
**Version**: 1.0.0
