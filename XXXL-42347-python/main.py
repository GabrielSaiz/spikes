import pandas as pd

INPUT_FILE_EXCEL = './input/PLZ-Tab ECOM 20210830.xlsx'
OUTPUT_FILE_CSV = './output/PLZ-Tab ECOM 20210830.csv'

# Load Excel file
fileExcel = pd.read_excel(INPUT_FILE_EXCEL)
print("The Excel file before deleting the column")
print(fileExcel)

# Remove LKZ column
del fileExcel["LKZ"]
print("The Excel file after deleting the column a")
print(fileExcel)

# Save as CSV
fileExcel.to_csv(OUTPUT_FILE_CSV,
                 index=None,
                 header=True)
