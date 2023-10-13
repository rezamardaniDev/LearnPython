date = input("enter date time: ")
names = input("enter students name: ").split(" ")

with open(f"{date}.txt", "w+") as list_students:
    for name in names:
        list_students.write(f"{name}\n")
    list_students.close()


