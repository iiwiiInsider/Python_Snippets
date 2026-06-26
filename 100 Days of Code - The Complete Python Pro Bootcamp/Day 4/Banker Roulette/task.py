import random
Friends = ["Rachel", "Phoebe", "Ross", "Chandler", "Monica", "Joey"]

# Option 1
random_string = random.choice(Friends)
print(random_string)

# 2nd option

random_index = random.randint(0, len(Friends) - 1)
print(Friends[random_index])
