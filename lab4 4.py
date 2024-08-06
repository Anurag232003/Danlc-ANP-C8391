# Input number N
N = 6

# Initialize the factorial result
factorial = 1

# Use a while loop to calculate the factorial
i = N
while i > 0:
    factorial *= i
    i -= 1

# Print the result
print(f"The factorial of {N} is: {factorial}")
