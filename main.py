import tkinter as tk

# Create the main tkinter window
root = tk.Tk()
root.title("Pallanguzhi")

rows = 2
cols = 7
button_grid = []

# Define a function to add 4 shapes to a button
def add_shapes(button):
    for _ in range(4):
        shape = tk.Canvas(button, width=20, height=20)
        shape.create_arc(5, 5, 15, 15, fill="blue")  # Example shape (you can change it)
        shape.grid(row=0, column=_, padx=2, pady=2)

for i in range(rows):
    row_buttons = []
    for j in range(cols):
        button = tk.Button(root, text="", height=5, width=5)
        button.grid(row=i, column=j, padx=5, pady=5)
        add_shapes(button)  # Add 4 shapes to each button
        row_buttons.append(button)
    button_grid.append(row_buttons)

# Initialize tkinter window with dimensions 650 x 500
root.geometry('650x500')

# Creating two Button labels on the canvas
btn = tk.Button(root, text="Button 1", height=4, width=20)
btn2 = tk.Button(root, text="Button 2", height=4, width=20)

btn.place(x=100, y=400)
btn2.place(x=325, y=400)

# Start the tkinter main loop
root.mainloop()
