def display_words(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                short_words = [word for word in words if len(word) < 4]
                for word in short_words:
                    print(word)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
display_words('story.txt')

