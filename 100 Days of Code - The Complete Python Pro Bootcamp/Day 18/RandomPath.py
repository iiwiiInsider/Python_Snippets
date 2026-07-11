import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

def path():
    timmy_the_turtle.pensize(10)
    timmy_the_turtle.speed("fastest")
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "brown"]
    directions = [0, 90, 180, 270]
    while True:
        timmy_the_turtle.color(random.choice(colors))
        timmy_the_turtle.setheading(random.choice(directions))
        timmy_the_turtle.forward(30)
        # Check if the turtle is out of bounds
        if not (-300 < timmy_the_turtle.xcor() < 300 and -300 < timmy_the_turtle.ycor() < 300):
            break
path()
screen = Screen()
screen.exitonclick()