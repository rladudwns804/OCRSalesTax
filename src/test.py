from PIL import Image
from googledrive import main as drive
import tkinter as tk
from tkinter import filedialog
import socket
import pytesseract as pt
import re
import pandas as pd


#Prompt user to open image file in system:
root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()
im = Image.open(filename)

#Using pytesseract, convert image into text:
text = pt.image_to_string(im, lang="eng")
text.upper()
substring = "TAX"

#Find substring conting Tax and parse with the tax amount: 
find = text.find(substring)
newText = text[find:find+12]
newText = re.sub("[^.0-9]",'',newText)
amount = newText.replace(" ", "")

#Load to Dataframe and export as csv/excel:
df = pd.DataFrame(columns = ["Tax"])
x = 0

if len(df) == 0:
    df.loc[x,"Tax"] = amount
    df.to_csv("sales tax.csv")
else:
    x = len(df)
    df.loc[x,"Tax"] = amount
    df.to_csv("sales tax.csv")

#Upload image to google drive:
drive(filename)

