from PIL import Image
import tkinter as tk
from tkinter import filedialog
import pytesseract as pt
import re
import pandas as pd


root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()


im = Image.open(filename)
text = pt.image_to_string(im, lang="eng")
text.upper()
substring = "TAX"
find = text.find(substring)
newText = text[find:find+12]
newText = re.sub("[^.0-9]",'',newText)
amount = newText.replace(" ", "")
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
