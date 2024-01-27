def last_char_remove(input_data):
    if len(input_data) <= 1:
        return input_data
    else:
        return input_data[:-1]


data = input('Enter data : ')
result = last_char_remove(data)
print(f"""
Original data: {data}
Data after last character removed: {result}
""")

