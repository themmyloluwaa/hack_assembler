# Hack Assembler (2 Pass Assembler)

This project translates code written in Hack assembly language into machine language by following the specifications of the hack assembly language. At the basic form, the hack assembly language supports two types of instructions

- A instructions that begin with a `@` e.g. `@0`. In machine code, A instructions start with 0.
- C instruction that have the format `dest = comp; jmp` where `dest` is the destination, `comp` is the computation to be stored in the destination and `jmp` refers to jump popularly known as `goto`. Each of these components have a table that maps each type of statement to the equivalent machine instruction. Please check `util.py` for the following `comp_table, dest_table, jump_table`. In machine code, C instructions start with 111.

The hack assembly language also supports symbols which are syntatic sugars made available to the developer to support code reusability and readability. These symbols are classified into

- Predefined variables e.g. R0 - R15, THIS, THAT, SCREEN etc.
- Labels used to classify a group of instructions. A label instruction starts with a `(` and then can be used as `@` e.g. (LOOP) then @LOOP. It's important to note that the assembly language supports usage before declaration. Meaning that you could come across @LOOP first then see the (LOOP) declaration at a later time.
- Variables -> any none digit A instruction that doesn't belong to the two categories of symbols above is classified as a variable. Variables in hack assembly code start from address 16 and goes up from there.

## Components

As this is a two pass assembler, the first pass extracts all label declarations into a `symbol table` that contains the predefined variables. The second pass then translates the intructions and if it encounters variables, it adds it into the symbol table if it wasn't present previously. Additionally, the assembler is expected to ignore white spaces and comments and I achieve that by first parsing the input file and performing some cleanup. The symbol table contains a key value pair of symbol -> address which is used in the translation process

### HackAssembler.py

Handles initialisation of each component, orchestration and cleanup. Accepts a hack assemble file with the extension `.asm`.

### Parser

Recieves the file and handles removing whitespaces, comments and produces a temporary `Parser.asm` file that contains the clean file.

### SymbolHandler

Recieves the output of the `Parser` component and extracts all label declarations from it into a symbol table. During initialisation, it adds the predefined tables to the symbol table constructed. The symbol table is discarded once the translation is done. This is the component that handles the first pass of the translation process.

### Translator

Recieves the output of the `Parser` component and handles translation of the code into machine language. By combining the symbol table constructed by the `SmybolHandler` component and the `comp, dest, jump` tables, it achieves translation by following the following steps.

- If A instruction, if the instruction is not a digit e.g. R0, look up symbol table. If it's not present in symbol table, then it's a variable. Add it into the symbol table with the variable as the key and the next variable address e.g. `16` as the value. Translate the value into the binary form and write it into the file.
- If C instruction, extract the 3 fields. Loop up the values in their corresponding tables and write it into a file.
- Repeat the first two steps above until you reach the end of the file.
- Save the output with extension `.hack`.

## Conclusion

I really learnt a lot from taking the [Nand2Tetris part 1](https://www.coursera.org/learn/build-a-computer) course and I'd recommend it to anyone who wants to understand how things work under the hood.

If you have questions or suggestions, please do not hesitate to reach out.
