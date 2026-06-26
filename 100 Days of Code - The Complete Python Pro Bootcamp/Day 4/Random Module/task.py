import random
import my_module

# random_integer = random.randint(1, 10)
# # print (random_integer)
#
# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)
#
# random_float = random.uniform(0, 10)
# print(random_float)

print("Welcome to the Heads or Tails Game!")
input("Press Enter to flip the coin...\n")
random_number = random.randint(1,2)
if random_number == 1:
    print("Heads")
else:
    print("Tails")
