import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.geometry("500x500")

tk.Label(window, text="Hello World!").pack(pady=100)

window.mainloop()