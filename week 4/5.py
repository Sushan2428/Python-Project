def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return celsius


temperature = float(input('Temperature : '))
temperature_unit = input('Is temperature in "C" or "F"? ').upper()
converted_fahrenheit = celsius_to_fahrenheit(temperature)
converted_celsius = fahrenheit_to_celsius(temperature)
if temperature_unit in 'C':
    print(f'''
Temperature in Celsius = {format(temperature, '.2f')} C
Temperature in Fahrenheit = {format(converted_fahrenheit, '.2f')} F
''')
else:
    print(f'''
Temperature in Fahrenheit = {format(temperature, '.2f')} F
Temperature in Celsius = {format(converted_celsius, '.2f')} C
''')
