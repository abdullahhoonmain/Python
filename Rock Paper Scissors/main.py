import random
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
