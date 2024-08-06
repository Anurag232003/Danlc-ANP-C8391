# Number of inputs
n = 10

# Initialize the sum
sum_numbers = 0

# Prompt user to input 10 numbers and calculate the sum
print("Enter 10 numbers:")

# Use a while loop to read the numbers from the user
i = 1
while i <= n:
    number = float(input(f"Enter number {i}: "))
    sum_numbers += number
    i += 1

# Calculate the average
average = sum_numbers / n

# Print the result
print("The sum of the 10 numbers is:", sum_numbers)
print("The average of the 10 numbers is:", average)
