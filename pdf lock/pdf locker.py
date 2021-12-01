import tkinter as tk
from tkinter import filedialog
from tkinter import font
from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader

# create a PdfFileWriter object
out = PdfFileWriter()

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=350, bg='azure3', relief='raised')
canvas1.pack()

label1= tk.Label(root, text='PDF Locker', bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getPNG():
    global import_file_path

    import_file_path = filedialog.askopenfilename()
    file = PdfFileReader(import_file_path)

    #Get number of pages in original file
    num = file.numPages

    # Iterate through every page of the original 
    # file and add it to our new file.
    for idx in range(num):
    
        # Get the page at index idx
        page = file.getPage(idx)
      
        # Add it to the output file
        out.addPage(page)

browseButton_PNG = tk.Button(text="  Import PDF File  ", command=getPNG, bg="royalblue",
fg='white', font=('helvetica', 12,'bold'))
canvas1.create_window(150,130,window=browseButton_PNG)

# password label
label2= tk.Label(root, text='Password:', bg='azure3')
label2.config(font=('helvetica', 12))
canvas1.create_window(70, 180, window=label2)
# TextBox Creation
inputtxt = tk.Text(root,
                   height = 1,
                   width = 20)
inputtxt.pack()
canvas1.create_window(200,180, window=inputtxt)

def convertToJPG():

    password = inputtxt.get(1.0, "end-1c")
    global import_file_path
    #export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    
    # Create a variable password and store 
    # our password in it.
    #password = "pass"
  
    # Encrypt the new file with the entered password
    out.encrypt(password)
    
    f_name = ""
    for letter in import_file_path:
        if letter ==  ".":
            #f_name += "_encrypted.pdf" 
            f_name += "_locked.pdf"
            break
        f_name += letter

    encrypted_file = f_name  
    # Open a new file "myfile_encrypted.pdf"
    with open(encrypted_file, "wb") as f:
        # Write our encrypted PDF to this file
        out.write(f)

    lbl.config(text = "Successfully locked ")

saveAsButton_JPG = tk.Button(text='LOCK', command=convertToJPG,
bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150,260,window=saveAsButton_JPG)

lbl = tk.Label(root, text = "")
lbl.pack()

root.mainloop()