import xlrd

excel_data_file = xlrd.open_workbook('./8.xls')
sheet = excel_data_file.sheet_by_index(6)

day_of_week = ''
count = 0

print('Расписание на',sheet.cell(15, 3).value.replace(' неделя', '-'), 'ую неделю')

a = sheet.ncols
b = sheet.nrows
print(a, ' ', b)
for row in range(19,sheet.nrows,2):

    if (sheet.cell(row, 3).value != ''):
        print(sheet.cell(row, 2).value, ' - ', sheet.cell(row, 3).value, ', ', sheet.cell((row + 1), 3).value)

    if ((day_of_week != sheet.cell(row, 0).value) and (sheet.cell(row, 0).value != '')):
        day_of_week = sheet.cell(row, 0).value
        print('___________________________')
        print(sheet.cell(row, 0).value, xlrd.xldate_as_tuple(sheet.cell(row, 1).value, 0))
        count = 0
