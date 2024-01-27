def count_number_of_upper_lower_letters(input_string):
    uppercase_letters = 0
    lowercase_letters = 0

    for char in input_string:
        if char.isupper():
            uppercase_letters += 1
        elif char.islower():
            lowercase_letters += 1

    return uppercase_letters, lowercase_letters


string = input('String : ')
upper_count, lower_count = count_number_of_upper_lower_letters(string)

print(f"Number of Uppercase letters : {upper_count}")
print(f"Number of Lowercase letters : {lower_count}")
