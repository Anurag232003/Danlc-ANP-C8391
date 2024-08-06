def search_word_in_file(file_path, search_word):
    word_count = 0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                word_count += words.count(search_word)
                
        print(f"The word '{search_word}' occurs {word_count} times in the file {file_path}.")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get file path and word to search from user
file_path = input("Enter the file path: ")
search_word = input("Enter the word to search: ")

# Call the function
search_word_in_file(file_path, search_word)

