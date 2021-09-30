import xlrd


file = 'D://Projects/excelparser/1.xls'
excel_data_file = xlrd.open_workbook(file)
sheet = excel_data_file.sheet_by_index(0)


def date(a):
    b = a.replace('(', '').replace(')', '').split(',')
    return b[2].strip() + '.' + b[1].strip() + '.' + b[0].strip()


def day(row):
    while True:
        if sheet.cell(row, 0).value != "":
            return sheet.cell(row, 0).value.strip(' ')
        row -= 2


def GroupSched(col):
    s = ''
    for row in range(19, sheet.nrows - 1, 2):
        if (sheet.cell(row, col).value != ""):
            s += day(row) + "\t" + sheet.cell(row, 2).value + "\t" + sheet.cell(row, col).value + "\t" + sheet.cell((row + 1), col).value + "\n"
    return s

for i in range(7):
    sheet = excel_data_file.sheet_by_index(i)
    print(i)
    for y in range(3, sheet.ncols):
        fname = './' + sheet.cell(16, y).value.replace('/', '_') + '.txt'
        file = open(fname, 'w', encoding='utf-8')
        file.write(GroupSched(y))
        file.close()