try:
    user_age = int(input("How old are you?\n"))
except ValueError:
    print("Please enter a valid number.")
    exit()

if user_age >= 18:
    print(f"You can drive at age {user_age}.")
elif user_age <= 17:
    print("You are not old enough to drive yet.")


