from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create turtles
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

race_on = False

if user_bet:
    race_on = True

# Race loop
while race_on:
    for turtle in all_turtles:
        # Check if turtle reached finish line
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet.lower():
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost. The {winning_color} turtle won the race.")
        # Move turtle forward randomly
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
