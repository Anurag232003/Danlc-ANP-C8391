def check_character(char):
    if char.isalpha():
        return "Alphabet"
    elif char.isdigit():
        return "Number"
    else:
        return "Special Character"

# Input character from user
char = input("Enter a character: ")

# Check and print the result
result = check_character(char)
print(f"The character '{char}' is a {result}.")


