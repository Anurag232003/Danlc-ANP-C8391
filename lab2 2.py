# Function to check if a character is lowercase or uppercase
def check_character_case(char):
    if 'A' <= char <= 'Z':
        return "The character is uppercase."
    elif 'a' <= char <= 'z':
        return "The character is lowercase."
    else:
        return "The character is neither uppercase nor lowercase."

# Input from the user
character = input("Enter a character: ")

# Ensure the input is a single character
if len(character) == 1:
    # Check and display the result
    result = check_character_case(character)
    print(result)
else:
    print("Please enter a single character.")
