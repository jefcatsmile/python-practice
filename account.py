class Account(object):
    account_number = 0

    def __init__(self, name, balance):
        # クラス変数は、＜クラス名＞.クラス変数名　で処理
        self.account_number = Account.account_number
        self.name = name
        self.balance = balance
        self.show_balance()
        Account.account_number += 1

    def withdraw(self, price):
        if self.balance < price:
            print("残高が不足しています。引き出しできません")
        else:
            print(f"{price} を引き出しました")
            self.balance -= price
        # インスタンスメソッドを呼ぶときは、self. をつける
        self.show_balance()

    def deposit(self, price):
        self.balance += price
        self.show_balance()

    def show_balance(self):
        print(f"name:{self.name}  account_number:{self.account_number}  balance:{self.balance}")


john_account = Account('john', 100000)
emma_account = Account('emma', 50000)
print()
john_account.withdraw(1100000)
john_account.withdraw(30000)
john_account.deposit(50000)
print()
emma_account.withdraw(1100000)
emma_account.withdraw(30000)
emma_account.deposit(50000)
