import os

arr_classes = []

arr_grades = []

num_of_classes = int(input("How many classes are you taking? "))

os.system('cls')

number = 1

total = 0

gpa = 0

placement = ["High Honor Roll", "'A' Honor Roll", "'B' Honor Roll", "Sorry you are ineligible because you got an F for one of your classes","Sorry your grades did not qualify you for any of the honor positions"]

eligible = True

for classes in range(num_of_classes):
    classes = input(f"What is your class {number} name? ")
    arr_classes.append(classes)
    os.system("cls")
    number += 1


for grades in range(num_of_classes):
    grades = input(f"What is your letter grade in {arr_classes[grades]}? ").upper()
    arr_grades.append(grades)




for grade in arr_grades:
    if grade == 'A':
        total += 4
    elif grade == 'B':
        total += 3
    elif grade == 'C':
        total += 2
    elif grade == 'D':
        total += 1
    else:
        eligible = False
        break


gpa = total / num_of_classes


if eligible:
    if gpa > 3.8:
        placement = f"Congrats you made the {placement[0]}"
    elif gpa >= 3.5:
        placement = f"Congrats you made the {placement[1]}"
    elif gpa >= 3.25:
        placement = f"Congrats you made the {placement[2]}"
    else:
        placement = placement[4]
else:
    placement = "Since you got an F in one of your classes you are ineligible to be placed in any honor ranks."

os.system('cls')

print("\tReport Card")
for i in range(num_of_classes):
    print(f"{arr_classes[i]}:   {arr_grades[i]}")
print()
print(f"Your gpa is {gpa}")
print(placement)

