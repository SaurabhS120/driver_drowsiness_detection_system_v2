import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
parent = tk.Tk()
parent.title("Drowsiness")
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='red')
bar = Progressbar(parent, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 0
bar.grid(column=0, row=0)
parent.geometry("200x50+650+10")
btn = tk.Button(parent, text='STOP')
btn.grid(column=0, row=1)
def close_main(event):
    import eye_detection
    eye_detection.want_continue=False
btn.bind('<Button-1>', close_main)
btn.configure(bg="blue",fg="white")
parent.update()
def update(val):
    bar['value'] = val * 10
    parent.update()
def close():
    parent.destroy()