# Day 3: Loops practice (for & while)

#Q1: Print numbers from 1 to 10 using for loop.
for i in range(1,11):
   print(i)
#Q2: Print even numbers between 1 and 20.
for j in range(2, 20, 2):
    print(j)
#Q3: Take a number from user and print its multiplication table.
num = int(input("Enter a number: "))
k = 1

while k <= 10:
    print(num * k)
    k += 1

#Q4: Use while loop to print numbers from 10 to 1.
i = 10
while i >= 1:
    print(i)
    i -= 1
#Q5: Print this pattern:
#*
#**
#***
#****
#*****
for i in range(1,6):
    print("*" * i)

 
