import tkinter as tk
import json
import random
import string
from tkinter import messagebox

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ---------------- GLOBAL STATE ---------------- #
last_email = ""


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


# ---------------- SAVE TO JSON ---------------- #
def save_to_json():
    global last_email

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill in all fields before saving.")
        return

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

    last_email = email

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    email_entry.delete(0, tk.END)
    email_entry.insert(0, last_email)


# ---------------- SEARCH FUNCTION ---------------- #
def search_website():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Please enter a website to search.")
        return

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]

        email_entry.delete(0, tk.END)
        email_entry.insert(0, email)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        messagebox.showinfo(title="Success", message=f"Details found for {website}")
    else:
        messagebox.showinfo(title="Not Found", message=f"No details found for {website}")


# ---------------- UI SETUP ---------------- #

canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
tk.Label(text="Website:").grid(row=1, column=0, sticky="e")
tk.Label(text="Email/Username:").grid(row=2, column=0, sticky="e")
tk.Label(text="Password:").grid(row=3, column=0, sticky="e")

# Entries
website_entry = tk.Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")

email_entry = tk.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = tk.Entry(width=22)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
tk.Button(text="Search", width=15, command=search_website).grid(row=1, column=2, sticky="e")
tk.Button(text="Generate Password", command=generate_password).grid(row=3, column=2, sticky="w")
tk.Button(text="Save", width=36, command=save_to_json).grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
