import random

letters= ['a', 'b', 'c', 'd', 'e', 'f' 'g','h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers= [1,2,3,4,5,6,7,8,9,0]
symbols= ['!', '@', '#', '%', '^', '&', '*', '(', ')']

no_of_letters= int(input(print("Enter the number of letters")))
no_of_numbers= int(input(print("Enter the number of numbers")))
no_of_symbols= int(input(print("Enter the number of symbols")))


password= ''
if no_of_letters>0:
    for n in range(0, no_of_letters):
        password+=(random.choice("abcdefghikjlmnopqrstuvwxyz"))

if no_of_numbers>0:
    for n in range(0, no_of_numbers):
        password+=(random.choice("1234567890"))

if no_of_letters>0:
    for n in range(0, no_of_letters):
        password+=(random.choice("!@#$%^&*()"))

password_list= list(password)
random.shuffle(password_list)
password= ''.join(password_list)
print("Password: "+password)