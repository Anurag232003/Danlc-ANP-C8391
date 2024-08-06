def count_words_in_file(file_path):
    total_words = 0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                total_words += len(words)
                
        print(f"Total number of words in the file {file_path}: {total_words}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
count_words_in_file('ABC.txt')
