a = int(input('Which number multiplication table do you want? '))
if -12 <= a <= 12:
    if a >= 0:
        print(f'multiplication table of {a}')
        for i in range(13):
            print(f'{a} X {i} = {i * a}')
    else:
        a = abs(a)
        print(f'multiplication table of {a}')
        for i in range(12, 0, -1):
            print(f'{a} X {i} = {i * a} ')

else:
    print('The number should be between -12 to 12')
