class Person:
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

class Student(Person):
    def __init__(self,firstname: str,lastname: str,major: str , uni):
        super().__init__(firstname, lastname)
        self.major = major
        self.uni = uni

    def fullname(self):
        return f"i study {self.major} lesson on {self.uni} university"


class Teacher(Person):
    def __init__(self, firstname: str, lastname: str, uni : str, departmanet: str):
        super().__init__(firstname, lastname)
        self.uni = uni
        self.departmanet = departmanet

    def working_ifno(self):
        return f"i work in {self.uni} at {self.departmanet}"
    

s1 = Student("ali", "zare", "computer", "fasa")
print(s1.fullname())

t1 = Teacher("reza", "mardani", "fasa", "math")
print(t1.fullname())