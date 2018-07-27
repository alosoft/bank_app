"""Contains all Class methods and functions and their implementation"""
import random


def account_number():
    """generates account number"""
    num = '300126'
    for _ in range(7):
        num += str(random.randint(0, 9))
    return int(num)


def make_dict(string, integer):
    """makes a dictionary of Account Names and Account Numbers"""
    return {string: integer}


class Account:
    """
    This Class contains Balance and  Name with functions like Withdraw, Deposit and Account History
    """

    def __init__(self, name, balance=0, total_deposit=0, total_withdrawal=0):
        """Constructor of __init__"""
        self.name = name.title()
        self.balance = balance
        self.records = [f'Default Balance: \t${self.balance}']
        self.total_deposit = total_deposit
        self.total_withdrawal = total_withdrawal
        self.account = account_number()

    def __str__(self):
        """returns a string when called"""
        return f'Account Name:\t\t{self.name} \nAccount Balance:\t${str(self.balance)} ' \
               f'\nAccount History:\t{self.records} \nAccount Number:\t\t{ self.account}'

    def __len__(self):
        """returns balance"""
        return self.balance

    def history(self):
        """returns Account Information"""
        return self.records

    def print_records(self, history):
        """Prints Account Records"""
        line = ' \n'
        print(line.join(history) + f' \n\nTotal Deposit: \t\t${str(self.total_deposit)} '
                                   f'\nTotal Withdrawal: \t${str(self.total_withdrawal)} '
                                   f'\nTotal Balance: \t\t${str(self.balance)} ')

    def deposit(self, amount):
        """Deposit function"""
        self.total_deposit += amount
        self.balance += amount
        self.records.append(f'Deposited: ${amount}')
        return f'Deposited: ${amount}'

    def withdraw(self, amount):
        """Withdrawal function"""
        if self.balance >= amount:
            self.total_withdrawal += amount
            self.balance -= amount
            self.records.append(f'Withdrew: ${amount}')
            return f'Withdrew: ${amount}'

        self.records.append(
            f'Balance: ${str(self.balance)} '
            f'is less than intended Withdrawal Amount: ${amount}')
        return f'Invalid command \nBalance: ${str(self.balance)} ' \
               f'is less than intended Withdrawal Amount: ${amount}'
