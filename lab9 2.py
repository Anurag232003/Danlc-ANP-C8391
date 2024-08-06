class CustomValueError(Exception):
    pass

def get_valid_integer():
    try:
        user_input = input("Please enter an integer between 1 and 1000: ")
        user_input = int(user_input)
        if user_input < 1 or user_input > 1000:
            raise CustomValueError("The value provided is not between 1 and 1000.")
        print(f"Valid input received: {user_input}")
    except ValueError:
        print("Error: Input is not a valid integer.")
    except CustomValueError as e:
        print(f"Error: {e}")

get_valid_integer()

