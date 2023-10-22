from tkinter import *
import ttkbootstrap
"""from ttkbootstrap.widgets import *
from ttkbootstrap.dialogs import Querybox
from ttkbootstrap.dialogs.dialogs import *"""
import calendar
root = Window(title="My Calendar", themename="cyborg")

#function to get the date
def see_date():
    date=cal.entry.get()
    date_label.config(text=date)
    
#this is the dataEntry widget
cal=ttkbootstrap.DateEntry(root, dateformat='%d%m%Y',bootstyle="info")
cal.pack(padx=40,pady=40)
#button to get the selected date
btn=ttk.Button(root,text="Show Date", bootstyle="light-outline", command=see_date)
btn.pack(padx=40,pady=45)
date_label=ttk.Label.pack(padx=40,pady=50)
root.mainloop()