def check_login(username, password):
    # Hardcoding the correct username and password for demonstration
    correct_username = "user123"
    correct_password = "password123"

    if username == correct_username and password == correct_password:
        print("Login successful!")
    else:
        print("Login failed. Incorrect username or password.")

# Example usage:
username = input("Enter username: ")
password = input("Enter password: ")

check_login(username, password)

