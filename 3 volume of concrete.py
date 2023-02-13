"""program to calculate the volume of concrete needed for each job and the total needed for all jobs on a day
"""

# initialise variables

final_amount = 0
commercial = 0.5
residential = 0.25
total_cubic = 0


# input first number
while True:

    value = str(input("Enter '1' for commercial, '2' for residential: "))
    if value == "1":
        print("you chose commercial!!!!!!!!!!!!!!!!!!!!!!!!")
        length = int(input("Enter the length of the slab: "))
        width = int(input("Enter the width of the slab: "))
        total_cubic = length * width * commercial
        print(total_cubic)
        final_amount = final_amount + total_cubic

    elif value == "2":
        print("you chose residential!!!!!!!!!!!!!!!!!!!!!!!!")
        length = int(input("Enter the length of the slab: "))
        width = int(input("Enter the width of the slab: "))
        total_cubic = length * width * residential
        print(total_cubic)
        final_amount = final_amount + total_cubic

    elif value == "X":
        print("total concrete needed: ", final_amount)
        break
