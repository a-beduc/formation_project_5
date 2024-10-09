class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        """ Deposit money into the account holder """
        try:
            if amount > 0:
                self.balance += amount
        except TypeError:
            print(f'Could not deposit "{amount}". Invalid amount, amount must be a number')

    def withdraw_v1(self, amount: float):
        """ Withdraw amount from bank account, if you block over-withdraws. """
        try:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print('Insufficient funds')
        except TypeError:
            print(f'Could not withdraw "{amount}". Invalid amount, amount must be a number')

    def withdraw_v2(self, amount: float):
        """
        Withdraw amount from bank account, if you resolve over-withdraws by withdrawing the content of the account.
        """
        try:
            if amount >= 0:
                self.balance = self.balance - min(amount, self.balance)
            # new_balance = self.balance - amount
            # if new_balance < 0:
            #     withdraw_amount = self.balance
            #     self.balance = 0
            #     print(f'You tried to over-withdraw : "{amount}", could only withdraw "{withdraw_amount}"')
            # else:
            #     self.balance = new_balance
        except TypeError:
            print(f'Could not withdraw "{amount}". Invalid amount, amount must be a number')

    def display_balance(self):
        print(f"{self.account_holder} : {self.balance}")


def main():
    account_01 = BankAccount('Jack', 10000)
    account_01.deposit(12)
    account_01.withdraw_v2(11000)
    account_01.display_balance()


if __name__ == '__main__':
    main()
