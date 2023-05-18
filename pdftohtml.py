import pdfkit
pdf_file = open('./pdfs/A Tour of C++.pdf')
html_file = pdfkit.from_file(pdf_file, "./HTMLs/A Tour of C++.html")
pdf_file.close()