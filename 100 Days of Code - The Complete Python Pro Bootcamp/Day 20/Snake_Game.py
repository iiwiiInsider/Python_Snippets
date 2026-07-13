from turtle import Turtle, Screen
import time
import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

SCREEN_SIZE = 600
BOUNDARY = SCREEN_SIZE // 2 - 10


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_position = 0
        for _ in range(4):
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.goto(x_position, 0)
            self.segments.append(square)
            x_position -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        tail = self.segments[-1]
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(tail.xcor(), tail.ycor())
        self.segments.append(new_seg)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.refresh()

    def refresh(self):
        x = random.randint(-BOUNDARY + 20, BOUNDARY - 20)
        y = random.randint(-BOUNDARY + 20, BOUNDARY - 20)
        self.goto(x, y)


def show_start_popup():
    popup = Turtle()
    popup.hideturtle()
    popup.color("white")
    popup.write(
        "Press SPACE to Start",
        align="center",
        font=("Courier", 24, "bold")
    )
    return popup


def clear_popup(popup):
    popup.clear()


# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.tracer(0)

snake = Snake()
food = Food()

# Start popup
popup = show_start_popup()
game_started = False


def start_game():
    global game_started
    if not game_started:
        game_started = True
        clear_popup(popup)


screen.listen()
screen.onkey(start_game, "space")

# WASD controls
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

# Main game loop
while True:
    screen.update()
    time.sleep(0.1)

    if not game_started:
        continue

    snake.move()

    # Boundary collision
    x = snake.head.xcor()
    y = snake.head.ycor()
    if abs(x) > BOUNDARY or abs(y) > BOUNDARY:
        break

    # Food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()

    # Win condition (snake fills screen)
    if len(snake.segments) >= (SCREEN_SIZE // MOVE_DISTANCE) ** 2:
        break

screen.clear()
screen.bgcolor("black")
end = Turtle()
end.hideturtle()
end.color("white")
end.write("Game Over", align="center", font=("Courier", 32, "bold"))

screen.exitonclick()
