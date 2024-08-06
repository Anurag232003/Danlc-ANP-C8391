def rotate_list(lst, k):
    if not lst:
        return lst
    
    # Handle cases where k is greater than the length of the list
    k = k % len(lst)
    
    return lst[-k:] + lst[:-k]

# Example usage
original_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(original_list, 2)
print("Rotated list:", rotated_list)
