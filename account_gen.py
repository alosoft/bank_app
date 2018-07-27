import random


def account_number_generator():
    num = '300126'
    for i in range(7):
        num += str(random.randint(0, 9))
    return int(num)


def save_account_number():
    try:
        file = open('account_numbers.txt', 'r')
        account_number = account_number_generator()
        while True:
            for each_number in file.readlines():
                new_number = int(each_number[:-1])
                if account_number == new_number:
                    # if account number exit, create new account number
                    account_number = account_number_generator()

            else:
                break

        file.close()
        file = open('account_numbers.txt', 'a')
        file.write(str(account_number) + '\n')
        file.close()
    except IOError:
        print('Could not save Account Number')


def read_account_number():
    try:
        file = open('account_numbers.txt', 'r')
        returned = ''
        print(returned.join([i for i in file.readlines()]))
        file.close()
    except IOError:
        print('Could not read Account Number')


save_account_number()
