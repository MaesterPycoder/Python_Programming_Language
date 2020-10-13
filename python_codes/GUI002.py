from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import os
root=Tk()
root.title("Welcome to Shanmukkha's GUI")
root.geometry("1360x768")
os.chdir("F:\python pratise files")
root.wm_iconbitmap("shanmu.ico")
c=Canvas(root,bg="darkblue",height=1280,width=960,cursor="pencil")
os.chdir(r"C:\Users\S.S Shanmukkha\Pictures\My Photos")
file1=ImageTk.PhotoImage(file="PHOTO.jpg")
file2=ImageTk.PhotoImage(file="profile.jpg")
id=c.create_image(500,500,anchor=CENTER,image=file1,activeimage=file2)
c.pack()
root.mainloop()
