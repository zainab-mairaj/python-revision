# Day 2: Conditional statements practice
#Q1: Take a number and check if it is even or odd.
# Topics: if, elif, else, comparison operators
num1 = int(input("Enter a number: "))
if num1%2==0:
    print("EVEN")
else: 
    print("ODD")
#Q2: Take age and check: Minor, Adult, Senior
age = int(input("Enter age: "))
if age>=50:
    print("SENIOR")
elif age>=20:
    print("ADULT")
else:
    print("MINOR")
#Q3: Take marks and print grade.
marks = int(input("Enter your marks: "))
if marks>=80:
    print("A+ grade")
elif marks>=70:
    print("A grade")
elif marks>=60:
    print("B grade")
else:
    print("FAIL")
#Q4: Take password input and check if it matches "python123".
info = input("Enter your password: ")
if info=="python123":
    print("UNLOCKED, CORRECT PASSWORD")
else:
    print("WRONG PASSWORD!!")
#Q5: Check if a number is: positive, negative, zero
num2 = int(input("Enter any number: "))
if num2 == 0:
    print("The number is zero")
elif num2 > 0:
    print("The number is positive")
else:
    print("The number is negative")
