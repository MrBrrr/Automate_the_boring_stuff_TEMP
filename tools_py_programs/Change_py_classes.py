import re

class pattern_repl():
    pattern_print_parenthesis = r'(print)(\ )(.*?)(\n)'
    repl_print_parenthesis = r'\1(\3)\4'
    #pattern_print_ffromat =
    #repl_print_ffromat =
    pattern_comma =
    def __init__(self, own_pattern, own_repl):
        self.

    def print_parenthesis(self):
        pattern = r'(print)(\ )(.*?)(\n)'
        repl = r'\1(\3)\4'
        re.sub(pattern, repl, string_to_sub)