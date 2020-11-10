"""
TypeSkript

A relatively simplistic programming language
that aims to allow understanding for those
without programming knowledge

Version: 1.09

TODO:
Rock paper scissors

Bugs:

"""

import os
import sys
import interpreter

cwd = os.getcwd()
n = "rps.tskr"

def parse(fileName='help.tskr'):
    if fileName.endswith('.tskr'): # checks the file extension
        fileLoc = cwd + "\\" + fileName
        scrSize = open(fileLoc, "r")
        fileSize = len(scrSize.readlines()) # gets number of lines in script
        boot = True

        # interprets script by each line
        while interpreter.looping or boot:
            boot = False
            scr = open(fileLoc, "r")
            for _ in range(fileSize):
                interpreter.interpret(scr.readline())
            interpreter.firstrun = False
    else:
        raise Exception('Cannot parse file')

try:
    if __name__ == '__main__':
        globals()[sys.argv[1]](sys.argv[2])
except:
    parse('rps.tskr')