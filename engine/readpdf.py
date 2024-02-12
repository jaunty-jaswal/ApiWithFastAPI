from pdf2image import convert_from_path
import pytesseract
import numpy as np
import re
from preprocess import preprocessing
import os

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

def return_custom():
    print("our custom string is --->",customstring)
    return customstring

def return_text():
    return myString

def returnid():
    if (len(id) == 0 or len(id) == -1):
        id.append(1)
    else:
        id.append(id[len(id)-1]+1)   
    return id

#filename
pdf_file = '--destination of your pdf file--'
ourpdffile = os.path.join(os.path.dirname(__file__),"..","ourpdf.pdf")
#converting to images

text = []
txt2 = []
if(os.path.exists(ourpdffile)):
    print("_____file found______")
    pagescutom = convert_from_path(ourpdffile)  
    for i in pagescutom:
        process = preprocessing.deskew(np.array(i))
        ext = extract_text_from_image(process)
        txt2.append(ext)
        # print(txt2)
else:
    txt2.append("no file found. create one using create route")

if(os.path.exists(pdf_file)):
    pagestoimages = convert_from_path(pdf_file)
    for i in pagestoimages:
        processedimage = preprocessing.deskew(np.array(i)) #preprocess
        txt = extract_text_from_image(processedimage)
        text.append(txt)

myString = ""
for i in text:
    myString = re.sub(r"[\n\t/\f]*", "", i)
customstring = f"{txt2[0]}"
# for i in txt2:
    # customstring = re.sub(r"[\n\t]*", "", i)
id = list()
