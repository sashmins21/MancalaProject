import tkinter as tk
import time

# Create the main tkinter window
root = tk.Tk()
root.title("Pallanguzhi")

rows = 2
cols = 7
button_grid = []

# Define a function to add 4 shapes to a button
seeds = 4


def create_button(row,col):
    button = tk.Button(root, text="OOOO", height=5, width=5, command=lambda:move(row, col))
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
    for i in range(len(button_grid[row * 7 + col].cget("text"))):
        current_text = str(button_grid[row * 7 + col - i - 1].cget("text"))
        button_grid[row * 7 + col - i - 1].config(text=current_text + "O")
        if i == len(button_grid[row * 7 + col].cget("text")) - 1:
            next_index = row * 7 + col - i
            if next_index % 7 != 6 and len(button_grid[next_index + 1].cget("text")) == 0:
                btn.config(text = "HERRO")
    button_grid[row * 7 + col].config(text="")






# Start the tkinter main loop
root.mainloop()
