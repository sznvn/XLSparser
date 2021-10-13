# This is advanced version of parser with better algorithm
import xlrd
import os

c = 0
# os.system("clear.bat")

def openXLS(name):
    file = 'C:/Users/sznvn/Desktop/files/' + name + '.xls'
    xls = xlrd.open_workbook(file)
    nsheet = xls.nsheets
    # print(str(name) + '.xls is opened\t', nsheet, 'sheets')
    for page in range(nsheet):
        sheet = xls.sheet_by_index(page)
        # print(sheet.nrows, 'строк, ', sheet.ncols, 'столбцов')
        for group in range(3, sheet.ncols):
            s = sheet.cell(16, group).value.replace('/', '_')
            if s != '':
                text = parseGroup(sheet, group)
                exportCSV(sheet.cell(16, group).value.replace('/', '_') + ' ' + sheet.cell(15, group).value.replace(' неделя', 'w'), text)

def parseGroup(sheet, col):
    global c
    s = ''
    for row in range(1, sheet.nrows):
        print(sheet.cell(row, col), row, sheet.nrows)
        s += str(sheet.cell(row, col).value) + ',\n'
        c += 1
    return s



def exportCSV(name, text):
    fname = 'C:/Users/sznvn/Desktop/files/out/' + name + '.txt'
    file = open(fname, 'w', encoding='utf-8')
    file.write(text)
    file.close()


for i in range(1, 16):
    openXLS(str(i))

print(c)