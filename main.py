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

for i in range(14):
    btn = button_grid[i]
    btn.place(x=210, y=210)


# Initialize tkinter window with dimensions 300 x 250
root.geometry('500x500')

# Creating a Button
btn = tk.Button(root, text="Store", height = 4, width=20)

# Set the position of button to coordinate (100, 20)
btn.place(x=210, y=210)



# Start the tkinter main loop
root.mainloop()