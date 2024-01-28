from shutil import copyfile
from sys import argv
# In this program we must have to run program using terminal & we back up any file using terminal

if __name__ == '__main__':
    try:
        filename_in = argv[1]
        filename, extension = filename_in.split('.')

        filename_out = f'{filename}-backup.{extension}'

        copyfile(filename_in, filename_out)
    except IndexError:
        print('No filename supplied. Nothing to do.')
    except ValueError:
        print('Argument does not look like a filename. Cannot find file extension.')
    except FileNotFoundError:
        print(f'Cannot open "{filename_in}". Bailing out.')
