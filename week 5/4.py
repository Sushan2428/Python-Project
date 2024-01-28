from sys import argv
import urllib.request

HTTP_SUCCESS = 200

if __name__ == '__main__':
    try:
        code = urllib.request.urlopen(argv[1]).getcode()

        if code == HTTP_SUCCESS:
            print(f'Webpage at "{argv[1]}" looks OK.')
        else:
            print(f'No Webpage found at "{argv[1]}".')
    except IndexError:
        print('No URL on command-line. Nothing to do.')
    except:
        print('Something unexpected happened. Probably a DNS failure. Does the server exist?')