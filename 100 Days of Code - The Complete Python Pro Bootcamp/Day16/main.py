# # import another_module
# # print(another_module.another_variable)
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("Blue")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# formats in ASCII
from prettytable import PrettyTable
table = PrettyTable()

# 2. Define the columns (headers)
table.field_names = ["Pokemon", "Type",]

# 3. Add rows of data
table.add_row(["Pickachu", "Electric"])
table.add_row(["Charmander", "Fire"])
table.add_row(["Squirtle", "Water"])




print(table)