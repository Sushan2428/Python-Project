def main():
    temp = input("Input the temperature in centigrade: ").strip().lower()
    temp = temp.removesuffix('c')
    temp = int(temp)
    print(f'The temperature is: {calculate(temp)}F')


def calculate(temp):
    a = temp * (9 / 5) + 32
    return a


main()

