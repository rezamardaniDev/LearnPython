date = input("enter date time: ")

with open(f"{date}.txt", "r") as file:
    
    student_list = file.readlines()
    print(f"\nstudent List in {date}")
    for name in student_list:
        print(name.strip("\n"))
    print("\n")
