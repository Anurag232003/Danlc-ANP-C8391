def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is {result}.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

number1 = 10
number2 = 0

divide_numbers(number1, number2)

