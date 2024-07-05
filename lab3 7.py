def print_denomination(amount):
    # Define the denominations
    denominations = [2000, 500, 200, 100, 50]
    
    # Create a dictionary to store the count of each denomination
    denomination_count = {}
    
    # Calculate the number of each denomination
    for denom in denominations:
        if amount >= denom:
            count = amount // denom
            amount -= count * denom
            denomination_count[denom] = count
    
    # Print the result
    for denom, count in denomination_count.items():
        print(f"{denom}X{count}={denom*count}")
    
    # Print the total
    total = sum(denom * count for denom, count in denomination_count.items())
    print(f"Total {total}")

# Example usage
input_amount = 13450
print_denomination(input_amount)


