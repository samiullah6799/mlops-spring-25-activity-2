class Bank:
    def __init__(self):
        self.amount = 0

    def deposit(self, amount):
        self.amount += amount

    def withDraw(self, amount):
        self.amount -= amount

    def getAmount(self):
        return self.amount