from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"] # Listing Indexes starts from 0 so first variable in the range = 0
dice_num = randint(0, 5)
print(dice_images[dice_num])
