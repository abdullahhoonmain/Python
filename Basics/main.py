# from datetime import datetime
import random
import selenium

          #calculator#
# print("enter a")
# a= int(input())
# print("enter b")
# b= int(input())
# print("enter operator")
# oper= input()
# if oper=='+':
#     result=a+b
# elif oper=='-':
#     reslt=a-b
# elif oper=='*':
#     result=a*b
# elif oper=='/':
#     if b==0:
#         result=0
#     else:
#      result=a/b
#
#
# else: print("not correct operator")
#
# print (result)
#
      #typecasting#
# x= int(input("enter x"))
# y = int(input("enter y"))
# z= (input("Enter z"))

      #current time#
# time1= datetime.now().strftime("%H")
# print(time1)

      #greater and smaller
# x= 10
# y=5
# match (x,y):
#     case(x,y) if x>y:
#         print("x is greater")
#     case(x,y) if x==y:
#         print("x is equal to y")
#     case(x,y) if y>x:
#         print("y is greater")
#     case _:
#         print("invalid values")

        #for loop
# we= "weeeeeeeee"
# c=0
# for x in we:
#     print(x)
#     c=c+1
# print(c)

       #for range
# for x in range(8):
#     print(x-3)
#     if x==2:
#         continue

        #even odd
# numbers= [1,2,3,4,5,6,7,8,9,11,12,1,31,414,1,4]
# for i in numbers:
#     if i%2==0:
#         print(str(i) + " is even")
#     else:
#         continue

        #randomization
# randomnumber= random.randint(1,20)
# print(randomnumber)
#
       #head tails
# randomfloat= random.random()
# if randomnumber%2==0:
#     print("heads")
# else:
#     print("Tails")
# print(randomfloat)

            #average height
#
# students_height= input("enter the heights of student seperted by space\n").split()
# for n in range(0, len(students_height)):
#     students_height[n]= int(students_height[n])
#     print(students_height[n])
#
# studentsum=0
#
# for student in range(0, len(students_height)):
#     studentsum= studentsum+students_height[student]
#
# avgheight= studentsum/len(students_height)
# print(avgheight)

       # defining function#
#
# def greet():
#     name= input("Enter your name:")
#     print("hello "+ name+ "!")
#
#
# greet()

                       #Sets#
# s1=,2,3}
# s2= {3,4,5}
# #print(s1.union(s2))
# print(s1.update(s2)) {1


                    #exception handling#
# try:
#     a= int(input("Enter a digit: "))
#     ab= [1,2,3,4]
#     print(ab[a])
# except ValueError:
#     print("input is not integer")
# except IndexError:
#     print('index out of range')


                    # Lambda function
                    # one line functions.
# name= lambda name: print(f"hello! {name}")
# sum= lambda x,y: print(x+y)
#
# name("Abdullah")
# sum(3,5)

                    #reduce, map and filter
# mylist= [12,4,5,7,9,5,2]
# cube= lambda x: x*x*x
# print(list(map(cube, mylist)))


#mylist2= [2,3,5,6,7,8,9,4,1,3]
# def notsmallerthan50(x):
#     return (x*x*x)>100
# newlist= list(map(lambda x: x*x*x, mylist2))
# recentlist=list(filter(notsmallerthan50, newlist))
# print(recentlist)


#                           #Decorators
# def greet(fx):
#     def mfx(*args, **kwargs):
#         #*awargs for tuple element and **kwargs for dictionary elements
#         print("Good morning")
#         fx(*args, **kwargs)
#         print("Good Bye")
#     return mfx()
# @greet
# def hello():
#     print("Hello i am here")
#
# def sum(a,b):
#     print(a+b)

                                  # Rock paper sissors
try:
    inp= int(input("Enter 1 for ROCK, 2 for PAPER and 3 for SICCOSRS:\n"))
    if inp<1 or inp>3:
        print("Value is not between 1 and 3")
        exit(0)

    rand = random.randint(1, 3)
    if inp == 1 and rand == 1 or inp == 2 and rand == 2 or inp == 3 and rand == 3:
        print("Draw!")
    elif inp == 1 and rand == 2 or inp == 2 and rand == 3 or inp == 3 and rand == 1:
        print("Computer wins!")
    elif inp == 2 and rand == 1 or inp == 3 and rand == 2 or inp == 1 and rand == 3:
        print("You won!")

    if inp == 1:
        print("You: Rock")
    elif inp == 2:
        print("You: Paper")
    elif inp == 3:
        print("You: Scissors")
    if rand == 1:
        print("Computer: Rock")
    elif rand == 2:
        print("Computer: Paper")
    elif rand == 3:
        print("Computer: Scissors")


except ValueError:
    print("Value is not between 1 and 3")
