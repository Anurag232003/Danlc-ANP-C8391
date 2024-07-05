def check_character_type(char):
    # Check if the character is an alphabet
    if char.isalpha():
        print(f"{char} is an alphabet.")
    # Check if the character is a digit
    elif char.isdigit():
        print(f"{char} is a number.")
    # If neither alphabet nor digit, it's a special character
    else:
        print(f"{char} is a special character.")

# Example usage:
character = input("Enter a character: ")
check_character_type(character)
