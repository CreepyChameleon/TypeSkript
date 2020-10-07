"""
TypeSkript

A relatively simplistic programming language
that aims to allow understanding for those
without programming knowledge

Version: 1.06

TODO:

"""

import os
import interpreter

cwd = os.getcwd()
fileLoc = cwd + "\\" + "testProgram.tskr"
scr = open(fileLoc, "r")
scrSize = open(fileLoc, "r")
fileSize = len(scrSize.readlines()) # gets number of lines in script

# interprets script by each line
for _ in range(fileSize):
    interpreter.interpret(scr.readline())