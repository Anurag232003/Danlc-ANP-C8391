def remove_duplicates(input_string):
    seen = set()
    result = []

    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)

input_string = "String and String Function"
output_string = remove_duplicates(input_string)

print(f"Output: {output_string}")
