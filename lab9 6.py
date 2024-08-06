import datetime

def get_valid_date():
    while True:
        date_input = input("Please enter a date in the format YYYY-MM-DD: ")
        try:
            year, month, day = map(int, date_input.split('-'))
            valid_date = datetime.date(year, month, day)
            return valid_date
        except ValueError as e:
            if "unconverted data" in str(e) or "too many values to unpack" in str(e):
                print("Error: Invalid format. Please enter the date in the format YYYY-MM-DD.")
            elif "day is out of range for month" in str(e):
                print("Error: Invalid day for the given month.")
            elif "month must be in 1..12" in str(e):
                print("Error: Month must be between 1 and 12.")
            else:
                print(f"Error: {e}")

# Example usage
valid_date = get_valid_date()
print(f"Valid date entered: {valid_date}")

