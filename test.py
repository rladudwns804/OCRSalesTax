from PIL import Image
import tkinter as tk
from tkinter import filedialog
import pytesseract as pt
import re
import pandas as pd



#tkinter for opening image file
root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()
im = Image.open(filename)



text = pt.image_to_string(im, lang="eng")
text.upper()
substring = "TAX"

#Find substring conting Tax and parse with the tax amount: 
find = text.find(substring)
newText = text[find:find+12]
newText = re.sub("[^.0-9]",'',newText)
amount = newText.replace(" ", "")

#Load to Dataframe and export as csv:
df = pd.DataFrame(columns = ["Tax"])
x = 0

if len(df) == 0:
    df.loc[x,"Tax"] = amount
    df.to_csv("sales tax.csv")
else:
    x = len(df)
    df.loc[x,"Tax"] = amount
    df.to_csv("sales tax.csv")



print(amount)
