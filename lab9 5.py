def parse_file(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                try:
                    number = float(line)
                    numbers.append(number)
                except ValueError:
                    print(f"ValueError: Non-numeric data found on line {line_number}: '{line}'")
    except FileNotFoundError:
        print(f"FileNotFoundError: The file '{file_path}' does not exist.")
    except PermissionError:
        print(f"PermissionError: Permission denied for file '{file_path}'.")

    return numbers

# Example usage
file_path = 'numbers.txt'
numbers = parse_file(file_path)
print("Parsed numbers:", numbers)

