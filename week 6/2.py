def main():
    x = int(input("enter the number to find factor of : "))
    factors(x)


def factors(x):
    print ("the factor of x is:")
    for i in range(1, x + 1):
        # if it is perfectly divisible it is a factor otherwise it is not a factor
        if x % i == 0:
            print(i)


main()