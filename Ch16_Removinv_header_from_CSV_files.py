#! python3

# # # # # # # # # # # # # # # # # # # # # # # # #
# Removes the header from .csv files
#
# 1. Search all the file in directory and choose those with .csv extention
#
#
#
#
#
# # # # # # # # # # # # # # # # # # # # # # # # #


import sys
import os
import re

try:
    new_path_list = sys.argv[1].split('/')
except IndexError:
    pass
    # new_path = os.getcwd()
else:
    new_path = os.path.join(new_path_list)
    os.chdir(new_path)

regex_obj = re.template('*.csv')



