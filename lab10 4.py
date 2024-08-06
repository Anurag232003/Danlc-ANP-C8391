def split_list(lst, length_of_first_part):
    if length_of_first_part > len(lst):
        return lst, []
    
    first_part = lst[:length_of_first_part]
    second_part = lst[length_of_first_part:]
    
    return first_part, second_part

# Example usage
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3
first_part, second_part = split_list(original_list, length_of_first_part)

print("Original list:", original_list)
print("Length of the first part of the list:", length_of_first_part)
print("Splitted the said list into two parts:", (first_part, second_part))
