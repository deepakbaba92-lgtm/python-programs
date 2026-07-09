# 50 + 70 ka addition print karo.

print(50+70)
print(10+20)

# 100 + 250 ka addition print karo.
print(100+250)
# print(a + b)

# Variables use karke addition karo.

a = 15
b = 25

sum = a + b
print(sum)

# User se 2 numbers lekar addition print karo.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

sum = a + b
print(sum)

# User se 3 numbers lekar addition print karo.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

print(a + b + c)

# Decimal numbers ka addition karo user se input le kr.
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

# print(a + b)

# Negative numbers ka addition karo.
a = -10
b = 40

# print(a + b)

# Addition ko 20 + 30 = 50 format me print karo.
a = 20
b = 30

print(f"{a} + {b} = {a+b}")


# Function bana kar addition karo.

def add(a, b):
    return a + b
print(add(10, 20))

# Do variables ka sum ek teesre variable me store karo.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

sum = a + b
print("Addition =", sum)

# Calculator ka sirf addition feature banao.



# # Addition Concepts

# # Addition Program (Hardcoded Values)
# # Variables ke saath Addition
# # User Input se Addition
# # int() aur float() ka use
# # Output Formatting (print, comma, f-string)
# # Addition of 3 Numbers
# # Addition Function



count = int(input("How many numbers do you want to add? "))

total = 0

for i in range(1, count + 1):
    num = int(input(f"Enter Number {i}: "))
    total = total + num

print("Total =", total)