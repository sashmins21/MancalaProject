import tkinter as tk

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

#this method creates the button
def create_button(row,col):
    button = tk.Button(root, text="OOOO", height=5, width=5, command=lambda:move(row, col))
    button.grid(row=row, column=col, padx=5, pady=5)
    button_grid.append(button)

#This for loop creates the 14 buttons in a 2x7 grid
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

#main move method that transports the O's to the next pits and highlights which pit should be clicked next
def move(row, col):
    num_buttons = 14
    current_index = row * cols + col
    num_Os = len(button_grid[current_index].cget("text"))

    for i in range(num_Os): #This for loop runs for the amount of O's in the pit and puts them in the other pits
        next_index = (current_index + i + 1) % num_buttons
        current_text = str(button_grid[next_index].cget("text"))
        button_grid[next_index].config(text=current_text + "O")

    next_button_index = (current_index + num_Os + 1) % num_buttons
    button_grid[next_button_index].config(fg='red')
    button_grid[current_index].config(text="")
    button_grid[current_index].config(fg='black')


def increment_score(event): #This adds one to the Player One score everytime 'p' is pressed
    global score
    score += 1
    btn.config(text=f"Player 1 Score: {score}")

# Bind the 'q' key event to the increment_score function
root.bind('q', increment_score)

def increment_score(event): #This adds one to the Player Two score everytime 'q' is pressed
    global score2
    score2 += 1
    btn2.config(text=f"Player 2 Score: {score2}")

# Bind the 'T' key event to the increment_score function
root.bind('p', increment_score)

def switch_player(): #This changes the player indicator on the button when a pit is cleared
    global current_player
    if current_player == 1: #switches the player turn using either 1 and 2 and switches between the two.
        btn3.config(text="Player 2 Turn")
        current_player = 2
    else:
        btn3.config(text="Player 1 Turn")
        current_player = 1

def key_press(a): #takes in the number pressed and clears the pit
    button_grid[int(a.char)].config(text="")
    for i in range(14): #makes sure everything is black after the pit clears
        button_grid[i].config(fg='black')
    switch_player()

for i in range(10): #Binded the key buttons to the row of numbers
    root.bind(str(i), key_press)

def change_letter(a): #This method clears the certain pit (index 10-13)
    if(a.char == 'z'): #assigns the 'z' key with index 10
        button_grid[10].config(text="")
        for i in range(14): #makes sure everything is black after the pit clears
            button_grid[i].config(fg='black')
        switch_player()
    if (a.char == 'x'): #assigns the 'x' key with index 11
        button_grid[11].config(text="")
        for i in range(14): #makes sure everything is black after the pit clears
            button_grid[i].config(fg='black')
        switch_player()
    if (a.char == 'c'): #assigns the 'c' key with index 12
        button_grid[12].config(text="")
        for i in range(14): #makes sure everything is black after the pit clears
            button_grid[i].config(fg='black')
        switch_player()
    if (a.char == 'v'): #assigns the 'v' key with index 13
        button_grid[13].config(text="")
        for i in range(14): #makes sure everything is black after the pit clears
            button_grid[i].config(fg='black')
        switch_player()

root.bind('z', change_letter)
root.bind('x', change_letter)
root.bind('c', change_letter)
root.bind('v', change_letter)


# Start the tkinter main loop
root.mainloop()
