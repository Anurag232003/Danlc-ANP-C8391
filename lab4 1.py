# Number of elements to print
n = 10

# Initialize the counter
i = 1

# Print the prefix 'A'
print("A", end="      ")

# Use a while loop to print the first 10 elements in the pattern
while i <= n:
    print(i ** 3, end=" ")
    i += 1

# Add a newline at the end for better formatting
print()
