import tabula
import pandas as pd


# target start and ending pages
startPage = 18
endPage = 20

# pdf file name you want to target | keep it the same folder where the script is
pdfFileName = "pdf_1.pdf"


for pageNumber in range(startPage, endPage + 1):
    print("Scraping page {}".format(pageNumber))

    # extracting all the tabels from the page
    tables = tabula.read_pdf(pdfFileName, pages=str(pageNumber))

    # concatenate the data horizontally
    tables = pd.concat(tables, axis = 1)

    # remove indexing
    tables.reset_index(drop=True)

    if pageNumber == startPage:
        tables.to_csv(pdfFileName.replace('.pdf', '') + ".csv", mode="a", header=True, index=False)
    else:
        tables.to_csv(pdfFileName.replace('.pdf', '') + ".csv", mode="a", header=False, index=False)