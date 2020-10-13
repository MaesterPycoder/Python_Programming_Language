import tkinter as tk
import os
from PIL import Image,ImageTk  
root = tk.Tk()  
root.title("display image")
os.chdir("F:\python pratise files")
im=Image.open("cat.jpg")  
photo=ImageTk.PhotoImage(im)  
cv = tk.Canvas()  
cv.pack(side='bottom', fill='both', expand='yes')  
cv.create_image(100, 100, image=photo, anchor='nw')  
root.mainloop()
