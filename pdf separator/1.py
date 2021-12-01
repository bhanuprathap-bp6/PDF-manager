from PyPDF2 import PdfFileReader,PdfFileWriter

file_name = "a.pdf"
file = PdfFileReader(file_name)
out = PdfFileWriter()
num = file.numPages

wanted_pg_no = [2,4]

for i in wanted_pg_no:
    page = file.getPage(i-1)
    out.addPage(page)

new_file_name = "b.pdf"
with open(new_file_name, "wb") as f:
        # Write our new PDF to this file
        out.write(f) 
