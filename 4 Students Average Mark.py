"""Program to keep track of students marks and grades
"""



print("Hi, I am your English teacher. "
      "This is to record students' grades. "
      "If there are no more students to enter, "
      "type an 'X'")

while studentname != "x" or "X":
studentname = input("Enter the student's name: ")
studentgrade = int(input("Enter the mark, 0-100: "))

if studentname == "x" or "X":
    exit()

total_marks = 0
total_students = 0
best_mark = 0
best_student = ""

while True:
    name = input("Enter the student's name: ")
    if name == "x" or "X":
        exit()
    else:
        mark = int(input("Enter the student's mark: "))
4
