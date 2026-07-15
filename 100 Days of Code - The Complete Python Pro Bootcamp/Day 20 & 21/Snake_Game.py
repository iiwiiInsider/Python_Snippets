import turtle
import time
import random
import os

# ==========================
#   HIGH SCORE HANDLING
# ==========================
HIGHSCORE_FILE = "snake_highscore.txt"

def load_highscore():
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    with open(HIGHSCORE_FILE, "r") as f:
        return int(f.read().strip())

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score))

# ==========================
#   SETUP SCREEN
# ==========================
screen = turtle.Screen()
screen.title("Snake Game (Turtle Version)")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# ==========================
#   SNAKE HEAD
# ==========================
head = turtle.Turtle()
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ==========================
#   FOOD
# ==========================
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# ==========================
#   SCORE DISPLAY
# ==========================
score = 0
highscore = load_highscore()

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write(f"Score: {score}  High Score: {highscore}", align="center", font=("Courier", 24, "normal"))

# ==========================
#   MOVEMENT FUNCTIONS
# ==========================
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)
    elif head.direction == "down":
        head.sety(y - 20)
    elif head.direction == "left":
        head.setx(x - 20)
    elif head.direction == "right":
        head.setx(x + 20)

# ==========================
#   KEYBOARD BINDINGS
# ==========================
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# ==========================
#   STARTING SEGMENTS (3 SQUARES TOTAL)
# ==========================
segments = []

for i in range(2):
    seg = turtle.Turtle()
    seg.shape("square")
    seg.color("green")
    seg.penup()
    seg.goto(head.xcor() - ((i + 1) * 20), head.ycor())
    segments.append(seg)

# ==========================
#   MAIN GAME LOOP
# ==========================
def game_loop():
    global score, highscore

    screen.update()

    # Wall collision
    if (head.xcor() > 280 or head.xcor() < -280 or
        head.ycor() > 280 or head.ycor() < -280):
        reset_game()

    # Food collision
    if head.distance(food) < 20:
        score += 1

        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

    # Move tail segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Tail collision
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    pen.clear()
    pen.write(f"Score: {score}  High Score: {highscore}", align="center", font=("Courier", 24, "normal"))

    screen.ontimer(game_loop, 100)

# ==========================
#   RESET GAME
# ==========================
def reset_game():
    global score, highscore

    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    # Recreate starting segments
    for i in range(2):
        seg = turtle.Turtle()
        seg.shape("square")
        seg.color("green")
        seg.penup()
        seg.goto(head.xcor() - ((i + 1) * 20), head.ycor())
        segments.append(seg)

    if score > highscore:
        highscore = score
        save_highscore(highscore)

    score = 0

# ==========================
#   START GAME
# ==========================
game_loop()
screen.mainloop()
