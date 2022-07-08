from tkinter import *
from tkinter import messagebox
from brand_data import get_brand_data

def ui():
    win = Tk()

    win.title("Import Data")
    win.geometry("250x100")

    lbl = Label(win, text="Enter Name Here: ")
    lbl.grid(column=1, row=0)

    txt = Entry(win,width=15)
    txt.grid(column=2, row=0)

    btn = Button(win, text="Import Data", command=lambda: get_brand_data(txt.get()), fg='black')
    btn.grid(column=1, row=1)

    # link1 = Button(win, text="Google Sheet", command=callback, fg="blue")
    # link1.grid(column=2, row=1)
    win.mainloop()
