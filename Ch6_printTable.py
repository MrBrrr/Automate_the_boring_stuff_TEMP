#!python

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
'''
list = 0,1,2
element[list] = 0,1,2,3
'''
def printTable(list_of_lists):
    for column_nr in range(len(list_of_lists[0])):
        max_len = 0
        for small_list in list_of_lists:
            elem_len = len(small_list[column_nr])
            if max_len < elem_len:
                max_len = elem_len
            #print str(small_list[column_nr]) + str(elem_len) + str(max_len)

        for list_nr in range(len(list_of_lists)):
            list_of_lists[list_nr][column_nr] = list_of_lists[list_nr][column_nr].rjust(max_len+3)
            #print list_of_lists[list_nr][column_nr]
            
    for small_list in list_of_lists:
        one_line = ''
        for element in small_list:
            one_line = one_line + element
        #one_line += '\n'
        print one_line


printTable(tableData)
#print str(tableData)
