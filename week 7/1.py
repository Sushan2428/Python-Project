def unique_letters_sorted(input_string):
    input_string = input_string.lower()
    unique_letters = set()
    for char in input_string:
        if char.isalpha():
            unique_letters.add(char)
    sort_letters = sorted(list(unique_letters))
    return sort_letters


string = input('String : ')
output = unique_letters_sorted(string)
print(output)
