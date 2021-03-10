"A fun treasure game"

print("Welcome to treasure island")
print("Your mission is to find the treasure.")
choice1 = input('You are at a crossroad, where do you want to go? Type "left" or "right".\n').lower()


if choice1 == "left":

    choice2 = input('You have come to a lake. There is a island in the middle of lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
       choice3 = input("Which door you want to use? red, blue or yellow\n").lower()
       if choice3 == "yellow":
           print("You Win")
       else:
           print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")

