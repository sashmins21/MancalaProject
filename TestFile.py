print("Herro")

def add_shapes():
    for x in range(28):
        shape = tk.Canvas(width=20, height=20)
        shape.create_arc(5, 5, 15, 15, fill="blue")  # Example shape (you can change it)
        shape.grid(row=0, column=x, padx=2, pady=2)

def move(row, col):
    for i in range(len(button_grid[row * 7 + col].cget("text"))):
        current_text = str(button_grid[row * 7 + col - i - 1].cget("text"))
        button_grid[row * 7 + col - i - 1].config(text=current_text + "O")
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
