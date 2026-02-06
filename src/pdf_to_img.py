import os
from pdf2image import convert_from_path

PDF_BASE_DIR = "data/synthetic"
IMG_BASE_DIR = "data/processed"

DOC_TYPES = ["pan", "aadhaar"]

def convert_pdfs_to_img():
    for doc in DOC_TYPES:
        pdf_dir=os.path.join(PDF_BASE_DIR,doc)
        img_dir=os.path.join(IMG_BASE_DIR,doc)

        os.makedirs(img_dir,exist_ok=True)

        for file in os.listdir(pdf_dir):
            if not file.endswith(".pdf"):
                continue
            
            pdf_path= os.path.join(pdf_dir,file)

            pages= convert_from_path(pdf_path,dpi=200)

            img_path= os.path.join(img_dir,file.replace(".pdf",".png"))

            pages[0].save(img_path,"PNG")

    print("PDF to Image conversion completed!")

if __name__=="__main__" :
    convert_pdfs_to_img()   