from tkinter import *


def get_button(name, to_do, size):
    button = Button(text=name, command=to_do,
                    font=('Arial Bold', 10), width=size)
    return button


def get_lable(name):
    label = Label(text=name, font=('Time New Roman', 13))
    return label


def get_entry(win, size):
    entry = Entry(win, width=size, font=('Arial Bold', 10))
    return entry
