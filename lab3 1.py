def is_alphabet(character):
    # Check if the character is an alphabet using isalpha() method
    return character.isalpha()

# Example usage:
char = input("Enter a character: ")

if is_alphabet(char):
    print(f"The character '{char}' is an alphabet.")
else:
    print(f"The character '{char}' is not an alphabet.")