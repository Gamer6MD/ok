import tkinter as tk
import random


root = tk.Tk()
root.geometry("150x65")
root.overrideredirect(True)

def on_closing():
    root.geometry("+{}+{}".format(random.randint(0, 1800), random.randint(0, 900)))
    root.deiconify()

def message():
    root.withdraw()
    root.after(1, on_closing)

label = tk.Label(root, text = "Nu poti sa scapi de mine.")
label.pack()
button = tk.Button(root, text="OK", command=message)
button.pack()

root.mainloop()
