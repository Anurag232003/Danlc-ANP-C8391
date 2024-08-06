import logging


logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def read_and_log(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        logging.error(f"FileNotFoundError: The file '{file_path}' does not exist.")
        print("Error: File not found.")
    except PermissionError:
        logging.error(f"PermissionError: Permission denied for file '{file_path}'.")
        print("Error: Permission denied.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred. Please check the log file.")

file_paths = [
    'existing_file.txt',  # Modify this path for testing
    'non_existent_file.txt',
    'no_permission_file.txt'
]

for file_path in file_paths:
    print(f"Reading file: {file_path}")
    read_and_log(file_path)
