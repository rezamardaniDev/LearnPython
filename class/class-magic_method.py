class Square:

    def __init__(self, side_lenght) -> None:
        self.s = side_lenght

    def __str__(self) -> str:
        return f"{self.s}"
    
    def __len__(self):
        return self.s


square = Square(2)
print(len(square))