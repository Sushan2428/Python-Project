def obfuscate(message):
    letters = [c for c in message if c.isalpha()]
    letters.reverse()

    return ''.join(letters)


string = input('String : ')
print(f'"{string}" -> "{obfuscate(string)}"')
