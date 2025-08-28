import hashlib
import msvcrt  


accounts = []


def getpass_masked(prompt="Password: "):
    print(prompt, end="", flush=True)
    buf = b""
    while True:
        ch = msvcrt.getch()
        if ch in {b"\r", b"\n"}:  
            print("")  
            break
        elif ch == b"\x08": 
            if len(buf) > 0:
                buf = buf[:-1]
                print("\b \b", end="", flush=True)
        elif ch == b"\x03":  
            raise KeyboardInterrupt
        else:
            buf += ch
            print("*", end="", flush=True)
    return buf.decode("utf-8")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_account():
    username = input("Enter a username: ")
    

    while True:
        password = getpass_masked("Create a password: ")
        confirm = getpass_masked("Confirm your password: ")
        if password == confirm:
            break
        else:
            print("❌ Passwords do not match. Try again.")

    try:
        balance = float(input("Enter your initial balance: "))
    except ValueError:
        print("Invalid input. Balance set to 0.")
        balance = 0.0

    account = {
        "user_name": username,
        "password": hash_password(password),
        "balance": balance
    }
    print("✅ Account created successfully!\n")
    return account


def add_income(account):
    try:
        income = float(input("Enter your income: "))
        if income > 0:
            account["balance"] += income
            print(f"💰 Income added. New balance: {account['balance']}\n")
        else:
            print("Income must be positive.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Add expense
def add_expense(account):
    try:
        expense = float(input("Enter your expense: "))
        if expense <= 0:
            print("Expense must be positive.")
        elif expense <= account["balance"]:
            account["balance"] -= expense
            print(f"💸 Expense recorded. New balance: {account['balance']}\n")
        else:
            print("❌ Not enough balance!")
    except ValueError:
        print("Invalid input. Please enter a number.")


def check_balance(account):
    print(f"Your balance is: {account['balance']}\n")


def login_user():
    username = input("Enter your username: ")
    password = getpass_masked("Enter password: ")

    for account in accounts:
        if username == account["user_name"] and hash_password(password) == account["password"]:
            print(f"\n🔓 Welcome, {username}!\n")
            choice2 = 0
            while choice2 != 4:
                print("--- Account Menu ---")
                print("1. Add income")
                print("2. Add expense")
                print("3. Check balance")
                print("4. Logout")
                try:
                    choice2 = int(input("Choose an option: "))
                    if choice2 == 1:
                        add_income(account)
                    elif choice2 == 2:
                        add_expense(account)
                    elif choice2 == 3:
                        check_balance(account)
                    elif choice2 == 4:
                        print("🔒 Logged out successfully.\n")
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Please enter a number (1-4).")
            return
    print("❌ Invalid username or password.\n")


def main():
    choice = 0
    while choice != 3:
        print("--- Main Menu ---")
        print("1. Login")
        print("2. Create account")
        print("3. Exit")
        try:
            choice = int(input("Choose from above options: "))
            if choice == 1:
                login_user()
            elif choice == 2:
                accounts.append(create_account())
            elif choice == 3:
                print("👋 Good-bye!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number (1-3).")


if __name__ == "__main__":
    main()
