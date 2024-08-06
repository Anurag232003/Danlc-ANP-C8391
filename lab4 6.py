def decimal_to_binary(n):
    # Array to store binary digits
    binary_digits = []
    
    # Continue the loop until n becomes 0
    while n > 0:
        # Find the modulus of n by 2
        remainder = n % 2
        # Append the remainder to the list
        binary_digits.append(remainder)
        # Update n to n divided by 2 (integer division)
        n = n // 2
    
    # Print the array in reverse order to get the correct binary representation
    binary_digits.reverse()
    
    return binary_digits

# Input a number
number = int(input("Enter an integer: "))

# Find and print the binary representation
binary_representation = decimal_to_binary(number)
print("The binary representation of", number, "is:", ''.join(map(str, binary_representation)))
