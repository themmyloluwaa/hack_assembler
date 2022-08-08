
from curses.ascii import isalpha
from util import default_variables


class SymbolHandler:
    def __init__(self):
        self.symbol_table = default_variables

    def pass_one(self, file):
        with open(file, 'r') as f:
            i = 0
            for l in f:
                line = l.strip()
                if line.startswith('('):
                    label = line[1:-1]
                    self.symbol_table[label] = i
                else:
                    i += 1
            f.close()
