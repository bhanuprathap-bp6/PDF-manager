from PyPDF2 import PdfFileReader,PdfFileWriter

file_name = "aa.pdf"
file = PdfFileReader(file_name)
out = PdfFileWriter()
num = file.numPages
unwanted_pg = [9]
wanted_pg_no = [x for x in range(1,num+1) if x not in unwanted_pg]

for i in wanted_pg_no:
    page = file.getPage(i-1)
    out.addPage(page)

new_file_name = "bb.pdf"
with open(new_file_name, "wb") as f:
        # Write our new PDF to this file
        out.write(f) 
