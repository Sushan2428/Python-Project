def letters_in_either(word1, word2):
    combined_letters = set(word1.lower()) | set(word2.lower())
    return sorted(combined_letters)


def letters_in_both(word1, word2):
    common_letters = set(word1.lower()) & set(word2.lower())
    return sorted(common_letters)


def letters_in_either_not_both(word1, word2):
    unique_letters_word1 = set(word1.lower()) - set(word2.lower())
    unique_letters_word2 = set(word2.lower()) - set(word1.lower())
    combined_unique_letters = unique_letters_word1 | unique_letters_word2
    return sorted(combined_unique_letters)


# Test the functions
word_1 = input('Enter 1st word : ')
word_2 = input("Enter 2nd word : ")

result1 = letters_in_either(word_1, word_2)
result2 = letters_in_both(word_1, word_2)
result3 = letters_in_either_not_both(word_1, word_2)

print("Letters in at least one of the two words:", result1)
print("Letters in both words:", result2)
print("Letters in either word, but not in both:", result3)
