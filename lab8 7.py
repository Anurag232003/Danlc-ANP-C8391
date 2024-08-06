def search_and_replace(file_path, search_string, replace_string):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        new_content = content.replace(search_string, replace_string)
        
        with open(file_path, 'w') as file:
            file.write(new_content)
        
        print(f"All occurrences of '{search_string}' have been replaced with '{replace_string}' in the file {file_path}.")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get file path, search string, and replace string from user
file_path = input("Enter the file path: ")
search_string = input("Enter the string to search: ")
replace_string = input("Enter the string to replace with: ")

# Call the function
search_and_replace(file_path, search_string, replace_string)

