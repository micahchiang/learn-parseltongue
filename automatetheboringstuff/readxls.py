#! python3
# reads a spreadsheet

import openpyxl, pprint

print('opening book...')
wb = openpyxl.load_workbork('censuspopdate.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

print('reading rows...')

for row in range(2, sheet.max_row+1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('writing results...')
resultFile = open('census2010.py', 'W')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('done')

