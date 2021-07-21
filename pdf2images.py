from pdf2image import convert_from_path
import os
import easyocr
pdfs = r"/home/abhinav/Downloads/1bd38f38-be81-4d30-9b84-2ef400871e67.pdf"
pages = convert_from_path(pdfs, 350)
reader = easyocr.Reader(['en'])
i = 1

for page in pages:
    text = ""
    image_name = "Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    output = reader.readtext("Page_" + str(i) + ".jpg")
    for detection in output:
          text += detection[1]
    print(text)
    i = i+1        