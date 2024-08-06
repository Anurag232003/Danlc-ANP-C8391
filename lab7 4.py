def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count

input_string = "Welcome to Python Assignment"
vowel_count = count_vowels(input_string)

print(f"Total vowels are: {vowel_count}")
