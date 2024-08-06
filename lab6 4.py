text = "Welcome to python Training"
vowels = "aeiouAEIOU"
vowel_count = {vowel: 0 for vowel in vowels}

for char in text:
    if char in vowels:
        vowel_count[char] += 1

print("Vowel counts in the given text:")
for vowel, count in vowel_count.items():
    if count > 0:
        print(f"{vowel}: {count}")
