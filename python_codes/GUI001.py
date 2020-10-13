from tkinter import *
from tkinter import font
import os
#for creating window
root=Tk()
#making title to the window
root.title("Welcome to Shanmukkha's GUI")
#creating size of window
root.geometry("1360x768")
#making path for getting window icon
os.chdir("F:\python pratise files")
root.wm_iconbitmap("shanmu.ico")
#for creating canvas
c=Canvas(root,bg="blue",height=800,width=700,cursor="pencil")
#for creating line
id=c.create_line(500,50,500,100,500,150,width=4,fill="white")
#for creating oval
id=c.create_oval(100,100,400,300,width=5,fill="yellow",outline="red",activefill="green")
#for filling text in GUI ,first setting font and next input
fnt=("Times",40,"bold italic underline")
id=c.create_text(600,100,text="This is my first GUI program",font=fnt,fill="yellow",activefill="green")
c.pack()
root.mainloop()
