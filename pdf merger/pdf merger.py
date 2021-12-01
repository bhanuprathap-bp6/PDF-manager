import tkinter as tk
from tkinter import filedialog
from tkinter import font
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

#call pdfmerger
merge_tool = PdfFileMerger()
root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='azure3', relief='raised')
canvas1.pack()

label1= tk.Label(root, text='PDF Merger', bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

# create a list as files
files = []
def addPDF():

    import_file_path = filedialog.askopenfilename()
    files.append(import_file_path)
    
browseButton_PNG = tk.Button(text="  Add PDF File  ", command=addPDF, bg="royalblue",
fg='white', font=('helvetica', 12,'bold'))
canvas1.create_window(150,130,window=browseButton_PNG)


def Merge():

    # print all files in list-files
    print(files)

    for file in files:
        merge_tool.append(PdfFileReader(file),"rb")
    merge_tool.write("Merged_file.pdf")

    lbl.config(text = "Successfully merged. ")

saveAsButton_JPG = tk.Button(text=' Merge PDF Files', command=Merge,
bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150,220,window=saveAsButton_JPG)

lbl = tk.Label(root, text = "")
lbl.pack()

root.mainloop()