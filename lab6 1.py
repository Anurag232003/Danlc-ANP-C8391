def count_word_occurrences(sentence):
    
    cleaned_sentence = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in sentence)
    
    
    words = cleaned_sentence.split()
    
   
    word_counts = {}
    
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts


sentence = "To change the overall look of your document. To change the look available in the gallery"


word_occurrences = count_word_occurrences(sentence)


for word, count in word_occurrences.items():
    print(f"{word}: {count}")
