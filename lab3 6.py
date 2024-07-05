def calculate_electricity_bill(units):
    if units < 200:
        return 0
    elif units <= 300:
        return (units - 200) * 1.2
    elif units <= 400:
        return 100 * 1.2 + (units - 300) * 1.5
    elif units <= 500:
        return 100 * 1.2 + 100 * 1.5 + (units - 400) * 2.5
    else:
        return 100 * 1.2 + 100 * 1.5 + 100 * 2.5 + (units - 500) * 8

# Take user input
units_consumed = int(input("Enter the units of electricity consumed: "))
bill_amount = calculate_electricity_bill(units_consumed)

# Print the bill amount
print(f"The electricity bill for {units_consumed} units is: {bill_amount}")


