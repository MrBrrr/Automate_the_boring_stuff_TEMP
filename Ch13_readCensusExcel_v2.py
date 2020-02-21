#! python
# tabulates population and number of census tract for each county

import openpyxl, os, pprint
import sys
print(os.getcwd())
os.chdir(os.path.join(os.getcwd(), "Ch13_materials"))
# sys.path.append(os.path.join('D:', 'Dusia', 'Programming', 'automate_online-materials'))
print(os.getcwd())

workbook_handler = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = workbook_handler.active

StateCountyDict = {}  # {state : { County : {tracts : , pop : } } }

# 0 tract, 1 state, 2 county, 3 population
for rows in tuple(sheet.rows)[1:sheet.max_row+1]:
    StateCountyDict.setdefault(rows[1].value, {})
    StateCountyDict[rows[1].value].setdefault(rows[2].value, {'tracts': 0, 'population': 0})

    StateCountyDict[rows[1].value][rows[2].value]['tracts'] += 1
    StateCountyDict[rows[1].value][rows[2].value]['population'] += int(rows[3].value)

workbook_handler.close()

"""for key, value in StateCountyDict.items():
    for key1, value1 in value.items():
        print(key.ljust(4, ' '), key1.ljust(10, ' '),
              'tracts: '+str(value1['tracts']).ljust(14, ' '),
              'population: '+str(value1['population']))
"""
print("Writing to a file")
file_handler = open('state_pop_traces.py', 'w')

file_handler.write('AllData = '+pprint.pformat(StateCountyDict))

file_handler.close()
print("Done")


"""
in the next file

dziala w shellu nie dziala w Pycharmie... :c 
"""
# os.chdir(os.path.join(str(os.getcwd()), 'Programming', 'automate_online-materials'))
os.getcwd()  # 'D:\\Dusia\\Programming\\automate_online-materials'
import state_pop_traces
"""
-> https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

"""



