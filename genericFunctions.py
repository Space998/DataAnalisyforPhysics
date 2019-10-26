import sys
import os
import re

def checkFile():
    """Checks if the file containing the data and the instruction for the analisy exists, if so returns it otherwise kills the program"""
    if len(sys.argv) != 2:
        sys.exit("ERROR: No file indicated")
    else:
        if os.path.isfile(sys.argv[1]):
            file = open(sys.argv[1], 'r')
            line = file.readline()
            if line.split()[0] == "DATA" and line.split()[1] == "ANALISY":
                return file #return file
            else:
                sys.exit("ERROR: The input file is not formatted correctly for the data analisy")
        else:
            sys.exit("ERROR: The specified path doesn't lead to a file")

def formatFile(originalFile):
    """Return a object containing only the information needed by the program/interpreter for the data analisy. 
    Opens the file specified by the user and formats it by removing all the comments and the blank lines, then returns a list whose elements are the lines of the formatted file."""
    originalFile = originalFile.read()
    
    #originalFile = originalFile.replace('@@', '\n@@')             
    originalFile = re.sub(r"@@#","\n@@# \n ",originalFile)        #start to eliminate multiline comments
    originalFile = re.sub(r"#@@","\n#@@ \n ",originalFile)        #start to eliminate multiline comments
    originalFile = re.sub(r"@@#[\s\S]*?#@@","",originalFile)     #eliminate multiline comments  
    print(originalFile)
    originalFile = re.sub(r"@@","\n@@ ",originalFile)            #eliminates inline comments 
    originalList= originalFile.split('\n')                      #create a list by splitting the file at the end of the lines
    

    program = list(filter(lambda x: not re.match(r'^\s*$', x) and not x.startswith('@@ '),originalList))         #eliminates the comments and the empty lines
    
    return program

