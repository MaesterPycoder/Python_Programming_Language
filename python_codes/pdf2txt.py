# Importing Required Modules
import tkinter as tk
import os, time
import pathlib
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import PyPDF2

def main():
    # Root Window
    win = tk.Tk()
    win.title("PDF2TXT CONVERTER")
    win.geometry('600x400')
    win.resizable(False, False)
    os.chdir(r'F:\py_projects\Pythonics')
    win.wm_iconbitmap('images/bird.ico')
    imageBG = ImageTk.PhotoImage(Image.open('images/loginBG.jpg'))
    canvas = tk.Canvas(win, width = 600, height = 400)
    canvas.create_image(0, 0, anchor = "nw", image = imageBG)
    canvas.place_configure(x = 0, y = 0)
    tk.Label(win, text = time.ctime(), fg = 'Gold', bg = 'Black', font = 'Helvetica 10').place_configure(x = 440, y = 40)

    # Variable Declaring 
    ch = tk.IntVar()
    languages = [
        "None",
        "PDF2TXT",
        "DOCS2PDF"
        ]
    p = 40

    # Functions
    def optChoice():
        opt = ch.get()
        if opt == 0:
            pass
        elif opt == 1:
            pass
        else:
            pass
    def openfile():
        filetypes = [('*.pdf')]
        file = askopenfile(filetypes)
        pdf_file = open(file.name, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        pathlib.Path('con_txt.txt').write_text(page_content)
        messagebox.showinfo("Done","Successfully Completed.")


    # Frame Design
    
    tk.Label(win, text = '*Welcome to PDF2TXT Converter*', fg = 'Red', bg = 'Black', font = 'Helvetica 18 bold').place(x=140,y=10)
    tk.Label(win, 
            text="Choose your Option:",
            justify = tk.LEFT,
            padx = 20,
            fg = "#00FD00",
            bg = "Black",
            font = 'Helvetica 14 bold'
            ).place(x = 20, y = 40)
    for val, language in enumerate(languages):
        p+=30
        tk.Radiobutton(win, 
                    text=language,
                    padx = 20, 
                    variable = ch, 
                    command = optChoice,
                    value = val,
                    fg = 'Orange',
                    bg = 'Black',
                    font = 'Helvetica 14',
                    activebackground = "Black"
                    ).place(x = 50, y = p)
    tk.Label(win, text = 'Direct path to file:', fg = '#FDFD00', bg = 'Black', font = 'Helvetica 16 bold').place(x = 40, y = 170)
    tk.Label(win, text = 'Choose file:', fg = '#FD0DEE', bg = 'Black', font = 'Helvetica 16 bold').place(x = 40, y = 203)
    tk.Button(win, text = "Select", width = 30, command = openfile).place(x = 200, y = 200)

    win.mainloop()
if __name__ == '__main__':
    main()