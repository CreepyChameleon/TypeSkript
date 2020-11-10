import ast
import random
from datetime import datetime

global globalVariables
globalVariables = {}

lastLineIfFalse = bool
looping = False
firstrun = True

def interpret(script="//"):
    global lastLineIfFalse
    global looping
    global firstrun
    # if a comment
    if script[:2] == "//": 
        pass
    # if an empty line
    elif script == "\n":
        pass
    scriptWords = script.split(' ')
    if scriptWords[0].lower() == 'firstrun':
        if firstrun:
            scriptWords.pop(0)
        else:
            pass
    # if an if statement
    if scriptWords[0].lower() == 'if':
        
        ic = Conditionals().ifCondition(scriptWords)
        if ic:   
            if scriptWords[10] == 'then':
                for _ in range(11):
                    scriptWords.pop(0)
            lastLineIfFalse = False
        elif ic == False:
            lastLineIfFalse = True
        else:
            raise Exception("If Statement Error")
    # if an else statement
    elif scriptWords[0].lower() == 'else':
        if lastLineIfFalse:
            lastLineIfFalse = False
            scriptWords.pop(0)
    # if not if or else statements
    else:
        lastLineIfFalse = False
    # if a variable fuction
    if scriptWords[0].lower() == 'the' and scriptWords[1].lower() == 'variable':
        # if setting a variable
        if scriptWords[3:6] == ['is', 'equal', 'to']:
            # if an input
            if scriptWords[7] == 'input':
                vName = scriptWords[2]
                for _ in range(8):
                    scriptWords.pop(0)
                s = Functions().buildString(scriptWords)
                #s =  ast.literal_eval(s)
                i = Functions().fixType(input(s))
                if str(type(i)) == "<class 'int'>":
                    vType = 'integer'
                elif str(type(i)) == "<class 'string'>":
                    vType = 'string'
                elif str(type(i)) == "<class 'boolean'>":
                    vType = 'boolean'
                elif str(type(i)) == "<class 'float'>":
                    vType = 'float'
                else:
                    vType = 'string'
                Functions().setVar(vName, vType, i)
            # if a random
            elif scriptWords[7] == 'random':
                name = scriptWords[2]
                Type = scriptWords[8]
                if Type == 'integer':
                    if scriptWords[9] == 'between':
                        a = int(scriptWords[10])
                        b = int(scriptWords[12])
                        r = random.randint(a, b)
                        Functions().setVar(name, Type, r)

            # if a string
            elif scriptWords[7] == 'string':
                vName = scriptWords[2]
                vType = 'string'
                for _ in range(8):
                    scriptWords.pop(0)
                s = Functions().buildString(scriptWords)
                Functions().setVar(vName, vType, s)
            else:
                Functions().setVar(scriptWords[2], scriptWords[7], scriptWords[8])
        elif scriptWords[3:6] == ['is', 'increased', 'by']:
            ### if specifying integer or float
            try:
                # if adding an integer
                if scriptWords[7] == 'integer':
                    Functions().addNumToVar(scriptWords[2], int(scriptWords[8]))
                # if adding a float
                elif scriptWords[7] == 'float':
                    Functions().addNumToVar(scriptWords[2], float(scriptWords[8]))
                # if adding a variable
                elif scriptWords[7] == 'variable':
                    Functions().addNumToVar(scriptWords[2], globalVariables[Functions().handleReturn(scriptWords[8])]['value'])
            ### no specification of number type
            except:
                if '.' in scriptWords[6]: # if a float
                    Functions().addNumToVar(scriptWords[2], float(scriptWords[6]))
                else:
                    Functions().addNumToVar(scriptWords[2], int(scriptWords[6]))
        elif scriptWords[3:6] == ['is', 'decreased', 'by']:
            ### see increased
            try:
                if scriptWords[7] == 'integer':
                    Functions().subNumFromVar(scriptWords[2], int(scriptWords[8]))
                elif scriptWords[7] == 'float':
                    Functions().subNumFromVar(scriptWords[2], float(scriptWords[8]))
                elif scriptWords[7] == 'variable':
                    Functions().addNumToVar(scriptWords[2], globalVariables[Functions().handleReturn(scriptWords[8])]['value'])
            except:
                if '.' in scriptWords[6]:
                    Functions().subNumFromVar(scriptWords[2], float(scriptWords[6]))
                else:
                    Functions().subNumFromVar(scriptWords[2], int(scriptWords[6]))
        elif scriptWords[3:6] == ['is', 'multiplied', 'by']:
            ### see increased
            try:
                if scriptWords[7] == 'integer':
                    Functions().multVar(scriptWords[2], int(scriptWords[8]))
                elif scriptWords[7] == 'float':
                    Functions().multVar(scriptWords[2], float(scriptWords[8]))
                elif scriptWords[7] == 'variable':
                    Functions().addNumToVar(scriptWords[2], globalVariables[Functions().handleReturn(scriptWords[8])]['value'])
            except:
                if '.' in scriptWords[6]:
                    Functions().multVar(scriptWords[2], float(scriptWords[6]))
                else:
                    Functions().multVar(scriptWords[2], int(scriptWords[6]))
        elif scriptWords[3:6] == ['is', 'divided', 'by']:
            ### see increased
            try:
                if scriptWords[7] == 'integer':
                    Functions().divVar(scriptWords[2], int(scriptWords[8]))
                elif scriptWords[7] == 'float':
                    Functions().divVar(scriptWords[2], float(scriptWords[8]))
                elif scriptWords[7] == 'variable':
                    Functions().addNumToVar(scriptWords[2], globalVariables[Functions().handleReturn(scriptWords[8])]['value'])
            except:
                if '.' in scriptWords[6]:
                    Functions().divVar(scriptWords[2], float(scriptWords[6]))
                else:
                    Functions().divVar(scriptWords[2], int(scriptWords[6]))
    # if a static variable
    if scriptWords[0].lower() == 'the' and scriptWords[1].lower() == 'staticvariable':
        if scriptWords[2] in globalVariables.keys():
            pass
        else:
            # if setting a variable
            if scriptWords[3:6] == ['is', 'equal', 'to']:
                # if an input
                if scriptWords[7] == 'input':
                    vName = scriptWords[2]
                    for _ in range(8):
                        scriptWords.pop(0)
                    s = Functions().buildString(scriptWords)
                    #s =  ast.literal_eval(s)
                    i = Functions().fixType(input(s))
                    if str(type(i)) == "<class 'int'>":
                        vType = 'integer'
                    elif str(type(i)) == "<class 'string'>":
                        vType = 'string'
                    elif str(type(i)) == "<class 'boolean'>":
                        vType = 'boolean'
                    elif str(type(i)) == "<class 'float'>":
                        vType = 'float'
                    else:
                        vType = 'string'
                    Functions().setVar(vName, vType, i)
                # if a random
                elif scriptWords[7] == 'random':
                    name = scriptWords[2]
                    Type = scriptWords[8]
                    if Type == 'integer':
                        if scriptWords[9] == 'between':
                            a = int(scriptWords[10])
                            b = int(scriptWords[12])
                            r = random.randint(a, b)
                            Functions().setVar(name, Type, r)

                # if a string
                elif scriptWords[7] == 'string':
                    vName = scriptWords[2]
                    vType = 'string'
                    for _ in range(8):
                        scriptWords.pop(0)
                    s = Functions().buildString(scriptWords)
                    Functions().setVar(vName, vType, s)
                else:
                    Functions().setVar(scriptWords[2], scriptWords[7], scriptWords[8])
    # if a print statement
    elif scriptWords[0].lower() == 'print':
        if scriptWords[1:3] == ['the', 'variable']:
            if '\n' in scriptWords[3]:
                key = scriptWords[3].strip('\n')
                print(globalVariables[key]['value'])
            else:
                print(globalVariables[scriptWords[3]]['value'])
        elif scriptWords[1:3] == ['the', 'string']:
            print(Functions().buildString(scriptWords[3:]))
        elif scriptWords[1:3] == ['the', 'integer']:
            print(int(scriptWords[3]))
        elif scriptWords[1:3] == ['the', 'float']:
            print(float(scriptWords[3]))
        elif scriptWords[1:3] == ['the', 'boolean']:
            print(bool(scriptWords[3]))
    # if a get statement
    elif scriptWords[0].lower() == 'get':
        # get the type of a variable
        if scriptWords[2] == 'type':
            print(globalVariables[Functions().handleReturn(scriptWords[6])]['type'])
        # get the current time
        elif scriptWords[2] == 'time':
            if len(scriptWords) == 3:
                print(datetime.now())
            elif len(scriptWords) == 4:
                frmt = scriptWords[3]
                frmt = list(frmt)
                frmtlst = []
                for i in range(len(frmt)):
                    if frmt[i].lower() == 'd':
                        frmtlst.append('%d')
                    elif frmt[i].lower() == 'm':
                        frmtlst.append('%m')
                    elif frmt[i].lower() == 'y':
                        frmtlst.append('%Y')
                time = datetime.now()
                print(time.strftime('/'.join(frmtlst)))
    # if an interpret statement
    elif scriptWords[0].lower() == 'interpret':
        # if interpreting python
        if scriptWords[1].lower() == 'python':
            for _ in range(2):
                scriptWords.pop(0)
            s = Functions().buildString(scriptWords)
            print(s)
            exec(s)
    if scriptWords[0] == 'loop' or scriptWords[0] == 'loop\n':
        looping = True
    if scriptWords[0] == 'stop' or scriptWords[0] == 'stop\n':
        looping = False
        exit()

################
# Conditionals #
################
class Conditionals:
    def ifCondition(self, wordList = []):
        if wordList[2] == 'variable':
            arg1 = globalVariables[wordList[3]]['value']
            # checking types of second argument
            if wordList[8] == 'integer':
                arg2 = int(wordList[9])
            elif wordList[8] == 'float':
                arg2 = float(wordList[9])
            elif wordList[8] == 'string':
                arg1 = Functions().buildString(arg1.split())
                arg2 = Functions().buildString(str(wordList[9]).split())
            elif wordList[8] == 'boolean':
                arg1 = globalVariables[wordList[3]]['value']
                arg2 = Functions().stringToBool(wordList[9])
            elif wordList[8] == 'variable':
                arg2 = globalVariables[wordList[9]]['value']
            else:
                arg2 = None
            
            # if comparing for equality
            if wordList[4:7] == ['is', 'equal', 'to']:
                try:
                    if arg1 == arg2:
                        return True
                    else:
                        return False
                except:
                    if globalVariables[arg1]['value'] == arg2:
                        return True
                    else:
                        return False
            # if checking for greater than
            elif wordList[4:7] == ['is', 'greater', 'than']:
                print(arg1, arg2)
                if arg1 > arg2:
                    return True
                else:
                    return False
            # if checking for less than
            elif wordList[4:7] == ['is', 'less', 'than']:
                if arg1 < arg2:
                    return True
                else:
                    return False

#############
# Functions #
#############
class Functions:
    def handleReturn(self, string):
        return string.strip('\n')

    def setVar(self, varName, varType, varValue):
        # add variable to a dictionary with its assignments
        if varType == 'integer':
            globalVariables[varName] = {'type':varType, 'value':int(varValue)}
        elif varType == 'float':
            globalVariables[varName] = {'type':varType, 'value':float(varValue)}
        elif varType == 'string':
            globalVariables[varName] = {'type':varType, 'value':str(varValue)}
        elif varType == 'boolean':
            globalVariables[varName] = {'type':varType, 'value':Functions().stringToBool(varValue)}
        elif varType == 'input':
            globalVariables[varName] = {'type':varType, 'value':varValue}
        else:
            Errors().typeError(varType)

    def addNumToVar(self, baseVarName, addVal):
        globalVariables[baseVarName]['value'] += addVal

    def subNumFromVar(self, baseVarName, subVal):
        globalVariables[baseVarName]['value'] -= subVal

    def multVar(self, baseVarName, multVal):
        globalVariables[baseVarName]['value'] *= multVal

    def divVar(self, baseVarName, divVal):
        globalVariables[baseVarName]['value'] /= divVal

    def buildString(self, wordList = []):
        string = ' '.join(wordList)
        if len(string) > 1:
            s = string.split()
            l = len(s)
            if s[-2:] == ['\\', 'n']:
                s.pop(l)
        string = ast.literal_eval(string)
        return string

    def fixType(self, string):
        try:
            string = ast.literal_eval(string)
            if string == 'true':
                string = True
            elif string == 'false':
                string = False
            return string
        except:
            if string == 'true':
                string = True
            elif string == 'false':
                string = False
            return string

    def stringToBool(self, string):
        string = Functions().handleReturn(string)
        if string == 'true' or string == 'True':
            return True
        elif string == 'false' or string == 'False':
            return False
        else:
            Errors().boolError(string)

##########
# Errors #
##########
class Errors:
    def typeError(self, Type=''):
        raise TypeError(f'"{Type}" is not an acceptable type')
    
    def boolError(self, Bool=''):
        raise TypeError(f'"{Bool}" is not an acceptable boolean value')
