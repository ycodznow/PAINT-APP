from tkinter import *
global new

def execute(event):

    new = canva.create_oval(event.x-2,event.y-2,event.x,event.y,outline = "red")

def click(event):

    print("clicked")
    new.config(outline = "black")


root = Tk()
root.geometry("500x300")
root.title("Paint ")

canva = Canvas(root)

canva.pack()

canva.bind("<Motion>",execute)
canva.bind("<Button-1>",click)

root.mainloop()