"""Bank App"""
from bank_class import Account
from exception import num_there, numb_warning, alpha_warning
from read_write import read_file, save_file

print('#' * 42)
print('# Hello and Welcome to ALONSO RURAL BANK #')
print('#' * 42)

loop = True
while loop:
    while True:
        ask_question = str(input('Please would you like to open an Account with Us? [yes / no]'))
        if num_there(ask_question):
            numb_warning()
        else:
            break
    if ('y'.lower() in ask_question) or ('e'.lower() in ask_question) or ('s'.lower() in ask_question):
        print('Hello again, My name is Auto-bot and I\'ll be '
              'guiding you through your Account creation '
              '\nFirst I need some few details about you')
        while True:
            full_name = str(input('Please enter your name in full:'))
            if num_there(full_name):
                numb_warning()
            else:
                break
        while True:
            initial_balance = str(input('Please would you like to make an '
                                        'initial deposit? [yes/no]'))
            if num_there(initial_balance):
                numb_warning()
            else:
                break
        if initial_balance == 'yes':
            while True:
                try:
                    amount = int(input('How much will you like to deposit: '))
                    new_account = Account(full_name, amount)
                    print('-' * 19)
                    print('Account Information')
                    print('-' * 19)
                    print(new_account)
                    print('-' * 19)
                    break

                except ValueError as error:
                    alpha_warning()

        else:
            new_account = Account(full_name)
            print('-' * 19)
            print('Account Information')
            print('-' * 19)
            print(new_account)
            print('-' * 19)
        print('Your Account has been Created!!!')

    else:
        print('\n')
        print('#' * 32)
        print('Thank You for Your Co-operation \nExiting.....')
        print('#' * 32)
        print('\n\n')

        print('$' * 26)
        print("$ Bank Accounts Database $")
        print('$' * 26, f'\n')

        try:
            save_file(str(new_account))
        except NameError:
            pass
            # print('Could not save Account Information')
        read_file()

        break

    print('\n\n')

    bool_action = True
    while bool_action:
        while True:
            action = str(
                input('Please input \'d\' to Deposit, \'w\' to withdraw, \'i\' to '
                      'print your Account Info, '
                      '\'p\' to print your Account Statement or \'e\' to exit'))
            if num_there(action):
                print('Input should be alphabets')
            else:
                break
        if action == 'd'.lower():
            print('\n')
            print('-' * 19)
            while True:
                try:
                    d_amount = int(input('How much will you like to deposit: '))
                    print(new_account.deposit(d_amount))
                    print('-' * 19)
                    print('\n')
                except ValueError:
                    alpha_warning()
                else:
                    break

        elif action == 'w'.lower():
            print('\n')
            print('-' * 19)
            while True:
                try:
                    w_amount = int(input('How much will you like to withdraw: '))
                    print(new_account.withdraw(w_amount))
                    print('-' * 19)
                    print('\n')
                except ValueError:
                    alpha_warning()
                else:
                    break

        elif action == 'i'.lower():
            print('\n')
            print('-' * 19)
            print(new_account)
            print('-' * 19)
            print('\n')
        elif action == 'p'.lower():
            print('\n')
            print('-' * 19)
            new_account.print_records(new_account.history())
            print('-' * 19)
            print('\n')
        elif action == 'e'.lower():
            break
