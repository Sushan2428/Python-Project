from sys import argv


if __name__ == '__main__':
    args = len(argv) - 1
    print(f'This program has {args} argument{"s" if args != 1 else ""}.')