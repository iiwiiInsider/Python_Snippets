print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))

    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age == 21:
        bill = 9
        print("Special tickets are $9.")
    elif age > 18:
        bill = 11
        print( "Adult tickets are $11.")

        wants_photo = input("Would you like a photo taken? (y/n) ")
        if wants_photo == "y":
            # Add 3$ to their bill
            bill += 3

        print(f"Your final bill is ${bill}.")

