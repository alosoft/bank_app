def num_there(s):
    # check if user input contains numbers
    return any(i.isdigit() for i in s)


def numb_warning():
    # print warning if user input number
    print('*' * 28)
    print('Input should be ONLY alphabets')
    print('*' * 28)


def alpha_warning():
    # print warning if user input word
    print('*' * 46)
    print('Input should be ONLY digits')
    print('*' * 46)
