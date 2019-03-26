# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Assignment 1st
#Use of Operators

print("Enter your choice\n")

print("A. Calculator using Arithematic operators")
print("B. GradeSheet of a student using 'and' operator")
print("C. Find The Greatest no Between Two Nubmbers using 'comparison' operators")

Choice=str(input())

if(Choice=='A'):   #here i use comparision operator(==)
    print("Enter your choice\n")

    print("1. add")
    print("2. sub")
    print("3. mult")
    print("4. div")
    print("5. Mod")
    print("6. exponential")
    print("7. Floor Division")

    c=int(input())

    if(c==1):
        x = int(input("Enter first Value\n"))  # assignment operator to assign a value to a variable
        y = int(input("Enter second value\n"))
        add=x+y            #addition operator(+)
        print(add)

    elif(c==2):
        x = int(input("Enter first Value\n"))  # assignment operator to assign a value to a variable
        y = int(input("Enter second value\n"))
        sub=x-y            #subtraction operator(-)
        print(sub)

    elif(c==3):
        x = int(input("Enter first Value\n"))  # assignment operator to assign a value to a variable
        y = int(input("Enter second value\n"))
        mult=x*y           #multiplication operator(*)
        print(mult)

    elif(c==4):
        x = int(input("Enter first Value\n"))  # assignment operator to assign a value to a variable
        y = int(input("Enter second value\n"))
        div=x/y            #division operator(/)
        print(div)

    elif(c==5):
        x = int(input("Enter first Value\n"))  # assignment operator to assign a value to a variable
        y = int(input("Enter second value\n"))
        mod=x%y            #modulous operator(%)
        print(mod)
        
    elif(c==6):
        x=int(input("Enter First Value\n"))     # assignment operator to assign a value to a variable
        y=int(input("Enter second Value\n"))
        exp=x**y           #Exponential operator(**)
        print(exp)
        
    elif(c==7):
        x=int(input("Enter First Value\n"))      # assignment operator to assign a value to a variable
        y=int(input("Enter second Value\n"))
        flr=x//y           #Floor Division operator(//)
        print(flr)


    else:
        print("invalid choice")

elif(Choice=='B'):
    x=int(input("Enter the marks of student\n"))   #here we take the marks form user

    if(x<100 and x>90):                                #use of logical Operator
        print("pass with A grade")                     #     (and)
    elif(x<90 and x>80):
        print("pass with B grade")
    elif(x<80 and x>60):
        print("pass with C grade")
    elif(x<60 and x>50):
        print("pass with D grade")
    elif(x<50 and x>0):
        print("Fail")
    else:
        print("Invalid Marks")

elif(Choice=='C'):
    x = input("the value of x\n")                 #in this Block of code we use Comparision Operator("<,>")
    y = input("the value of y\n")

    if x > y:
        print("x is greater than y\n")

    elif y > x:
        print("y is greater than x\n")

    else:
        print("both are equal")
else:
    print("Invalid Choice!!!!")