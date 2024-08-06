def get_largest_and_smallest(numbers):
    if not numbers:  # Check if the list is empty
        return None, None

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest

# Example usage
numbers = [3, 5, 7, 2, 8, -1, 4, 10, 12]
largest, smallest = get_largest_and_smallest(numbers)
print("The largest number is:", largest)
print("The smallest number is:", smallest)
