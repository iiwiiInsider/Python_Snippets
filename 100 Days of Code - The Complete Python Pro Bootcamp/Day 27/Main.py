import tkinter as tk

# Conversion formulas stored in a dictionary
CONVERSIONS = {
    "Distance": {
        "Miles → Kilometers": lambda x: x * 1.60934,
        "Kilometers → Miles": lambda x: x / 1.60934,
        "Feet → Meters": lambda x: x * 0.3048,
        "Meters → Feet": lambda x: x / 0.3048,
        "Inches → Centimeters": lambda x: x * 2.54,
        "Centimeters → Inches": lambda x: x / 2.54,

        # Millimeters
        "Millimeters → Centimeters": lambda x: x / 10,
        "Centimeters → Millimeters": lambda x: x * 10,
        "Millimeters → Meters": lambda x: x / 1000,
        "Meters → Millimeters": lambda x: x * 1000
    },

    "Weight": {
        "Pounds → Kilograms": lambda x: x * 0.453592,
        "Kilograms → Pounds": lambda x: x / 0.453592,
        "Ounces → Grams": lambda x: x * 28.3495,
        "Grams → Ounces": lambda x: x / 28.3495,

        # Metric Ton (Tonne)
        "Kilograms → Metric Tons": lambda x: x / 1000,
        "Metric Tons → Kilograms": lambda x: x * 1000,

        # US Short Ton
        "Pounds → US Tons": lambda x: x / 2000,
        "US Tons → Pounds": lambda x: x * 2000
    },

    "Volume": {
        "Liters → Milliliters": lambda x: x * 1000,
        "Milliliters → Liters": lambda x: x / 1000,
        "Gallons → Liters": lambda x: x * 3.78541,
        "Liters → Gallons": lambda x: x / 3.78541
    },

    "Temperature": {
        "Celsius → Fahrenheit": lambda x: (x * 9/5) + 32,
        "Fahrenheit → Celsius": lambda x: (x - 32) * 5/9,
        "Celsius → Kelvin": lambda x: x + 273.15,
        "Kelvin → Celsius": lambda x: x - 273.15
    },

    "Speed": {
        "MPH → KPH": lambda x: x * 1.60934,
        "KPH → MPH": lambda x: x / 1.60934
    }
}

def update_conversion_options(*args):
    """Update the second dropdown based on category selection."""
    category = category_var.get()
    conversion_menu["menu"].delete(0, "end")

    for conv in CONVERSIONS[category]:
        conversion_menu["menu"].add_command(
            label=conv,
            command=lambda value=conv: conversion_var.set(value)
        )

    conversion_var.set(list(CONVERSIONS[category].keys())[0])

def convert():
    """Perform the selected conversion."""
    try:
        value = float(entry_value.get())
    except ValueError:
        label_result.config(text="Invalid input")
        return

    category = category_var.get()
    conversion = conversion_var.get()

    result = CONVERSIONS[category][conversion](value)
    label_result.config(text=f"{result:.4f}")

# Main window
root = tk.Tk()
root.title("Universal Unit Converter")
root.geometry("500x500")

# Center frame
center_frame = tk.Frame(root)
center_frame.pack(expand=True)

# Category dropdown
category_var = tk.StringVar(value="Distance")
category_label = tk.Label(center_frame, text="Select Category:", font=("Arial", 14))
category_label.pack(pady=5)

category_menu = tk.OptionMenu(center_frame, category_var, *CONVERSIONS.keys())
category_menu.config(font=("Arial", 12))
category_menu.pack(pady=10)

# Conversion dropdown
conversion_var = tk.StringVar()
conversion_label = tk.Label(center_frame, text="Select Conversion:", font=("Arial", 14))
conversion_label.pack(pady=5)

conversion_menu = tk.OptionMenu(center_frame, conversion_var, "")
conversion_menu.config(font=("Arial", 12))
conversion_menu.pack(pady=10)

# Initialize conversion dropdown
update_conversion_options()
category_var.trace("w", update_conversion_options)

# Entry field
entry_value = tk.Entry(center_frame, width=10, font=("Arial", 14))
entry_value.pack(pady=10)

# Result label
label_result = tk.Label(center_frame, text="Result appears here", font=("Arial", 16))
label_result.pack(pady=10)

# Convert button
btn_convert = tk.Button(center_frame, text="Convert", command=convert, font=("Arial", 14))
btn_convert.pack(pady=10)

root.mainloop()
