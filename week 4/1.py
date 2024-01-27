def num():
    number = int(input("enter a number:"))
    print(f"The number {number} in range of 1-100: {check(number)}")


def check(number):
    if number not in range(0, 101):
        return False
    else:
        return True


num()
