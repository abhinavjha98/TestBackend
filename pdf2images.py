from pdf2image import convert_from_path

pdfs = r"/home/abhinav/Downloads/1bd38f38-be81-4d30-9b84-2ef400871e67.pdf"
pages = convert_from_path(pdfs, 350)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    i = i+1        