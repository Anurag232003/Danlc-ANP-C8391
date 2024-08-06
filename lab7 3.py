def count_char_types(input_string):
    uppercase = lowercase = numeric = special = 0

    for char in input_string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            numeric += 1
        elif not char.isspace():  # Count special characters excluding spaces
            special += 1

    return uppercase, lowercase, numeric, special

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase, lowercase, numeric, special = count_char_types(input_string)

print(f"UpperCase: {uppercase}")
print(f"LowerCase: {lowercase}")
print(f"NumberCase: {numeric}")
print(f"SpecialCase: {special}")
