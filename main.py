import tkinter as tk

# Create the main tkinter window
root = tk.Tk()
root.title("Pallanguzhi")

rows = 2
cols = 7
button_grid = []

# Define a function to create a rectangle shape on a canvas
def create_rectangle_shape(canvas):
    canvas.create_rectangle(5, 5, 35, 35, fill="blue")  # Create a blue rectangle

for i in range(rows):
    row_buttons = []
    for j in range(cols):
        button = tk.Button(root, text="", height=40, width=40)
        button.grid(row=i, column=j, padx=5, pady=5)
        canvas = tk.Canvas(button, width=40, height=40)
        canvas.pack()
        create_rectangle_shape(canvas)  # Create the same rectangle shape on each button
        row_buttons.append(button)
    button_grid.append(row_buttons)

# Initialize tkinter window with dimensions 800 x 400
root.geometry('800x400')

# Creating a Button
btn = tk.Button(root, text="Store", height=4, width=20)
btn2 = tk.Button(root, text="Store", height=4, width=20)

btn.place(x=100, y=310)
btn2.place(x=425, y=310)

# Start the tkinter main loop
root.mainloop()
