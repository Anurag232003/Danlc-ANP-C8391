def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")


file_path = 'hello.txt'
read_file(file_path)

