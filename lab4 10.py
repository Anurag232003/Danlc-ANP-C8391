def categorize_age(age):
    if age >= 18:
        return "Adult"
    elif age >= 4:
        return "School-age student"
    elif age >= 0:
        return "Baby"
    else:
        return "Invalid age"

def count_categories(ages):
    adult_count = 0
    baby_count = 0
    school_age_count = 0
    
    for age in ages:
        category = categorize_age(age)
        if category == "Adult":
            adult_count += 1
        elif category == "School-age student":
            school_age_count += 1
        elif category == "Baby":
            baby_count += 1
    
    return adult_count, school_age_count, baby_count

# Initialize an empty list to store ages
ages = []

# Read ages from user input
print("Enter ages of 15 people:")
for i in range(15):
    age = int(input(f"Enter age {i+1}: "))
    ages.append(age)

# Count categories
adult_count, school_age_count, baby_count = count_categories(ages)

# Print results
print(f"\nNumber of adults: {adult_count}")
print(f"Number of school-age students: {school_age_count}")
print(f"Number of babies: {baby_count}")
