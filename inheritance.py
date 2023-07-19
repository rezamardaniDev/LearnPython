class Person:
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

    def fullnam(self):
        return f"{self.firstname} {self.lastname}"


class Student(Person):
    def __init__(self,firstname: str,lastname: str,major: str ):
        super().__init__(firstname, lastname)
        self.major = major


p1 = Student("ali", "zere", "cp")
print(p1.fullnam())