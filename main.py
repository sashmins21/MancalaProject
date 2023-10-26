import tkinter as tk
from tkinter import messagebox
# Create the main tkinter window
root = tk.Tk()
root.title("Pallanguzhi")

#instance variables
rows = 2
cols = 7
button_grid = []
score = 0
score2 = 0
current_player = 1

#Create a 2x7 grid
def create_button(row,col):
    button = tk.Button(root, text="OOOO", height=5, width=5, command=lambda:move(row, col))
    button.grid(row=row, column=col, padx=5, pady=5)
    button_grid.append(button)


for i in range(2):
    for j in range(7):
        create_button(i,j)

root.geometry('650x500')

# Creating three Button labels on the canvas
btn = tk.Button(root, text="Player 1", height=4, width=20)
btn2 = tk.Button(root, text="Player 2", height=4, width=20)
btn3 = tk.Button(root, text="Player 1 Turn", height=2, width=10)

btn.place(x=100, y=200)
btn2.place(x=325, y=200)
btn3.place(x=250, y=280)


def move(row, col):
    num_buttons = 14
    current_index = row * cols + col
    num_Os = len(button_grid[current_index].cget("text"))

    for i in range(num_Os):
        next_index = (current_index + i + 1) % num_buttons
        current_text = str(button_grid[next_index].cget("text"))
        button_grid[next_index].config(text=current_text + "O")

    next_button_index = (current_index + num_Os + 1) % num_buttons
    button_grid[next_button_index].config(fg='red')
    button_grid[current_index].config(text="")
    button_grid[current_index].config(fg='black')


def increment_score(event):
    global score
    score += 1
    btn.config(text=f"Player 1 Score: {score}")
    if score >= 28:
        messagebox.showinfo(title="Game Over", message="Player 1 WINS!")

# Bind the 'T' key event to the increment_score function
root.bind('q', increment_score)

def increment_score(event):
    global score2
    score2 += 1
    btn2.config(text=f"Player 2 Score: {score2}")
    if score2 >= 28:
        messagebox.showinfo(title="Game Over", message="Player 2 WINS!")
# Bind the 'T' key event to the increment_score function
root.bind('p', increment_score)

def switch_player():
    global current_player
    if current_player == 1:
        btn3.config(text="Player 2 Turn")
        current_player = 2
    else:
        btn3.config(text="Player 1 Turn")
        current_player = 1

def key_press(a):
    button_grid[int(a.char)].config(text="")
    for i in range(14):
        button_grid[i].config(fg='black')
    switch_player()


for i in range(10):
    root.bind(str(i), key_press)

def change_letter(a):
    if(a.char == 'z'):
        button_grid[10].config(text="")
        for i in range(14):
            button_grid[i].config(fg='black')
        switch_player()
    if (a.char == 'x'):
        button_grid[11].config(text="")
        for i in range(14):
            button_grid[i].config(fg='black')
        switch_player()
    if (a.char == 'c'):
        button_grid[12].config(text="")
        for i in range(14):
            button_grid[i].config(fg='black')
        switch_player()
    if (a.char == 'v'):
        button_grid[13].config(text="")
        for i in range(14):
            button_grid[i].config(fg='black')
        switch_player()

root.bind('z', change_letter)
root.bind('x', change_letter)
root.bind('c', change_letter)
root.bind('v', change_letter)


# Start the tkinter main loop
root.mainloop()
