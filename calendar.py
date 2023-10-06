from tkinter import ttk
import ttkbootstrap

root = ttkbootstrap.window(themename="cyborg")
root.title('Calendar')

def see_date():
    date=cal.entry.get()
    date_label.config(text=date)

