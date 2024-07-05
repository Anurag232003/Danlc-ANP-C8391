import getpass

# Sample data for user credentials and balances
users = {
    'user1': {'password': 'pass123', 'balance': 1000},
    'user2': {'password': 'pass456', 'balance': 2000}
}

# Function to validate login
def validate_login(username, password):
    if username in users and users[username]['password'] == password:
        return True
    return False

# Function to change password
def change_password(username):
    new_password = getpass.getpass("Enter new password: ")
    users[username]['password'] = new_password
    print("Password changed successfully!")

# Function to check balance
def check_balance(username):
    print(f"Your current balance is: ${users[username]['balance']}")

# Function to deposit amount
def deposit_amount(username):
    amount = float(input("Enter amount to deposit: "))
    users[username]['balance'] += amount
    print(f"${amount} deposited successfully!")
    check_balance(username)

# Function to withdraw amount
def withdraw_amount(username):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= users[username]['balance']:
        users[username]['balance'] -= amount
        print(f"${amount} withdrawn successfully!")
    else:
        print("Insufficient balance!")
    check_balance(username)

# Main function to handle user interaction
def main():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if validate_login(username, password):
        print("Login successful!")
        while True:
            print("\nChoose an option:")
            print("1. Change password")
            print("2. Check balance")
            print("3. Deposit amount")
            print("4. Withdraw amount")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                change_password(username)
            elif choice == '2':
                check_balance(username)
            elif choice == '3':
                deposit_amount(username)
            elif choice == '4':
                withdraw_amount(username)
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")
    else:
        print("Invalid username or password.")

# Run the main function
if __name__ == "__main__":
    main()

