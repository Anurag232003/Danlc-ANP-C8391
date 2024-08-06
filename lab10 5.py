def traverse_reverse_with_index(lst):
    for i in range(len(lst)-1, -1, -1):
        print(f"Index {i}: {lst[i]}")

# Example usage
original_list = ['red', 'green', 'white', 'black']
print("Original list:", original_list)
print("Traverse the said list in reverse order:")
traverse_reverse_with_index(original_list)
