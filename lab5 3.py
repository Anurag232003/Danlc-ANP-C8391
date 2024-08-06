def print_multiplication_table(number, range_limit):
    """Print the multiplication table for a given number up to a given range limit."""
    for i in range(1, range_limit + 1):
        print(f"{number} x {i} = {number * i}")

def print_multiplication_tables(start, end, range_limit):
    """Print multiplication tables for all numbers in the given range up to a given range limit."""
    for num in range(start, end + 1):
        print(f"\nMultiplication table for {num}:")
        print_multiplication_table(num, range_limit)

# Input range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
range_limit = int(input("Enter the range limit for the tables: "))

# Print multiplication tables
print_multiplication_tables(start, end, range_limit)
