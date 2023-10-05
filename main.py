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

bank = tk.Button(root, text="Bank", height=5, width=10)

# Start the tkinter main loop
root.mainloop()