

def comma_code(passed_list):
    inner_string = passed_list[0]
    if len(passed_list) > 2:
        for i in passed_list[1:-1]:
            inner_string = inner_string + ', ' + i
    if len(passed_list) > 1:
        inner_string = inner_string + ' and ' + passed_list[-1]
    else:
        inner_string = inner_string + ' and nothing else'
    return inner_string


spam = ['apples', 'bananas', 'tofu', 'cats']

one_string = comma_code(spam)
print(one_string)
