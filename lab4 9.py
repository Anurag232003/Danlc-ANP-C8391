def is_leap_year(year):
    # A year is a leap year if it is divisible by 4, except for years that are divisible by 100.
    # However, years divisible by 400 are leap years.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def print_leap_years(n):
    year = 1
    while year <= n:
        if is_leap_year(year):
            print(year)
        year += 1

# Input from the user
n = int(input("Enter the value of n: "))
print(f"Leap years from 1 to {n} are:")
print_leap_years(n)
