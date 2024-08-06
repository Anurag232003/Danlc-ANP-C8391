def copy_file_contents(source_file_path, destination_file_path):
    try:
        with open(source_file_path, 'r') as source_file:
            content = source_file.read()
        
        with open(destination_file_path, 'w') as destination_file:
            destination_file.write(content)
        
        print(f"Contents copied from {source_file_path} to {destination_file_path} successfully.")
    except FileNotFoundError:
        print(f"One of the files {source_file_path} or {destination_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get file paths from user
source_file_path = input("Enter the destination file path: /storage/emulated/0/python /lab2 1.py ")
destination_file_path = input("Enter the destination file path: /storage/emulated/0/python /lab2 2.py  ")

# Call the function
copy_file_contents(source_file_path, destination_file_path)

