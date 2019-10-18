from dataList import DList
from dataSet import DSet
from sympy import *
import numpy
import math
import genericFunctions
from sympy.parsing.sympy_parser import parse_expr
#from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr
#init_printing(use_unicode=True)
import re

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#creation of the dictionari that will contain all the dataSet
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
        elif line[0] == 'PLOT':
            #print('--Hello')
            for j in range(i,len(file)):
                newLine = file[j].split()
                if newLine[0] == 'END':
                    info = file[i:j]
                    newPlot(info)
                    break

def newData(data):
    names = data[0].split()
    if names[1] not in dataSet_dict:
        dataSet_dict[names[1]] = DSet(names[1])
    dataSet = dataSet_dict[names[1]]
    num = len(data[1:])
    for i in range(0,len(names[2:]),2):
        dataSet._set.append(DList(names[i+2], names[i+3]))
        #print(dataSet._set[int(i/2)]._name)  
        dataSet._set[int(i/2)]._valueList = np.zeros(num)
        dataSet._set[int(i/2)]._errorList = np.zeros(num)
    for i in range(num):
        value = data[i+1].split()
        print('--',value)
        #for j in range(len(dataSet._set)):
        #    print('--',j)
        for n in range(0,len(value),2):
            #print(n, dataSet._set[int(n/2)]._name)
            if value[n+1] == '#':
                dataSet._set[int(n/2)]._valueList[i] = value[n]
            else:
                dataSet._set[int(n/2)]._valueList[i] = value[n]
                dataSet._set[int(n/2)]._errorList[i] = value[n+1]
    #print(dataSet._set[int(0)]._valueList, dataSet._set[0]._errorList)

def printData(set):
    for j in range(len(set)):
        dataSet = dataSet_dict[set[j]]
        #print(dataSet._set)
        for i in dataSet._set:
            print(i._name, ' ', i._unit, '\t\u03C3Err(', i._name, ')', end = '\t')
        print()
        for n in range(len(dataSet._set[0]._valueList)):
            #print(len(dataSet._set[0]._list))
            for i in range(len(dataSet._set)):
                #print('--', n)
                #print('##',dataSet._set[i]._list)
                #print(dataSet._set[i]._list[n]._value)
                print(dataSet._set[i]._valueList[n], '\t', dataSet._set[i]._errorList[n], end = '\t')
            print()

def startAnalisy(null):
    for i in dataSet_dict:
        for j in dataSet_dict[i]._set:
            Symbol(j._name +'_s')

def function(expr):
    #select the correct data set
    dataSet = dataSet_dict[expr[0]] 
    num = len(dataSet._set[0]._valueList)
    #create a new DList to contain the new calculated value
    newDList = DList(expr[1])
    newDList._valueList = np.zeros(num)
    newDList._errorList = np.zeros(num)
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
                expr = re.sub(j._name,j._name+'_s',expr)
                variable.append(j._name+'_s')
                errVariable.append(j._name+'_s')
                errVariable.append(str(j._name+'_s') + '_error')
        for n in variable:
            expr1 = expr1 + '((' + str(diff(expr, n)) + ')' + '*(' + str(n) + '_error)**2)' + ' + '
    expr1 = ' '.join(expr1.split(' ')[:-2]) + ')'
    print(expr)
    print(expr1)
    #creates the solvable expressions for sympy using numpy   
    variable_dict = {}
    errVariable_dict = {}
    func = parse_expr(expr)
    func1 = parse_expr(expr1)
    for j in range(num):
        for i in variable:
            variable_dict[i] = dataSet._set[0]._valueList[j]
        for i in errVariable:
            if '_error' not in i:
                errVariable_dict[i] = dataSet._set[0]._valueList[j]
            else: 
                errVariable_dict[i] = dataSet._set[0]._errorList[j]
        #print(func.evalf(subs=variable_dict))
        #print(func1)
        #print(func1.evalf(subs=errVariable_dict))
        newDList._valueList[j] = func.evalf(subs=variable_dict)
        newDList._errorList[j] = func1.evalf(subs=errVariable_dict)
    #print(variable_dict)
    #print(errVariable_dict)
    #print(newDList._list)
    #print(newDList._valueList)
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
        
def newPlot(info):
    #print(info[0].split()[1])
    dataSet = dataSet_dict[info[0].split()[1]]
    #print(dataSet._name)
    title = info[1]
    title1 = ''.join(info[1].split())
    #print(title) 
    yname = info[3].split()[0] + ' ('
    ylabel = info[3].split()[1]
    #print(yname)
    for i in range(len(dataSet._set)):
        if dataSet._set[i]._name == info[2].split()[1]:
            y = dataSet._set[i]._valueList
            yname += dataSet._set[i]._unit
            yname += ')'
            #print(y)
    np.asarray(y)
    xname = info[2].split()[0] + ' ('
    #print(xname)
    for i in range(len(dataSet._set)):
        if dataSet._set[i]._name == info[3].split()[2]:
            x = dataSet._set[i]._valueList
            xname += dataSet._set[i]._unit
            xname += ')'
            #print(x)
    x = np.asarray(x)
    #print('y ',y)
    #print('x ', x)
    #title1 = ' '.join(info[3:])
    #title2 = ''.join(info[3:])
    plt.plot(x,y,label=ylabel)
    plt.title(title)
    plt.xlabel(xname)
    plt.ylabel(yname)
    #if len(info) > 3:   
    plt.grid()
    plt.legend()
    plt.savefig(title1)
    #plt.show()
    '''
    ax.set(xlabel= xname, ylabel= yname,
        title= title1)
    ax.grid()

    fig.savefig(title2+".png")
    plt.show()
    '''
functionDict = {'PRINTDATA': printData, 'STARTANALISY': startAnalisy, 'FUNCTION': function}
#add ability to create custom dataSets  
