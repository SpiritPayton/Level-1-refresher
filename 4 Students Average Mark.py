"""Program to keep track of students marks and grades
"""

student_name = []
student_score = []

print("Hi, I am your English teacher. "
      "This is to record students' grades. "
      "If there are no more students to enter, "
      "type an 'X'")

# input first number
while True:

    value = str(input("Enter student name: "))
    if type(value) == str and value != "X":
        print("You entered student named: ", value)
        exam_mark = int(input("What is their exam mark?: "))
        if exam_mark >= 0 and exam_mark <= 100:
            student_name.append([value])
            student_score.append([exam_mark])

        else:
            print("enter a valid score")
    elif value == "X":
        top_score = max(student_score)
        index = student_score.index(top_score)
        print("Best Student", *student_name[index], "With score", *student_score[index])
        break
