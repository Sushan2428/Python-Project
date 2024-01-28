def frequency_analysis(message):
    message = message.lower()
    message = message.replace(" ", "")
    character_counts = {}
    for character in message:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    sorted_letter_counts = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_letter_counts[:6]


text = input("Enter your message : ")
result = frequency_analysis(text)
for letter, count in result:
    print(f"{letter}: {count}")
