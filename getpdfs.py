import os
import sys


def getfiles():
    # Instruction(s) to get the list of PDF files goes here (and/or below)...
    pdf_files = []
    for root, dirs, files in os.walk(os.getcwd()):
        pdf_files.extend([])
        for fname in files:
            if fname.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, fname))

    return pdf_files


print(getfiles())

