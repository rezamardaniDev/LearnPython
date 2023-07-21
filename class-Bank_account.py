class BankAccount:
    def __init__(self, name:str, balance:int=0) -> None:
        self.name = name
        self.balance = balance
    
    def transfer(self,amount, target):
        self.balance -= amount
        target.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __add__(self, other):
        return f"owner: {self.name}+{other.name} --> {self.balance + other.balance} "