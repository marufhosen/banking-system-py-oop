class BankingSyatem:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def diposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"New balance: {self.balance}")
        else:
            print("Insuffient fund!")


class SavingsAccount(BankingSyatem):
    def __init__(self, acc_no, balance, interest_rate=0.05):
        BankingSyatem.__init__(self, acc_no, balance)
        self.interest_rate = interest_rate

    def add_to_accc(self):
        total_balance = self.balance * self.interest_rate
        self.diposit(total_balance)
        print(f"Interest added. New balance: ${self.balance}")


class CheckingAccount(BankingSyatem):
    def __init__(self, acc_no, balance, limit):
        BankingSyatem.__init__(self, acc_no, balance)
        self.limit = limit

    def withdraw_with_limit(self, amount):
        total_wd_balance = self.balance + self.limit
        self.balance = total_wd_balance
        if amount <= total_wd_balance:
            self.withdraw(amount)
        else:
            print(f"Insuffient amount with limit. Available bal: {self.balance}")


# savings_account = BankingSyatem("MARUF-1JKFGH")
# savings_account.diposit()
# savings_account.withdraw()

savings_acc = SavingsAccount("MARUF-1JKFGH", 300)
savings_acc.add_to_accc()

checking_acc = CheckingAccount(acc_no="MARUF-1JKFGH", balance=500, limit=100)
checking_acc.withdraw_with_limit(900)
