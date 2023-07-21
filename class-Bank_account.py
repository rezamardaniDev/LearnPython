import os
os.system("cls")
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
        return f"owner: {self.name}+{other.name} | amount: {self.balance + other.balance} "
    
    def __iadd__(self, other):
        self.balance += other.balance
        other.balance = 0
        return self
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __str__(self) -> str:
        return f"owner: {self.name} | amount: {self.balance}"
    
john_acc = BankAccount('john', 1000)
david_acc = BankAccount('david', 1000)

print(john_acc+david_acc)

john_acc.transfer(100, david_acc)

david_acc.deposit(4000)

john_acc += david_acc

print(john_acc == david_acc)

print(john_acc)
print(david_acc)
