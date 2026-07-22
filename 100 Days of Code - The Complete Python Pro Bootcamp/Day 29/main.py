import tkinter as tk
import csv
import random
import string

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ---------------- GLOBAL STATE ---------------- #
last_email = ""   # Stores the most recently used email


# ---------------- PASSWORD GENERATOR ---------------- #
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()-_=+"

    password_chars = (
        random.choices(letters, k=6) +
        random.choices(digits, k=3) +
        random.choices(symbols, k=3)
    )

    random.shuffle(password_chars)
    password = "".join(password_chars)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ---------------- SAVE FUNCTION ---------------- #
def save_to_csv():
    global last_email

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        print("Please fill in all fields before saving.")
        return

    # Save to CSV in same directory
    with open("passwords.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([website, email, password])

    # Remember last email
    last_email = email

    # Clear fields after saving
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    # Repopulate email field
    email_entry.delete(0, tk.END)
    email_entry.insert(0, last_email)


# ---------------- UI SETUP ---------------- #

# Canvas
canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = tk.Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")

email_entry = tk.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = tk.Entry(width=22)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="w")

add_password_button = tk.Button(text="Save", width=36, command=save_to_csv)
add_password_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
