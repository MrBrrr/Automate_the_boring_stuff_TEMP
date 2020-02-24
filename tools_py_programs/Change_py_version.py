#! python
# Change version of python programs
# 2 to 3


def main():
    import re, os
    os.chdir(os.path.dirname(os.getcwd()))
    print(os.getcwd())

    # take each .py file
    #
    re_py = re.compile(r'Ch\d{1,2}\_.*?\.py'    )
    files_to_check = re_py.findall(str(os.listdir()))
    print(files_to_check)

    print_pattern = r'(print)(\ )(.*?)(\n)'
    # print 'str'
    # print var
    print_repl = r'\1(\3)\4'
    # --> print(<sth>)\n

    # to musi być w for - każdą linijkę sprawdzam wielokrotnie dopóty dopóki nie usunę wszystkich znaczników %
    # # a właściwie to sobie mogę stworzyć klasę - ale na razie siana se dam :)
    print_fformat1_pattern = r'(print\(.*?)(%\ \w{1})(.*?)(%\ \w+)(\,?)'
    # print(<"jakies znaki wraz ze spacja równeż f">
    # % x
    # <jakies inne znaki>
    # % <nazwa zmiennej azAZ09_>
    # <ewentualny przecinek>
    # w pętli do while - dopóki linijka wczytywana jest równa linijce wynikowej, wykorzystanie re.sub(:)

    comma_pattern = r''
    colon_pattern = r'(:)(\w|\'|\")'
    colon_repl = r': \2'

    for file in files_to_check[:2]:
        print(f'opening {file}')
        file_handler = open(file, 'r')
        # ...

        print(f'closing {file}')
        file_handler.close()



if __name__ == '__main__': main()
