from pyoo import calc

# Open a connection to LibreOffice Calc
doc = calc.Calc(docname='path_to_your_spreadsheet.ods')

# Access a specific sheet
sheet = doc.sheets[0]  # Replace 0 with the index of your sheet

# Read data from cells
data = sheet.read("A1:F10")  # Adjust the range as per your data

# Perform analysis or computations on the data
# For example, calculate the sum of a column
column_sum = sum(row[0] for row in data)  # Assuming you want to sum the first column

# You can perform various other data analysis operations as needed

# Close the document
doc.close()
