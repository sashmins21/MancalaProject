import tkinter as tk

# Create the main tkinter window
root = tk.Tk()
root.title("Pallanguzhi")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

rows = 2
cols = 7
button_grid = []

# Define a function to add 4 shapes to a button
def add_shapes(button):
    for _ in range(4):
        shape = tk.Canvas(button, width=20, height=20)
        shape.create_rectangle(5, 5, 15, 15, fill="blue")  # Example shape (you can change it)
        shape.pack(side="left")

for i in range(rows):
    row_buttons = []
    for j in range(cols):
        button = tk.Button(root, text="B B B B", height=5, width=5)
        button.grid(row=i, column=j, padx=5, pady=5)
        add_shapes(button)  # Add 4 shapes to each button
        row_buttons.append(button)
    button_grid.append(row_buttons)



# Initialize tkinter window with dimensions 650 x 500
root.geometry('650x500')

# Creating a Button
btn = tk.Button(root, text="", height=4, width=20)
btn2 = tk.Button(root, text="", height=4, width=20)

btn.place(x=100, y=210)
btn2.place(x=325, y=210)

# Start the tkinter main loop
root.mainloop()
