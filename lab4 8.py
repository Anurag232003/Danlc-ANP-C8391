# Initialize an empty list to store the numbers
numbers = []

# Input 10 numbers from the user
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Find the minimum and maximum numbers
min_number = min(numbers)
max_number = max(numbers)

# Print the minimum and maximum numbers
print("The minimum number is:", min_number)
print("The maximum number is:", max_number)
