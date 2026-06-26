print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

else:
    print("Sorry, please enter S, M, or L")
    exit()

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    elif size == "L":
        bill += 3
else:
    print("Sorry, please enter Y or N")
    exit()

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1
else:
    print("Sorry, please enter Y or N")
print(f"Your final bill is: ${bill}.")