from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and a decagon from a single point with each shape being a  different color
def multiShapeAndMultiColor():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "brown"]
    sides = [3, 4, 5, 6, 7, 8, 9,]
    for i in range(len(sides)):
        timmy_the_turtle.color(colors[i])
        for _ in range(sides[i]):
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(360 / sides[i])

multiShapeAndMultiColor()

screen = Screen()
screen.exitonclick()
