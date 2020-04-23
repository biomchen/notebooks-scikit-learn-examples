from p2j import *
from itertools import compress

def py2jupyter(directory):
    allFiles = pathlib.Path(directory).glob('*')
    files = [file.name for file in allFiles]
    checkFiles = [str(file).endswith('.py') for file in files]
    pyFiles = list(compress(files, checkFiles))
    for pf in pyFiles:
        jf = pf.split('.')[0] + '.ipynb'
        p2j(pf, jf, True)

def main():
    print('Please write down your selected directory: ')
    directory = input()
    py2jupyter(directory)

if __name__ == "__main__":
    main()
