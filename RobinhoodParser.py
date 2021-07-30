from PyPDF2.pdf import PageObject
from tika import parser
from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger
import os

class Stock:
    name = ""
    shares = 0
    avarage = 0
    trades = 0
    deltaMoney = 0

class Crypto:
    name = ""
    amount = 0
    avarage = 0
    trades = 0
    deltaMoney = 0

class Options:
    deltaMoney = 0

tickerNames = []
tickerDict = {}


pdf_file = PdfFileReader(open("829234bf-09f3-4f86-aa70-731c04efd559.pdf","rb"))
num_of_pages = pdf_file.getNumPages()

os.system("echo Hello from the other side!")

for num in range(num_of_pages):
    print(num)
    page = pdf_file.getPage(num)
    page.trimBox.lowerLeft = (0, 500)
    page.trimBox.upperRight = (250, 612)
    page.cropBox.lowerLeft = (0, 500)
    page.cropBox.upperRight = (250, 612)
    output = PdfFileWriter() 
    output.addPage(page)
    outputStream = open('temp.pdf','wb')
    output.write(outputStream)
    outputStream.close()
    os.system("\"C:/Program Files/gs/gs9.54.0/bin/gswin64c.exe\" -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=temp1.pdf temp.pdf")
    parsed_pdf = parser.from_file("temp1.pdf")
    data = parsed_pdf['content'] 
    print(data)
    print(type(data))






# 1. Crop top of page and check for string "Account Summary"
    # Store page object to list if it does
# 2. If it exists crop and parse the rest
# 3. If it say Executed trades pending settlement do otherwise  



#last page of active or nah is weird

#webbrowser.open(page)
#page[]

#page.mediaBox.lowerRight = (lower_right_new_x_coordinate, lower_right_new_y_coordinate)
#page.mediaBox.lowerLeft = (lower_left_new_x_coordinate, lower_left_new_y_coordinate)
#page.mediaBox.upperRight = (upper_right_new_x_coordinate, upper_right_new_y_coordinate)
#page.mediaBox.upperLeft = (upper_left_new_x_coordinate, upper_left_new_y_coordinate)

# opening pdf file
#parsed_pdf = parser.from_file("829234bf-09f3-4f86-aa70-731c04efd559.pdf")
  
# saving content of pdf
# you can also bring text only, by parsed_pdf['text'] 
# parsed_pdf['content'] returns string 
#data = parsed_pdf['content'] 
  
# Printing of content 
#print(data)
  
# <class 'str'>
#print(type(data))


print(page.cropBox.getLowerLeft())
print(page.cropBox.getLowerRight())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())

# 0, 612
# |
# |
# |
# |
# |___________ 792, 0


# 0,0    792,0     0,612    792,612