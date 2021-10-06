import time


class Account(object):
    account_number = 0

    def __init__(self, name, balance):
        self.account_number = Account.account_number
        self.name = name
        self.balance = balance
        self.show_balance()
        self.transaction_history = []
        Account.account_number += 1

    def withdraw(self, price):
        if self.balance < price:
            print("残高が不足しています。引き出しできません")
        else:
            print(f"{price} を引き出しました")
            self.balance -= price
            # 日付情報は、トランザクションを追加するメソッドで取得する
            # date_tran = self.transaction_date()
            self.transaction(-price)
        self.show_balance()

    def deposit(self, price):
        self.balance += price
        # date_tran = self.transaction_date()
        self.transaction(price)
        self.show_balance()

    def show_balance(self):
        print(f"name:{self.name}  account_number:{self.account_number}  balance:{self.balance}")

    def transaction(self, price):
        # 日付情報を取得するスタティックメソッドを呼ぶ
        tran_dict = {
            'date': Account.transaction_date(),
            'balance': self.balance,
            'withdraw/deposit': price
        }
        self.transaction_history.append(tran_dict)

    @staticmethod
    def transaction_date():
        tran_date = time.localtime()
        date_tran = "{0.tm_year}/{0.tm_mon}/{0.tm_mday}/{0.tm_hour}/{0.tm_min}/{0.tm_sec}".format(tran_date)
        return date_tran


john_account = Account('john', 100000)
print()
john_account.withdraw(1100000)
john_account.withdraw(30000)
john_account.deposit(50000)
print()
print(john_account.transaction_history)

print()
emma_account = Account('emma', 50000)
emma_account.withdraw(1100000)
emma_account.withdraw(30000)
emma_account.deposit(50000)
print()
print(emma_account.transaction_history)
