class BankAccount:

    balance = 0
    num_of_withdrawals = 0

    def __init__(self, amount: int):
        self.balance = amount

    def deposit(self, amount: int):
        if amount > 0:
            print("I am easily reachable in deposit")
            self.balance = self.balance + amount

    def withdraw(self, amount: int):
        if amount > self.balance:
            print("I am easily reachable in withdraw")
            return
        if self.num_of_withdrawals >= 5:
            assert False
            print("I am very hard to reach in withdraw")
            return
        self.balance = self.balance - amount
        self.num_of_withdrawals += 1


# Test driver
def flag(x: bool):
    if x:
        return 1
    else:
        return 0


def test_driver(length: int):
    b = BankAccount(0)
    for i in range(length):
        if flag(True) == 0:
            b.deposit(10)
        else:
            b.withdraw(1)


if __name__ == '__main__':
    test_driver(3)
