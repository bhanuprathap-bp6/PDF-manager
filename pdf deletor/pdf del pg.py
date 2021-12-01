import tkinter as tk
from tkinter import filedialog
from tkinter import font

from PyPDF2 import PdfFileWriter, PdfFileReader

# create a PdfFileWriter object
out = PdfFileWriter()

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=450, bg='azure3', relief='raised')
canvas1.pack()

label1= tk.Label(root, text='PDF Remove Pages', bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getPNG():
    global file
    import_file_path = filedialog.askopenfilename()
    file = PdfFileReader(import_file_path)

browseButton_PNG = tk.Button(text="  Import PDF File  ", command=getPNG, bg="royalblue",
fg='white', font=('helvetica', 12,'bold'))
canvas1.create_window(150,130,window=browseButton_PNG)

# pg no label
label2= tk.Label(root, text='UnWanted Pages :', bg='azure3')
label2.config(font=('helvetica', 12))
canvas1.create_window(70, 180, window=label2)
# TextBox Creation
discret_pg = tk.Text(root,
                   height = 1,
                   width = 20)
discret_pg.pack()
canvas1.create_window(210,180, window=discret_pg)

# new file name label
label3= tk.Label(root, text='New PDF Name :', bg='azure3')
label3.config(font=('helvetica', 12))
canvas1.create_window(70, 250, window=label3)
# TextBox Creation
new_file_name_lb = tk.Text(root,
                   height = 1,
                   width = 20)
new_file_name_lb.pack()
canvas1.create_window(210,250, window=new_file_name_lb)

def convertToJPG():
    lbl.config(text = "creating... ")
    global file
    a = discret_pg.get(1.0, "end-1c")

    pg=[]
    if ('-' in a)and(',' in a):
        b=a.split(',')
        for i in b:
            j=i.split('-')
            k=list(range(int(j[0]),int(j[1])+1))
            pg += k

    elif '-' in a:
        b=a.split('-')
        pg=list(range(int(b[0]),int(b[1])+1))

    elif ',' in a:
        b=a.split(',')
        pg = [int(x) for x in b]
    
    num = file.numPages
    unwanted_pg = pg
    wanted_pg_no = [x for x in range(1,num+1) if x not in unwanted_pg]

    for i in wanted_pg_no:
        j=int(i)-1
        page = file.getPage(j)
        out.addPage(page)

    new_file_name = new_file_name_lb.get(1.0, "end-1c") + ".pdf"
    with open(new_file_name, "wb") as f:
        # Write our new PDF to this file
        out.write(f) 
    
    lbl.config(text = "Successfully created. ")

saveAsButton_JPG = tk.Button(text='Separate', command=convertToJPG,
bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150,300,window=saveAsButton_JPG)

lbl = tk.Label(root, text = "")
lbl.pack()

root.mainloop()