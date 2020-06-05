import tkinter as tk
import random


win = tk.Tk()
win.title("排座位助手")

win.geometry("250x100")
win.resizable(0, 0)

win.config(bg="#323232")
list = []


def random_list():
    list = []
    n = nub_en.get()
    i = 1
    sum = 0
    while i <= int(n):
        sum = sum+1
        i = i+1
        list.append(sum)
    random.shuffle(list)
    print("結果:", list)


number = tk.Label(text="人數", bg="#323232", fg="white")
number.config(width=10, height=2)
number.grid(row=0, column=0)


nub_en = tk.Entry()
nub_en.grid(row=0, column=1)


btn = tk.Button(text="start", command=random_list)
btn.config(width=10, height=2)
btn.config(background="#696969")
btn.grid(row=1, column=1)


win.mainloop()
