def is_armstrong(number):
    """Check if a number is an Armstrong number."""
    num_str = str(number)
    num_length = len(num_str)
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    return sum_of_powers == number

def find_armstrong_numbers(start, end):
    """Find all Armstrong numbers in a given range."""
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Input range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Find and print Armstrong numbers
armstrong_numbers = find_armstrong_numbers(start, end)
print(f"Armstrong numbers between {start} and {end} are: {armstrong_numbers}")
