#! python
# An insecure password locker program
import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Choose an account')
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(str(PASSWORDS[account]))
    print('Password in clipboard, you can paste it')

else:
    print 'There is no account named ' + str(account) + \
    'Type down the password or leave blank to exit'
    password = input()
    if password == '':
        sys.exit()
    else:
        PASSWORDS[str(account)] = str(password)

        print 'New account added (at real not ;) I don\'t know how to change the dict holding passwords'
