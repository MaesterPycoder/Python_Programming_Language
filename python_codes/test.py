# Importing Modules
import tkinter as tk
from PIL import Image, ImageTk
import os, datetime, time

if __name__=='__main__':
    # Root Window
    win = tk.Tk()
    win.title("Pythonics SignUp")
    win.geometry('600x400')
    win.resizable(False, False)
    os.chdir(r'F:\py_projects\Pythonics')
    win.wm_iconbitmap('images/bird.ico')
    imageBG = ImageTk.PhotoImage(Image.open('images/loginBG.jpg'))
    canvas = tk.Canvas(win, width = 600, height = 400)
    canvas.create_image(0, 0, anchor = "nw", image = imageBG)
    canvas.place_configure(x = 0, y = 0)

    # Variables Declartaion
    name = tk.StringVar()
    emailid = tk.StringVar()
    mobile = tk.IntVar(value = 91)
    # dob
    userName = tk.StringVar()
    password = tk.StringVar()
    reTypePass = tk.StringVar()

    # SignUp Functions
    def signUp():
        pass

    # Buttons and Layout
    label1 = tk.Label(win, text = '*Pythonics Account SignUp*', fg = 'Maroon', bg = 'Lawn Green', font = 'Helvetica 15 bold')
    label1.place(x = 160, y = 10)

    label2 = tk.Label(win, text = 'Enter Credentials:', fg = 'White', bg = 'Black', font = 'Helvetica 12 bold')
    label2.place(x = 10, y = 40)

    label3 = tk.Label(win, text = 'Name            :', fg = 'White', bg = 'Black', font = 'Helvetica 12 bold')
    label3.place(x = 100, y = 65)
    nameField = tk.Entry(win, textvariable = name, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 12')
    nameField.place(x = 210, y = 65, width = 300)
    nameField.focus()

    label3 = tk.Label(win, text = 'Email-id        :', fg = 'White', bg = 'Black', font = 'Helvetica 12 bold')
    label3.place(x = 100, y = 95)
    mailField = tk.Entry(win, textvariable = emailid, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 12')
    mailField.place(x = 210, y = 95, width = 300)

    label4 = tk.Label(win, text = 'Date of birth:', fg = 'White', bg = 'Black', font = 'Helvetica 12 bold')
    label4.place(x = 100, y = 125)
    # dobField = tk.Entry(win, textvariable = dob, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 12')
    # dobField.place(x = 210, y = 125, width = 300)

    label5 = tk.Label(win, text = 'MobileNo.    :', fg = 'White', bg = 'Black', font = 'Helvetica 12 bold')
    label5.place(x = 100, y = 155)
    mobileField = tk.Entry(win, textvariable = mobile, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 12')
    mobileField.place(x = 210, y = 155, width = 200)

    label6 = tk.Label(win, text = 'UserName   :', fg = 'White', bg = 'Black', font = 'Helvetica 12 bold')
    label6.place(x = 100, y = 185)
    userField = tk.Entry(win, textvariable = userName, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 12', justify = "center")
    userField.place(x = 210, y = 185, width = 200)

    label7 = tk.Label(win, text = 'Password    :', fg = 'White', bg = 'Black', font = 'Helvetica 12 bold')
    label7.place(x = 100, y = 215)
    keyField = tk.Entry(win, textvariable = password, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 12')
    keyField.place(x = 210, y = 215, width = 200)

    label8 = tk.Label(win, text = 'Re-enter          :\n Password', fg = 'White', bg = 'Black', font = 'Helvetica 10 bold')
    label8.place(x = 100, y = 245)
    rekeyField = tk.Entry(win, textvariable = password, fg = 'maroon', bg = 'Light cyan', font = 'Helvetica 12')
    rekeyField.place(x = 210, y = 245, width = 200)

    signUpB = tk.Button(win, text = "Sign Up", fg = 'Dark Green', bg = 'Turquoise', width = 10, height = 1, command = signUp, font = 'Helvetica 10 bold')
    signUpB.place(x = 250, y = 280)

    tk.Label(win, text = time.ctime(), fg = 'Gold', bg = 'Black', font = 'Helvetica 9').place_configure(x = 440, y = 10)
    year = str(datetime.date.today())
    tk.Label(win, text = "SSS UNION", fg = "White", bg = 'Black', font = 'Helvetica 10 bold').place_configure(x = 250, y = 360)
    tk.Label(win, text = "© "+year[:4]+" All Rights Reserved", fg = "White", bg = 'Black', font = 'Helvetica 10 bold').place_configure(x = 200, y = 380)

    win.mainloop()