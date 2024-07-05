# Function to check if a character is an alphabet
def is_alphabet(char):
    # Check if the character is between 'a' and 'z' or 'A' and 'Z'
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        return True
    else:
        return False

# Input from the user
character = input("Enter a character: ")

# Ensure the input is a single character
if len(character) == 1:
    # Check and display the result
    if is_alphabet(character):
        print(f"{character} is an alphabet.")
    else:
        print(f"{character} is not an alphabet.")
else:
    print("Please enter a single character.")
