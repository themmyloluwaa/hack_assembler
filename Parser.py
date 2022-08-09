from tempfile import TemporaryFile
import os
class Parser:
    def __init__(self, file):
        self.file = file;
        self.output = "parser.asm"
    def parse(self):
        temp = TemporaryFile('w+t')
        with open(self.file, 'r') as f:
            for l in f:
                line = l.strip()
                if line.startswith('//') or line == "":
                    continue
                line = line.split('//')[0]
                temp.write(line + '\n')
            f.close()
        temp.seek(0)
        with open(self.output, 'w') as f:
            for line in temp:
                f.write(line)
            f.close()
        temp.close()
    def cleanup(self):
        if os.path.isfile(self.output):
            os.remove(self.output)
        print('Parser cleanup complete.')
