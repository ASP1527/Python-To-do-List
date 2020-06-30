import tkinter as tk
from tkinter import *
import os

root = tk.Tk()
root.title("Checklist")
items = []

canvas = tk.Canvas(root, height=800, width=700, bg="#C0C0C0")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight = 0.8, relx=0.1, rely=0.1)


if os.path.isfile('list.txt'):
    with open('list.txt', 'r') as f :
        temp = f.read()
        print(temp)
        temp = temp.split(",")
        items = [x for x in temp if x.strip()]
        for i in range (0,len(items)):
            label = tk.Label(frame, text=items[i], bg="#C0C0C0")
            label.pack()

def getEntry():
    item = e.get()
    item = str(item)
    if item in items:
        global temporaryItem
        temporaryItem = item
        items.remove(item)
    else:
        items.append(item)
    print (items)
    for widget in frame.winfo_children():
        widget.destroy()
    for i in range (0,len(items)):
        label = tk.Label(frame, text=items[i], bg="#C0C0C0")
        label.pack()

def undoTask():
    items.append(temporaryItem)
    for widget in frame.winfo_children():
        widget.destroy()
    for i in range (0,len(items)):
        label = tk.Label(frame, text=items[i], bg="#C0C0C0")
        label.pack()

e = tk.Entry(root, width=50)
e.pack()

add = tk.Button(root, text="Click", padx=10, pady=5, fg="white", bg="#C0C0C0", font=('helvetica',9), command=getEntry)
add.pack()

undo = tk.Button(root, text="Undo", padx=10, pady=5, fg="white", bg="#C0C0C0", command=undoTask)
undo.pack()

root.mainloop()

with open('list.txt', 'w') as f:
    for item in items:
        f.write(item + ',')