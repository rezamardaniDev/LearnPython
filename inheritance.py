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


# class Student:
#     def __init__(self, fitrstname:str, lastname:str, major:str, uni:str) -> None:
#         self.firtstname = fitrstname
#         self.lastname = lastname
#         self.major = major
#         self.uni = uni

#     def how_i_am(self):
#         return f"{self.firtstname} {self.lastname}"
    
# class Teacher:
#       def __init__(self, fitrstname:str, lastname:str, department:str, uni:str) -> None:
#         self.firtstname = fitrstname
#         self.lastname = lastname
#         self.departmant = department
#         self.uni = uni

#       def how_i_am(self):
#         return f"{self.firtstname} {self.lastname} im a teacher in {self.uni} university"
    

# t1 = Teacher("ali", "zare", "mit", "fasa")
# print(t1.how_i_am())