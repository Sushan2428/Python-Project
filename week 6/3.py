def main():
    x = int(input("enter the number to check if it is a prime or not : "))
    print(x, "is a prime number.", prime(x))


count = 0


def prime(x):
    global count
    count = 0

    if x == 1:
        return "One is neither prime nor composite."
    elif x > 1:
        for i in range(1, x + 1):
            if x % i == 0:
                count = count + 1
                if count > 2:
                    return False
        return True
    else:
        return False


main()