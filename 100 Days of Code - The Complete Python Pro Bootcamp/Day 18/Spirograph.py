from turtle import Turtle, Screen

import random_color

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

# Draw a Spirograph with a random color for each circle
def spirograph():
    timmy_the_turtle.speed("fastest")
    for _ in range(36):
        timmy_the_turtle.color(random_color.random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.right(10)

spirograph()

screen = Screen()
screen.exitonclick()