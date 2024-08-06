def get_two_numbers():
    try:
        num1 = input("Please enter the first number: ")
        num2 = input("Please enter the second number: ")

        num1 = float(num1)
        num2 = float(num2)

        print(f"The two numbers entered are {num1} and {num2}.")
    except ValueError:
        raise TypeError("Both inputs must be numerical.")

try:
    get_two_numbers()
except TypeError as e:
    print(f"Error: {e}")

