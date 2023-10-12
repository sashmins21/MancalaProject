import tkinter as tk

# Create the main tkinter window
root = tk.Tk()
root.title("Pallanguzhi")

rows = 2
cols = 7
button_grid = []

# Define a function to add 4 shapes to a button
seeds = 4


def create_button(row,col):
    button = tk.Button(root, text="B B B B", height=5, width=5, command=lambda:move(row, col))
    button.grid(row=row, column=col, padx=5, pady=5)
    button_grid.append(button)

for i in range(2):
    for j in range(7):
        create_button(i,j)

root.geometry('650x500')

# Creating two Button labels on the canvas
btn = tk.Button(root, text="Button 1", height=4, width=20)
btn2 = tk.Button(root, text="Button 2", height=4, width=20)

btn.place(x=100, y=200)
btn2.place(x=325, y=200)

def move(row, col):
    button_grid[row * 7 + col].config(text="")
    for i in range(seeds):
        current_text = str(button_grid[row*7 +col-i-1].cget("text")) # FIX THIS
        button_grid[row*7 + col-i-1].config(text =current_text + " B")


# Start the tkinter main loop
root.mainloop()
