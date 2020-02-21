tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
'''
list = 0,1,2
element[list] = 0,1,2,3
'''
def printTable(list_of_lists):
    max_len = 0
    for column_nr in range(len(list_of_lists), -1, 0):
        for small_list in list_of_lists:
            elem_len = len(small_list[column_nr])
            if max_len < elem_len:
                max_len = elem_len
            print str(small_list[column_nr]) + str(elem_len) + str(max_len)

        for small_list in list_of_lists:
            small_list[column_nr].rjust(max_len+3)
            print str(small_list[column_nr])
    print ':)'


printTable(tableData)
print str(tableData)





