def convert_to_float(strings):
    floats = []
    errors = []
    
    for s in strings:
        try:
            value = float(s)
            floats.append(value)
        except ValueError as ve:
            errors.append((s, f"ValueError: {ve}"))
        except Exception as e:
            errors.append((s, f"Unexpected error: {e}"))
    
    return floats, errors


strings = ['10.5', 'abc', '3.14', '42', 'NaN', '']
floats, errors = convert_to_float(strings)

print("Converted floats:", floats)
print("Errors:", errors)
