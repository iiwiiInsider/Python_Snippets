import turtle
import time

# --- Screen Setup ---
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# --- Score ---
score_a = 0
score_b = 0

# --- Pause flag ---
paused = True   # start paused so game waits for click

# --- Paddle A ---
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# --- Paddle B ---
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# --- Ball ---
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Slower ball speed
ball.dx = 0.10
ball.dy = 0.10

# --- Scoreboard ---
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 24, "normal"))

# --- Start/Pause Message ---
message = turtle.Turtle()
message.speed(0)
message.color("yellow")
message.penup()
message.hideturtle()
message.goto(0, 0)
message.write("CLICK TO START", align="center", font=("Courier", 28, "bold"))

# --- Click to Start Function ---
def start_game(x=None, y=None):
    global paused
    paused = False
    message.clear()

wn.onclick(start_game)

# --- Paddle Movement ---
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 40)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        paddle_a.sety(y - 40)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 40)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        paddle_b.sety(y - 40)

# --- Keyboard Bindings ---
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# --- Main Game Loop ---
while True:
    wn.update()

    # Skip movement if paused
    if paused:
        continue

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right side (Player A scores)
    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A: {score_a}    Player B: {score_b}",
                  align="center", font=("Courier", 24, "normal"))

        paused = True
        message.write("CLICK TO RESUME", align="center", font=("Courier", 28, "bold"))

    # Left side (Player B scores)
    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A: {score_a}    Player B: {score_b}",
                  align="center", font=("Courier", 24, "normal"))

        paused = True
        message.write("CLICK TO RESUME", align="center", font=("Courier", 28, "bold"))

    # Paddle collisions
    if (340 < ball.xcor() < 350) and \
       (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and \
       (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
