import tkinter
import customtkinter
from tkinter import filedialog

# Function to calculate mill value
def calculate_mill():
    try:
        x = float(meters_var.get())
        if 100 <= x <= 1600:
            y = calculate_mill_value(x)
            output_label.configure(text=f"For a distance of {x} meters, the output is: {y}")
            save_recent_input(x)
        else:
            output_label.configure(text="Input is out of range. Please enter a distance between 100 and 1600 meters.")
    except ValueError:
        output_label.configure(text="Invalid input. Please enter a valid number.")

# Function to calculate mill value based on input
def calculate_mill_value(x):
    x1, y1 = 100, 978
    x2, y2 = 1600, 622
    y = y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)
    return y

# Function to save recent inputs to a file
def save_recent_input(input_value):
    with open("recent_inputs.txt", "a") as file:
        file.write(str(input_value) + "\n")

# Function to save recent inputs to a file via GUI
def save_recent_inputs_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            with open("recent_inputs.txt", "r") as recent_inputs_file:
                file.write(recent_inputs_file.read())

# Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Window
app = customtkinter.CTk()
app.geometry("600x350")
app.title("Arty Calculator")

# UI elements
title = customtkinter.CTkLabel(app, text="Insert meters to ping")
title.pack(padx=10, pady=10)

# Input
meters_var = tkinter.StringVar()
input_entry = customtkinter.CTkEntry(app, width=350, height=40, textvariable=meters_var)
input_entry.pack()

# Button
calculate_button = customtkinter.CTkButton(app, text="Calculate", command=calculate_mill)
calculate_button.pack(padx=10, pady=10)

# Output
output_label = customtkinter.CTkLabel(app, text="")
output_label.pack(padx=10, pady=10)

# Progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.pack(padx=10, pady=10)

# Save recent inputs button
save_recent_inputs_button = customtkinter.CTkButton(app, text="Show Recent Inputs", command= save_recent_input)
save_recent_inputs_button.pack(padx=10, pady=5)

# Save recent inputs to file button
save_recent_inputs_button = customtkinter.CTkButton(app, text="Save Recent Inputs to File", command=save_recent_inputs_to_file)
save_recent_inputs_button.pack(padx=10, pady=5)

# Loop
app.mainloop()
