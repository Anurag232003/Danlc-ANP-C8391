def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range."
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"


test_list = [10, 20, 30, 40, 50]

print(safe_list_access(test_list, 2))  
print(safe_list_access(test_list, -1))  
print(safe_list_access(test_list, 10))  
print(safe_list_access(test_list, 'a')) 
print(safe_list_access([], 0))  
print(safe_list_access(test_list, -6))  
