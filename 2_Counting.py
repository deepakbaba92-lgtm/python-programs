# 1. Maths counting print program 
print(1)
print(2)
print(3)
print(4)
print(5)

# 2. Counting program Using Variable

num = 1
print(num)

num = 2
print(num)

num = 3
print(num)

# 3. Counting program Using While Loop
num = 1

while num <= 20:
    print(num)
    num = num + 1

# 4. Counting program Using For Loop
for num in range(1, 21):
    print(num)

# 5. Counting program Using User Input
end = int(input("Kaha tk ki counting print krvani hai: "))

for num in range(1, end + 1):
    print(num)

# 6. Counting program Using Function
def counting():
    for num in range(1, 21):
        print(num)

counting()

# 7. Counting program Using Function +parameter
def counting(start, end):
    for num in range(start, end + 1):
        print(num)

counting(1, 20)

end = int(input("Kaha tk ki counting print krvani hai: "))

for num in range(-100, end + 1):
    print(num)

start= int(input("Kaha se counting print krvani hai: "))

end = int(input("Kaha tk ki counting print krvani hai: "))

for num in range(start, end + 1):
    print(num)


# Practice Set
# 1.	1 se 1000 tk counting print

for i in range(1, 1001):
    print(i)

# 1 → Starting Number
# 1001 → Ending Number + 1
# 1 → Default Increment

# 2.	1000 se 1 tk ki counting print

for i in range(1000, 0, -1):
    print(i)

# 1000 → Starting Number
# 0 → Stop Value (0 print nahi hoga)
# -1 → Har baar 1 kam hoga

# 3.	koi bhi number se counting print krna hai 500 tk

num = int(input("Enter Starting Number: "))

for i in range(num, 501):
    print(i)


# 4.	-100 se 100 tk ki counting print
for i in range(-100, 101):
    print(i)


#5. 500 se 50 tak counting print karo. //Reverse Counting

for i in range(500, 49, -1):
    print(i)