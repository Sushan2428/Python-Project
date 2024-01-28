from sys import argv


if __name__ == '__main__':
    if len(argv) == 1:
        print('No CLAs provided. So none is the shortest.')
    elif len(argv) == 2:
        print(f'Just the one CLA, so it must be shortest: {argv[1]}.')
    else:
        sorted_args = argv[:]
        sorted_args.sort(key=len)
        print(f'Shorted argument (of the {len(argv) - 1}): {sorted_args[0]}.')