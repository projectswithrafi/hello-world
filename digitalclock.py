import tkinter as tk
from time import strftime

root = tk.TK()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

Label = tk.Label(
    root, font=('calibri', 50, bold, background='yellow', foreground='black')
                    
label.pack(anchor='center')

time()

root.mainloop()

