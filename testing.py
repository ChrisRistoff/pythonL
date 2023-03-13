import tkinter as tk

window = tk.Tk()
window.title("Testing")
window.minsize(500, 500)

my_label = tk.Label(text="Hello World", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()
