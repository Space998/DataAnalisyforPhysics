from dataErr import Data
from dataList import DList
from dataSet import DSet
from sympy import *
import numpy
import math
import genericFunctions
#from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr
#init_printing(use_unicode=True)

dataSet_dict = {}

def operation(file):
    for i in range(len(file)):
        line = file[i].split()
        if line[0] in functionDict:
            #print('-',line[0])
            functionDict[line[0]](line[1:])
        elif line[0] == 'NEWDATA':
            #print('--Hello')
            for j in range(i,len(file)):
                newLine = file[j].split()
                if newLine[0] == 'END':
                    data = file[i:j]
                    newData(data)
                    break
            #match = re.findall("NEWDATA([\s\w]*?)END", file)
            #print(match)

def newData(data):
    names = data[0].split()
    if names[1] not in dataSet_dict:
        dataSet_dict[names[1]] = DSet(names[1])
    dataSet = dataSet_dict[names[1]]
    for i in range(0,len(names[2:]),2):
        dataSet._set.append(DList(names[i+2], names[i+3]))
        #print(dataSet._set[i]._name)  
    for i in range(len(data[1:])):
        value = data[i+1].split()
        print('--',value)
        #for j in range(len(dataSet._set)):
        #    print('--',j)
        for n in range(0,len(value),2):
            #print(n, dataSet._set[int(n/2)]._name)
            if value[n+1] == '#':
                dataSet._set[int(n/2)]._list.append(Data(value[n]))
            else:
                dataSet._set[int(n/2)]._list.append(Data(value[n],value[n+1]))

def printData(set):
    for j in range(len(set)):
        dataSet = dataSet_dict[set[j]]
        #print(dataSet._set)
        for i in dataSet._set:
            print(i._name, ' ', i._unit, '\t\u03C3Err(', i._name, ')', end = '\t')
        print()
        for i in range(len(dataSet._set)):
            #rint(len(dataSet._set[0]._list))
            for n in range(len(dataSet._set[0]._list)):
                #print(dataSet._set[0]._list)
                #print('--', n)
                print(dataSet._set[i]._list[n]._value, '\t', dataSet._set[i]._list[n]._error, end = '\t')
            print()

def startAnalisy(null):
    for i in dataSet_dict:
        for j in dataSet_dict[i]._set:
            j._name = Symbol(j._name)

def function(expr):
    #select the correct data set
    dataSet = dataSet_dict[expr[0]] 
    #create a new DList to contain the new calculated value
    newDList = DList(expr[1], 'user')
    #collect the math function
    expr = expr[2:]
    expr = " ".join(expr)
    #print(expr)
    #define two list to contain the variables in wich the calculation will be made
    variable = []
    errVariable = []
    #creates the mathematical expression for the derivates -> this formula is the differential formula for error propagation
    expr1 = 'sqrt('
    for i in dataSet_dict:
        for j in dataSet_dict[i]._set:
            if str(j._name) in expr:
                expr1 = expr1 + '((' + str(diff(expr, j._name)) + ')' + '*(' + str(j._name) + '_error)**2)' + ' + '
                variable.append(j._name)
                errVariable.append(j._name)
                errVariable.append(str(j._name) + '_error')
    expr1 = ' '.join(expr1.split(' ')[:-2]) + ')'
    #creates the solvable expressions for sympy using numpy   
    variable_dict = {}
    errVariable_dict = {}
    for j in range(len(dataSet._set[0]._list)):
        for i in variable:
            variable_dict[i] = i._list[j]._value
        for i in errVariable:
            if '-_error' not in i:
                errVariable_dict[i] = i._list[j]._value
            else: 
                val = i.split('_')[0]
                errVariable_dict[i] = val._list[j]._error
        newDList._list.append(Data(expr.evalf(subs=variable_dict),expr1.evalf(subs=errVariable_dict)))
    dataSet._set.append(newDList)
    ''' 
    print(expr1)
    print(variable)
    print(variable_dict)
    print(errVariable) 
    print(errVariable_dict)
    func = lambdify(variable, expr, "numpy") 
    funcErr = lambdify(errVariable, expr1, "numpy")
    for i in range(len(variable)):
        for i in range(len(dataSet._set[0]._list)):
            newDList._list.append(Data(func(variable[i]._list[j]._value)))
    '''
        


functionDict = {'PRINTDATA': printData, 'STARTANALISY': startAnalisy, 'FUNCTION': function}
#add ability to create custom dataSets  