from PyPDF2.pdf import PageObject
from tika import parser
from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger
import os

class Transaction:
    date = ""
    buy = False
    shareAmount = 0
    pricePerShare = 0
    fullAmount = 0

#profit = shares * (sell price - buy avarage)
class Stock:
    def __init__(self, name):
        self.name = name
    shares = 0
    _avarageCost = 0
    trades = [] #List of transactions
    deltaMoney = 0

class Options:
    deltaMoney = 0

tickerNames = []
tickerDict = {}

def cashDiv(line):
    ""

def goldFee(line):
    ""

def CIL(line):
    ""

def call(line):
    ""

def put(line):
    ""

def regularStock(line):
    splitLine = line.split()
    stockOb = tickerDict.setdefault(splitLine[3], Stock(splitLine[3]))
    transaction = Transaction()
    if splitLine[5] == "Buy":
        transaction.buy = True
    else: 
        transaction.buy = False
            


parsed_pdf = parser.from_file("829234bf-09f3-4f86-aa70-731c04efd559.pdf")
data = parsed_pdf['content'] 
print(data)


lines = data.splitlines() #Split lines
print(lines)
activityPrev = lines.find("Account Activity", 0)

#Loops while there are more "Account Activity" strings
while activityPrev != -1:
    currentLinePos = activityPrev + 3 #Info starts three lines down
    currentLine = lines[currentLinePos]

    #While there is more to this page and its not at the end 
    while currentLine != "" and currentLine.find("Total Funds Paid and Received") == -1:
        if currentLine.find("Crypto Money Movement") != -1:
            ""
        elif currentLine.find("Cash Div") != -1:
            cashDiv(currentLine)
        elif currentLine.find("Gold Fee") != -1:
            goldFee(currentLine)
        elif currentLine.find("CIL on") != -1:
            CIL(currentLine)
        elif currentLine.find("Call $") != -1:
            call(currentLine)
        elif currentLine.find("Put $") != -1:
            put(currentLine)
        else:
            currentLinePos += 1
            regularStock(lines[currentLinePos])
    
    activityPrev = lines.find("Account Activity", activityPrev)

pendingPrev = lines.find("Executed Trades Pending Settlement", 0)
while pendingPrev != -1:
    pendingPrev = lines.find("Executed Trades Pending Settlement", pendingPrev)