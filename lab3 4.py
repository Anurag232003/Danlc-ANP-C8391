# List of accepted currency notes
accepted_notes = [50, 100, 200, 500, 2000]

# Function to check if the note is correct
def check_currency_note():
    try:
        # Prompt the user to enter the currency note
        note = int(input("Please enter the currency note you want to deposit: "))

        # Check if the entered note is in the list of accepted notes
        if note in accepted_notes:
            print("You have provided a correct currency note for deposit.")
        else:
            print("You have provided an incorrect currency note. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Call the function
check_currency_note()


