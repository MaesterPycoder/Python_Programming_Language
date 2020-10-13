# # Importing Modules
# import tkinter as tk
# from tkinter import ttk
# from PIL import ImageTk, Image
# import os, datetime
# os.chdir(r"F:\py_projects\Pythonics")


# # Root Window
# root = tk.Tk()
# root.title('PyTest')
# root.geometry('600x400')
# root.resizable(False, False)

# # Functions
# def lpYr_check(y):
#     if y%400 == 0:
#         return 1
#     elif y%100 != 0 and y%4 == 0:
#         return 1
#     return 0

# # Variables
# day = tk.StringVar()
# month = tk.StringVar()
# year = tk.StringVar()

# if month.get() in ["February"]:
#     if lpYr_check(year.get()):
#         lmt = 29
#     else:
#         lmt = 28
# elif month.get() in ["April","June","September","November"]:
#     lmt = 30
# else:lmt = 31
# spnb1 = tk.ttk.Spinbox(root,textvariable = day, wrap = True, from_ = 1, to = lmt, font = 'Helvetica 15')
# spnb1.place(x=430,y=100,width=120,height=30)
# year = str(datetime.date.today())
# spnb2 = tk.ttk.Spinbox(root,textvariable = month, wrap=True,values=["January","February","March","April","May","June",
#                                               "July","Augest","September","October","November","December"],font='Helvetica 15')
# spnb2.place(x=300,y=100,width=120,height=30)
# spnb3 = tk.ttk.Spinbox(root,textvariable = year, wrap=True,from_=2000,to=int(year[:4]),font='Helvetica 15')
# spnb3.place(x=170,y=100,width=120,height=30)

# root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def example1():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def example2():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)

root.mainloop()