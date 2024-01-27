a = int(input('Which number multiplication table do you want? '))
if 0 <= a <= 12:
    print(f'multiplication table of {a}')
    for i in range(13):
        print(f'{a} X {7} = {i * a}')
else:
    print('The number should be between 0 to 12')
