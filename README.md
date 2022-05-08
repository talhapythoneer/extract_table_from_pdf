# extract_table_from_pdf
It's a simple script to extract the tables from the target pages of a PDF into CSV.

Dependencies:
- Tabule-Py
- Pandas

The code is pretty self-explanatory. Enter the file name + target pages and run the script.
You might wonder why I have concatenated the tables horizontally that exist on the same page. This is because, sometimes, the tables are divided into more than 1 column on the same page. It reads them as separate tables even if it's ONE actually. If that is not the case you can remove line no. 18.

Thanks & Regards
@talhapythoneer
