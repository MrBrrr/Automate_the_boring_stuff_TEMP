#! python

import openpyxl, os

os.chdir(os.path.join(os.getcwd(), "automate_online-materials"))

wb = openpyxl.load_workbook("censuspopdata.xlsx")
work_sheet = wb.active

countyData = {}

the_row = ''
sum_of_pop = 0
sum_of_census_tract = 0
for each_row in work_sheet.rows:
    if each_row[2].value != the_row:
        # accumulate data to dictionary, first check if the county already exist in dictionary
        try:
            countyData[the_row]
        except KeyError:
            # such county does not exist in our data dictionary
            countyData[the_row] = (sum_of_pop, sum_of_census_tract)
        else:
            # such county exists
            countyData[the_row] = (sum_of_pop+countyData[the_row][0], sum_of_census_tract+countyData[the_row][1])
        # print("County: %s, population: %s" % (the_row, str(sum_of_pop)))
        # start new row in dictionary
        the_row = each_row[2].value
        sum_of_pop = each_row[3].value
        sum_of_census_tract = each_row[0].value
    else:
        sum_of_pop += each_row[3].value
        sum_of_census_tract += each_row[0].value

# print(countyData['San Francisco'][0])
# print(countyData['Rusk'][0])

file_handler = open(os.path.join(os.getcwd(), "CensusPopData_accumulator.txt"), "w")

countyData = {k: v for k, v in countyData.items() if k}

for county, value in countyData.items():
    file_handler.write(county.ljust(20, ' ') + str(value[0]) + os.linesep)

print(len(countyData.keys()))

file_handler.close()
