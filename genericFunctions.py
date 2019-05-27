import sys
import os

def checkFile():
    """Checks if the file containing the data and the instruction for the analisy exists, if so returns it otherwise kills the program"""
    if len(sys.argv) != 2:
        sys.exit("No file indicated")
    else:
        if os.path.isfile(sys.argv[1]):
            file = open(sys.argv[1], 'r')
            line = file.readline()
            if line.split('\n')[0] == "DATA ANALISY":
                return sys.argv[1]
                file.close()
            else:
                sys.exit("The input file is not formatted correctly for the data analisy")
        else:
            sys.exit("The specified path doesn't lead to a file")
