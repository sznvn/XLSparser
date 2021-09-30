import xlrd


file = 'D:\Projects\excelparser\1.xls'
excel_data_file = xlrd.open_workbook(file)
sheet = excel_data_file.sheet_by_index(2)

StartRow = 0
day_of_week = 'понедельник'
count = 1


def date(a):
    b = a.replace('(', '').replace(')', '').split(',')
    return b[2].strip() + '.' + b[1].strip() + '.' + b[0].strip()


for row in range(StartRow, sheet.nrows):
    if sheet.cell(row, 3).value == 'УД 23.1/Б-18':
        StartRow = row + 3
        break


for row in range(StartRow, sheet.nrows, 2):
    if sheet.cell(row, 3).value != '':
        print(sheet.cell(row, 2).value.strip() + ' - ' + (sheet.cell(row, 3).value).strip() + ', ' + (sheet.cell((row + 1), 3).value).strip())
        count += 1

    if (day_of_week != sheet.cell(row, 0).value) and (sheet.cell(row, 0).value != '' and (count != 0)):
        day_of_week = sheet.cell(row, 0).value
        print('___________________________')
        print()
        print(sheet.cell(row, 0).value.title(), date(str(xlrd.xldate_as_tuple(sheet.cell(row, 1).value, 0))))
        count = 0