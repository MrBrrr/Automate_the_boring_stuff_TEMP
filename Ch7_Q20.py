import re

reg_num = re.compile(r'^(\d{1,3})((,\d{3})*)$')
#reg_num = re.compile(r'(\d{1,3})([,\d{3}]*)')
lancuch = '1,242,543'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch = '1,242'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch = '43'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch = '1,24,2,54,3'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch = '24243'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
