print("Herro")

def add_shapes():
    for x in range(28):
        shape = tk.Canvas(width=20, height=20)
        shape.create_arc(5, 5, 15, 15, fill="blue")  # Example shape (you can change it)
        shape.grid(row=0, column=x, padx=2, pady=2)
