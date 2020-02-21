import re

reg_num = re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs).',re.I)



lancuch = 'Alice eats apples.'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch = 'Bob pets cats.'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch =  'Carol throws baseballs.'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch = 'Alice throws Apples.'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch = 'BOB EATS CATS.'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch = 'Robocop eats apples.'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch = 'ALICE THROWS FOOTBALLS.'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
lancuch = 'Carol eats 7 cats.'
if(reg_num.search(lancuch)):print reg_num.search(lancuch).group()
