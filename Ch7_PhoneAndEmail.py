import pyperclip, re

phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?              # area code - xxx or (xxx) or null
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension - could be nothing
    ''', re.VERBOSE)
string_to_search = str(pyperclip.paste())
phones_numbers = []

list_of_phones = phoneRegex.findall(str(string_to_search))
# print str(list_of_phones)
for groups in list_of_phones:
    if groups[0] != '':
        areaRegex = re.compile(r'(\(?)(\d{3})(\)?)')
        phone_number = '-'.join([areaRegex.sub(r'\2',groups[0]),groups[2],groups[4]])
    else:
        phone_number = '-'.join([groups[2],groups[4]])
    if groups[5] != '':
        extRegex = re.compile(r'\s*(ext|x|ext\.)\s*(\d{1,})')
        phone_number = ' '.join([phone_number,extRegex.sub(r'ext. \2',groups[5])])

    # print phone_number
    phones_numbers.append(phone_number)
# print phones_numbers

emailRegex = re.compile(r'''
    \s([a-zA-Z0-9\_\!\$\+\=\-\&\^]+)   # user name - one or more alphanumerical signs plus sth ._%\-+ lub !\#$%&'*/=?^_`{|}~.+-
    (@)                                   # at - have to be
    ([a-zA-Z0-9]+)   # domain
    (\.)                                   # dot - have to be
    ([a-zA-Z]{2,4})# something - have to be 2 up to 4 alfabertical
    ''', re.VERBOSE)
emails_addresses = []

list_of_emails = emailRegex.findall(str(string_to_search))
# print list_of_emails

for groups in list_of_emails:
    # print ':)' + str(groups)
    email_addres = ''.join([groups[0],groups[1],groups[2],groups[3],groups[4]])
    emails_addresses.append(email_addres)            
# print emails_addresses

matches = phones_numbers + emails_addresses

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


# list_of_emails = emailRegex.findall(string_to_search)
# matches = [list_of_phones, list_of_emails]
