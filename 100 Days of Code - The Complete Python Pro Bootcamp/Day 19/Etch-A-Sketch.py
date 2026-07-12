from turtle import Turtle, Screen

# Create a Etch-A-Sketch App
def App():
    screen = Screen()
    screen.title("Etch-A-Sketch")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)

    # Create a turtle for drawing
    drawer = Turtle()
    drawer.speed(0)
    drawer.color("white")
    drawer.pensize(2)

    # Define movement functions
    def move_forward():
        drawer.forward(10)

    def move_backward():
        drawer.backward(10)

    def turn_left():
        drawer.left(15)

    def turn_right():
        drawer.right(15)

    def clear_screen():
        drawer.clear()

    # Bind keys to movement functions
    screen.listen()
    screen.onkey(move_forward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear_screen, "c")

    # Keep the window open until closed by the user
    screen.mainloop()

App()

