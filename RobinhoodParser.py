from PyPDF2.pdf import PageObject
from tika import parser
from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger

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
page = pdf_file.getPage(0)

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

# 1. Crop top of page and check for string "Account Summary"
    # Store page object to list if it does
# 2. If it exists crop and parse the rest
# 3. If it say Executed trades pending settlement do otherwise  

page.mediaBox.lowerRight = (250, 400)
page.mediaBox.lowerLeft = (0, 400)
page.mediaBox.upperRight = (250, 612)
page.mediaBox.upperLeft = (0, 612)

print(page)
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
