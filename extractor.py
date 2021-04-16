#! /usr/bin/env python
# this program extract text from pdfs
# author dave
import re
import sys
import pdfplumber

def extractor(path_to_pdf):

    pdf = pdfplumber.open(path_to_pdf)

    num_pages=len(pdf.pages)

    pdf_str = ""

    for i in range(num_pages):
        pdf_str+='\n'+str(pdf.pages[i].extract_text().replace('\n ',''))
    
    pdf.close()

    pdf_str_list = re.split(r'\.+\s+\n',pdf_str)
    
    return pdf_str, pdf_str_list

if __name__ == "__main__":

    path = sys.argv[1]
    text = extractor(path)[0]
    print(text)
    
   
