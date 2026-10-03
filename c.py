
import tkinter as tk

root = tk.Tk()
root.title("Calculator")

e = tk.Entry(root, font=("Arial", 20), justify="right")
e.grid(row=0, column=0, columnspan=4)

def click(x):
    if x == "=":
        ans = eval(e.get())
        e.delete(0, tk.END)
        e.insert(0, ans)
    elif x == "C":
        e.delete(0, tk.END)
    else:
        e.insert(tk.END, x)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

r = 1
c = 0

for b in buttons:
    tk.Button(
        root, text=b, width=5, height=2,
        command=lambda x=b: click(x)
    ).grid(row=r, column=c)

    c += 1
    if c == 4:
        c = 0
        r += 1

root.mainloop()