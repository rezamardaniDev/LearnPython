class DataBase:
    def __init__(self, name, number) -> None:
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name} : {self.number}"
    
p1 = DataBase("ali", 45788)
print(p1)
