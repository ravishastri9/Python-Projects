"Program to find out bill of different pizza size"

print("Welcome to the Python Pizza Deliveries ")
size = input("What size would you like to order? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
    print("Small Pizza: $15")
elif size == "M":
    bill += 20
    print("Medium Pizza: $20")
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is {bill}")
