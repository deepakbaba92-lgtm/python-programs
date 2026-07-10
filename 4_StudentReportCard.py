print("========== STUDENT REPORT CARD ==========\n")

# Student Details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

print("\nEnter Marks (Out of 100)\n")

# Subject Marks
maths = float(input("Maths: "))
science = float(input("Science: "))
english = float(input("English: "))
hindi = float(input("Hindi: "))
computer = float(input("Computer: "))
social = float(input("Social Science: "))

# Total and Percentage
total = maths + science + english + hindi + computer + social
percentage = (total / 600) * 100

# Pass / Fail Check
if (maths < 33 or science < 33 or english < 33 or
    hindi < 33 or computer < 33 or social < 33):
    result = "FAIL"
    grade = "F"
    division = "No Division"

else:
    result = "PASS"

    # Grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    # Division
    if percentage >= 60:
        division = "First Division"
    elif percentage >= 45:
        division = "Second Division"
    elif percentage >= 33:
        division = "Third Division"
    else:
        division = "No Division"

# Report Card
print("\n========== REPORT CARD ==========")

print("Name             :", name)
print("Roll Number      :", roll_no)

print("\n----- Subject Marks -----")

print("Maths            :", maths)
print("Science          :", science)
print("English          :", english)
print("Hindi            :", hindi)
print("Computer         :", computer)
print("Social Science   :", social)

print("-------------------------------")
print("Total Marks      :", total, "/ 600")
print(f"Percentage       : {percentage:.2f}%")
print("Grade            :", grade)
print("Division         :", division)
print("Result           :", result)

print("================================")