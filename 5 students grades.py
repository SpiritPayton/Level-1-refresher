"""Program to keep track of students marks and grades
"""


print("Hi, I am your English teacher. "
      "This is to record students' grades. "
      "If there are no more students to enter, "
      "type an 'X'")

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


results = [name, mark, grade]

def calc_grade():
    if mark < 40:
        grade = "E"
    elif mark < 50:
        grade = "D"
    elif mark < 55:
        grade = "C-"
    elif mark < 90:
        grade = "A"
    else:
        grade = "A+"

results.append
