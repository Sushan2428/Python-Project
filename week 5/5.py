from statistics import mean
from sys import argv


def chomp(s):
    return s[:-1] if len(s) > 1 else s


def read_temperatures(temp_list):
    temps = []

    for arg in temp_list:
        if arg.endswith(('C', 'c')):
            temps.append(float(chomp(arg)))
        else:
            raise ValueError('Invalid data on command-line')

    return temps


def print_results(temps_list):
    print()
    print(f'Max Temp:  {max(temps_list):6.2f}C.')
    print(f'Min Temp:  {min(temps_list):6.2f}C.')
    print(f'Mean Temp: {mean(temps_list):6.2f}C.')
    print()


if __name__ == '__main__':

    try:
        print_results(read_temperatures(argv[1:]))
    except ValueError:
        print('Error processing data. How sad.')
