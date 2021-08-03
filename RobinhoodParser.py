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

parsed_pdf = parser.from_file("829234bf-09f3-4f86-aa70-731c04efd559.pdf")
data = parsed_pdf['content'] 
print(data)




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




# 0, 612
# |
# |
# |
# |
# |___________ 792, 0


# 0,0    792,0     0,612    792,612