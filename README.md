# Expense Tracker

Expense Tracker is a simple command-line Python application for managing personal finances. It allows users to create accounts, securely log in, add income, record expenses, and check their balance. Passwords are masked during entry and securely hashed for storage.

## Features

- **Account Creation:** Create an account with a username, password, and initial balance.
- **Secure Login:** Passwords are masked during input and stored as SHA-256 hashes.
- **Income Tracking:** Add income to your account balance.
- **Expense Recording:** Record expenses and update your balance.
- **Balance Inquiry:** Check your current account balance.
- **User-Friendly Menus:** Simple text-based menus for navigation.

## Requirements

- Python 3.x
- Windows OS (uses `msvcrt` for password masking)

## How to Run

1. **Clone or Download the Repository**

   Download the `ExpenseTracker.py` file to your computer.

2. **Open a Command Prompt**

   Navigate to the directory containing `ExpenseTracker.py`.

3. **Run the Application**

   ```sh
   python ExpenseTracker.py
   ```

## Usage

### Main Menu

- **1. Login:** Log in to an existing account.
- **2. Create account:** Create a new account.
- **3. Exit:** Exit the application.

### Account Menu (after login)

- **1. Add income:** Add money to your account.
- **2. Add expense:** Record an expense.
- **3. Check balance:** View your current balance.
- **4. Logout:** Log out of your account.

### Password Security

- Passwords are entered in masked mode (characters are replaced by `*`).
- Passwords are stored as SHA-256 hashes for security.

## Example

```
--- Main Menu ---
1. Login
2. Create account
3. Exit
Choose from above options: 2
Enter a username: alice
Create a password: ******
Confirm your password: ******
Enter your initial balance: 1000
✅ Account created successfully!

--- Main Menu ---
1. Login
2. Create account
3. Exit
Choose from above options: 1
Enter your username: alice
Enter password: ******
🔓 Welcome, alice!

--- Account Menu ---
1. Add income
2. Add expense
3. Check balance
4. Logout
Choose an option: 3
Your balance is: 1000.0
```

## Notes

- All account data is stored in memory and will be lost when the program exits.
- Only works on Windows due to the use of `msvcrt` for password masking.

## License

This project is for educational purposes.