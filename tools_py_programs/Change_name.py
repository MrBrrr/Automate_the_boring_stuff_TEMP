#! python
# Change names of chosen files in current directory


def main():
    import os, re
    re_obj = re.compile(
        r'(Ch)'
        r'(\d{1,2})'
        r'(\_.*?\.py)')
    # lub r'(Ch)(\d{1,2})(\_.*?\.py)')
    # lub '(Ch{1})(\\d{1,2})(_.*?\\.py)')

    wrong_file_names = re_obj.findall(str(os.listdir()))

    print(wrong_file_names)

    for file_name in wrong_file_names:
        good_file_name = list(file_name)
        good_file_name[0] = 'Ch'
        print(good_file_name)
        os.rename(''.join(file_name), ''.join(good_file_name))


if __name__ == '__main__': main()
