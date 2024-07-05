def check_number(n):
    if n > 0:
        print(f"{n} is a positive number.")
    elif n < 0:
        print(f"{n} is a negative number.")
    else:
        print("The number is zero.")

# Example usage:
num = float(input("Enter a number: "))  # Taking input from user
check_number(num)
