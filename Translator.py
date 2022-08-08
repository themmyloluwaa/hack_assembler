from curses.ascii import isalnum
from SymbolHandler import SymbolHandler
from util import dest_table, comp_table, jump_table
from tempfile import TemporaryFile


class Translator:
    def __init__(self, smybolHandler: SymbolHandler, output: str):
        self.symbolHandler = smybolHandler
        self.temp = TemporaryFile('w+t')
        self.output = output
        print(output)

    def translate(self, file):
        with open(file, 'r') as f:
            i = 16
            for l in f:
                line = l.strip()
                if line.startswith('('):
                    continue
                if line.startswith('@'):
                    label = line[1:]
                    if not label.isdigit() and label not in self.symbolHandler.symbol_table:
                        self.symbolHandler.symbol_table[label] = i
                        i += 1
                    res = self.__handleAInstruction(line)
                    self.temp.write(res + '\n')
                else:
                    res = self.__handleCInstruction(line)
                    self.temp.write(res + '\n')
            f.close()
        self.temp.seek(0)
        with open(self.output, 'w') as f:
            for line in self.temp:
                f.write(line)
            f.close()
        self.temp.close()

    def __handleAInstruction(self, instruction: str):
        temp = instruction[1:]
        binary_code = None
        if temp.isdigit():
            binary_code = bin(int(temp))
        else:
            value = self.symbolHandler.symbol_table[temp]
            binary_code = bin(value)
        binary_code = binary_code.replace('b', '0')

        if len(binary_code) > 16:
            binary_code = binary_code[1:]
        else:
            binary_code = "0" * (16 - len(binary_code)) + binary_code
        return binary_code

    def __handleCInstruction(self, instruction: str):
        res = ""
        jmpInstruction = instruction.split(';')
        jmp = None
        if len(jmpInstruction) > 1:
            jmp = jmpInstruction[-1]
        dest = None
        destInstruction = jmpInstruction[0].split('=')
        if len(destInstruction) > 1:
            dest = destInstruction[0]
        comp = destInstruction[-1]
        res = "111" + comp_table[comp] + dest_table[dest] + jump_table[jmp]

        return res
