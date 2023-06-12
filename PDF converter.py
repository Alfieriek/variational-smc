from pdf2docx import parse

# path of pdf file
pdf_file = '/Users/alfieriek/Desktop/CO_BE_ETHICS_SUM_2022.pdf'

# will create .docx in same path
docx_file = '/Users/alfieriek/Desktop/CO_BE_ETHICS_SUM_2022.docx'

# Here is where we convert pdf to docx
parse(pdf_file, docx_file, start=0, end=None)

/Users/alfieriek/Desktop/Copy of CO_TM_SBM_SUM_2022.pdf
/Users/alfieriek/Desktop/Copy of CO_BE_ETHICS_SUM_2022.pdf
/Users/alfieriek/Desktop/CO_TM_SBM_SUM_2022.pdf
/Users/alfieriek/Desktop/CO_BE_ETHICS_SUM_2022.pdf