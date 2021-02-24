import os
import glob
import csv
import openpyxl

currentDirectory = os.getcwd()
os.chdir (currentDirectory)

for csvfile in glob.glob(os.path.join('.', '*.csv')):
    wb = openpyxl.Workbook()
    ws = wb.active
    with open(csvfile, 'rt', encoding='UTF-8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader, start=1):
            for c, val in enumerate(row, start=1):
                ws.cell(row=r, column=c).value = val
    wb.save(csvfile.replace ('.csv', '.xlsx')) #.csv' + '.xlsx')