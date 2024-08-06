def find_duplicates(items):
    duplicates = []
    seen = set()
    
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    
    return duplicates

# Example usage
numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
duplicates = find_duplicates(numbers)
print("Duplicate values are:", duplicates)
