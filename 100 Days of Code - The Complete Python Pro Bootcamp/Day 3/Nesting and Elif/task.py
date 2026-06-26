print("Welcome to the rollercoaster!")

age = int(input("What is your age?\n"))

if age <= 12:
    print("Please pay $5.")
elif age <= 18:
    print("Please pay $7.")
elif age == 21:
    print("Please pay $9.")
else:
    print("Please pay $11.")
