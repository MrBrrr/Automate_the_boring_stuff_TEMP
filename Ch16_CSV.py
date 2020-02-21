#! python3

# ########################################
# Handling csv files
# 1. Reader
# 2. Writer
# 3. DictReader - with header
# 4. DictWriter - with header
#
#
#
#
# ########################################

import csv
import os
import pprint

# READER
os.chdir(os.path.join(os.getcwd(), 'Ch16_materials'))

"""
example_file_handler = open('example.csv')
example_reader = csv.reader(example_file_handler)
example_data = list(example_reader)
"""


"""
pprint.pprint(example_data)
print(example_data[5][2])
print(example_data[0][0])
print(example_data[1][1])
print(example_data[2][2])

example_file_handler.close()
"""

"""
# 1
print('#1')
for row, line_num in zip(example_data, range(1, example_reader.line_num++1)):
    print('Row #' + str(line_num) + ' ' + str(row))
example_file_handler.close()
"""
"""
# 2 example_reader have to start from the beginning
print('#2')
example_file_handler1 = open('example.csv')
example_reader1 = csv.reader(example_file_handler1)
for row in example_reader1:
    print('Row #' + str(example_reader1.line_num) + ' ' + str(row))
example_file_handler1.close()
"""

# WRITER
"""
output_csv_handler = open('output.csv', 'w', newline='')
output_writer = csv.writer(output_csv_handler)
print(output_writer.writerow(['cell1', 'cell2', 'cell3', 'cell4']))  # 20 + 3x, + cr + lf
print(output_writer.writerow(['sth', 'eth', 'ath', 'nth']))  #
print(output_writer.writerow(['hallo, world ']))  # 2x" + 13 + cr + lf
output_csv_handler.close()
"""

# TSV - delimiter (tab) + line terminator
# delimiter is just one sign
# line terminator could be multiple
"""
output_csv_handler = open('output.tsv', 'w', newline='')
output_writer = csv.writer(output_csv_handler, delimiter='\t', lineterminator='\n\n')
print(output_writer.writerow(['cell1', 'cell2', 'cell3', 'cell4']))  # 20 + 3x, + cr + lf
print(output_writer.writerow(['sth', 'eth', 'ath', 'nth']))  #
print(output_writer.writerow(['hallo, world ']))  # 2x" + 13 + cr + lf
output_csv_handler.close()
"""

# CSV with headers - DictReader + DictWriter
"""
import os
example_csv_with_header = open('exampleWithHeader.csv')
example_reader = csv.DictReader(example_csv_with_header)
print(' '.join(example_reader.fieldnames))
for row in example_reader:
    print('#%s:' % (example_reader.line_num-1), row['Timestamp'], row['Fruit'], row['Quantity'])
example_csv_with_header.close()
"""

# if csv doesn't have header, I can add it by myself
"""
import os
example_csv_WITHOUT_header = open(os.path.join('example.csv'))
example_reader = csv.DictReader(example_csv_WITHOUT_header, fieldnames=['Timestamp', 'Fruit', 'Quantity'])
print(' '.join(example_reader.fieldnames))
for row in example_reader:
    print('#%s:' % (example_reader.line_num-1), row['Timestamp'], row['Fruit'], row['Quantity'])
example_csv_WITHOUT_header.close()
"""

# CSV Dict Writer - how to write and add a header (the first step of writing down to the file)
"""
output_csv_with_header = open('outputWithHeader.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_csv_with_header, fieldnames=['Cell1', 'Cell2', 'Cell3', 'Cell4'])
output_dict_writer.writeheader()
print(output_dict_writer.writerow({'Cell1':'cell1', 'Cell2':'cell2', 'Cell3':'cell3', 'Cell4':'cell4'}))  # 20 + 3x, + cr + lf
print(output_dict_writer.writerow({'Cell2':'eth', 'Cell3':'ath', 'Cell4':'nth', 'Cell1':'sth'}))  #
output_csv_with_header.close()
"""


