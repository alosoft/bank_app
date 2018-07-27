"""Input and Output to file(text files)"""


def save_file(string):
    """
    This function saves a text file in its parent directory

    param string:
    param file_name: default.txt
    return: saves a file
    """
    try:
        file = open('bank.txt', 'a')
        lines = '*' * 100
        file.write(f'{lines}\n' + string + f'\n{lines}\n\n')
        file.close()
    except IOError as error:
        print(error, f'\nCould not save file from Database')


def read_file():
    """
    This function reads a text file in its parent directory

    param string:
    param file_name: default.txt
    return: strings red form file
    """
    try:
        file = open('bank.txt', 'r')
        returned = ''
        print(returned.join([i for i in file.readlines()]))
        file.close()
    except IOError as error:
        print(error, f'\nCould not read file from Database')
