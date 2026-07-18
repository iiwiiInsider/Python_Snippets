import turtle
import pandas

# --- Setup screen ---
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)

# Load your map GIF (must be in same folder)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# --- Read CSV ---
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# --- Turtle for writing text ---
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

guessed_states = []

# --- Game Loop ---
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Guess a state's name:"
    )

    if answer_state is None:
        break  # user closed the window

    answer_state = answer_state.title()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Get coordinates from CSV
        state_data = data[data.state == answer_state]
        x = int(state_data["x"].iloc[0])
        y = int(state_data["y"].iloc[0])

        # Write state name on map
        writer.goto(x, y)
        writer.write(answer_state, align="center", font=("Arial", 10, "bold"))

# --- End of game ---
turtle.mainloop()
