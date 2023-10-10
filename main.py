import tkinter as tk

# Create the main tkinter window
root = tk.Tk()
root.title("Pallanguzhi")

rows = 2
cols = 7
button_grid = []

for i in range(rows):
    row_buttons = []
    for j in range(cols):
        button = tk.Button(root, text="", height=5, width=5)
        button.grid(row=i, column=j, padx=5, pady=5)
        row_buttons.append(button)
    button_grid.append(row_buttons)

# Initialize tkinter window with dimensions 650 x 500
root.geometry('650x500')

# Creating a Button
btn = tk.Button(root, text="Store", height=4, width=20)
btn2 = tk.Button(root, text="Store", height=4, width=20)

btn.place(x=100, y=210)
btn2.place(x=325, y=210)

# Start the tkinter main loop
root.mainloop()