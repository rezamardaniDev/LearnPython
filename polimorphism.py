class Calculator:
    def __init__(self, tool, arz):
        self.tool = tool
        self.arz = arz


class moraba(Calculator):
    def __init__(self, tool, arz):
        super().__init__(tool, arz)


    def masahat(self):
        print(self.tool * self.arz)

class mostatil(Calculator):
    def __init__(self, tool, arz):
        super().__init__(tool, arz)


    def masahat(self):
        print(self.tool * self.arz // 2)

def mains(arg):
    return arg.masahat()

p1 = moraba(5, 4)
p2 = mostatil(2, 6)

mains(p1)
mains(p2)