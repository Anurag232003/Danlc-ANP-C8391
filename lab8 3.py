def count_uppercase_characters(file_path):
    uppercase_count = 0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                for char in line:
                    if char.isupper():
                        uppercase_count += 1
                        
        print(f"Total number of uppercase characters in the file {file_path}: {uppercase_count}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
count_uppercase_characters('ABC.txt')
