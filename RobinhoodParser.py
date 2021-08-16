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


lines = data.splitLines()
activityPrev = lines.find("Account Activity", 0)
while activityPrev != -1:
    activityPrev = lines.find("Account Activity", activityPrev)
    currentLine = lines[activityPrev].split()

pendingPrev = lines.find("Executed Trades Pending Settlement", 0)
while pendingPrev != -1:
    pendingPrev = lines.find("Executed Trades Pending Settlement", pendingPrev)