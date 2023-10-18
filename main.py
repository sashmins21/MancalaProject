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

def move(row,col):
    num_buttons = 14
    current_index = row * cols + col
    num_Os = len(button_grid[current_index].cget("text"))

    for i in range(num_Os):
        current_text = str(button_grid[(current_index + i + 1) % num_buttons].cget("text"))
        button_grid[(current_index + i + 1) % num_buttons].config(text=current_text + "O")
        if i == len(button_grid[row * 7 + col].cget("text")) - 1:
            next_index = row * 7 + col - i
            if next_index % 7 != 6 and len(button_grid[next_index + 1].cget("text")) == 0:
                prev_index = row * 7 + col - i - 1
                while prev_index != next_index:
                    current_text = str(button_grid[prev_index].cget("text"))
                    btn_text = str(btn.cget("text"))
                    btn.config(text=btn_text + current_text)
                    button_grid[prev_index].config(text="")
                    prev_index = (prev_index - 1) % 14  # Wrap around the grid
    button_grid[row * 7 + col].config(text="")







# Start the tkinter main loop
root.mainloop()
