import sys
from Parser import Parser
from SymbolHandler import SymbolHandler
from Translator import Translator


class HackAssembler:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.parser = Parser(file_path)
        self.symbolHandler = SymbolHandler()
        # output_file = file_path.split('.')[0] + ".hack"
        output_file = file_path.split('/')[-1].split('.')[0] + ".hack"
        self.translator = Translator(self.symbolHandler, output_file)

    def assemble(self):
        self.parser.parse()
        self.symbolHandler.pass_one(self.parser.output)
        self.translator.translate(self.parser.output)

        self.parser.cleanup()

        print('Successfully translated assembly code to machine code.')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Please supply the file to be translated.")
    file = sys.argv[1]
    if(not file.endswith('.asm')):
        raise ImportError('Assembly files must end with .asm')

    assembler = HackAssembler(file)
    assembler.assemble()
