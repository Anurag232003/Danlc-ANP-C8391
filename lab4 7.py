# Initialize the starting character
char = 'a'

# Loop until the character is less than or equal to 'z'
while char <= 'z':
    # Print the current character
    print(char, end=' ')
    # Move to the next character
    char = chr(ord(char) + 1)
