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
    #print(num)
    for i in range(0,len(names[2:]),2):
        dataSet._set[names[i+2]] = DList(names[i+2], names[i+3])
        #print(dataSet._set[names[i+2]]._name)  
        dataSet._set[names[i+2]]._valueList = np.zeros(num)
        dataSet._set[names[i+2]]._errorList = np.zeros(num)
    for i in range(num):
        value = data[i+1].split()
        #print('--',value)
        #for j in range(len(dataSet._set)):
        #    print('--',j)
        j = 0
        for name in dataSet._set:
            #print(name)
            #print(j)
            #print(n, dataSet._set[int(n/2)]._name)
            if value[j+1] == '#':
                dataSet._set[name]._valueList[i] = value[j]
            else:
                dataSet._set[name]._valueList[i] = value[j]
                dataSet._set[name]._errorList[i] = value[j+1]
            j += 2
    #print(dataSet._set[int(0)]._valueList, dataSet._set[0]._errorList)

def printData(set):
    dataSet = dataSet_dict[set[0]]
    #print(dataSet._set)
    if len(set) == 1:
        for i in dataSet._set:
            print(dataSet._set[i]._name, ' ', dataSet._set[i]._unit, '\t\u03C3Err(', dataSet._set[i]._name, ')', end = '\t')
        print()
        for n in range(len(list(dataSet._set.values())[0]._valueList)):
            #print(len(dataSet._set[0]._list))
            for i in dataSet._set:
                #print('--', n)
                #print('##',dataSet._set[i]._list)
                #print(dataSet._set[i]._list[n]._value)
                print(dataSet._set[i]._valueList[n], '\t', dataSet._set[i]._errorList[n], end = '\t')
            print()

def startAnalisy(null):
    for i in dataSet_dict:
        #print(i)
        for j in dataSet_dict[i]._set:
            #print(j)
            #print(dataSet_dict[i]._set[j]._name)
            Symbol(dataSet_dict[i]._set[j]._name +'_s')

def function(expr):
    #select the correct data set
    dataSet = dataSet_dict[expr[0]] 
    num = len(list(dataSet._set.values())[0]._valueList)
    #create a new DList to contain the new calculated value
    if expr[2] == '#':
        newDList = DList(expr[1])
    else:
        newDList = DList(expr[1],expr[2])
    newDList._valueList = np.zeros(num)
    newDList._errorList = np.zeros(num)
    #collect the math function
    expr = expr[3:]
    expr = " ".join(expr)
    #print(expr)
    #define two list to contain the variables in wich the calculation will be made
    variable = []
    errVariable = []
    #creates the mathematical expression for the derivates -> this formula is the differential formula for error propagation
    for i in dataSet._set:
        #print(i)
        if i in expr:
            expr = re.sub(i,i+'_s',expr)
            variable.append(i+'_s')
            errVariable.append(i+'_s')
            errVariable.append(i+'_s'+ '_error')
    expr1 = 'sqrt('
    for n in variable:
        expr1 = expr1 + '((' + str(diff(expr, n)) + ')' + '*(' + str(n) + '_error)**2)' + ' + '
    expr1 = ' '.join(expr1.split(' ')[:-2]) + ')'
    #print(expr)
    #print(expr1)
    #creates the solvable expressions for sympy using numpy   
    variable_dict = {}
    errVariable_dict = {}
    func = parse_expr(expr)
    func1 = parse_expr(expr1)
    for j in range(num):
        for i in variable:
            #print('--',i)
            variable_dict[i] = dataSet._set[i.split('_')[0]]._valueList[j]
        for i in errVariable:
            if '_error' not in i:
                errVariable_dict[i] = dataSet._set[i.split('_')[0]]._valueList[j]
            else: 
                errVariable_dict[i] = dataSet._set[i.split('_')[0]]._errorList[j]
        #print(func.evalf(subs=variable_dict))
        #print(func1)
        #print(func1.evalf(subs=errVariable_dict))
        newDList._valueList[j] = func.evalf(subs=variable_dict)
        newDList._errorList[j] = func1.evalf(subs=errVariable_dict)
    #print(variable_dict)
    #print(errVariable_dict)
    #print(newDList._list)
    #print(newDList._valueList)
    dataSet._set[newDList._name] = newDList
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
    xname = info[2].split()[0] + ' (' + dataSet._set[info[2].split()[1]]._unit + ')'
    #print(xname)
    x = dataSet._set[info[2].split()[1]]._valueList
            #print(x)
    yname = info[3].split()[0] + ' (' + dataSet._set[info[3].split()[2]]._unit + ')'
    ylabel = info[3].split()[1]
    #print(yname)
    y = dataSet._set[info[3].split()[2]]._valueList
            #print(y)
    #print('y ',y)
    #print('x ', x)
    #title1 = ' '.join(info[3:])
    #title2 = ''.join(info[3:])
    plt.plot(x,y,label=ylabel)
    plt.title(title)
    plt.xlabel(xname)
    plt.ylabel(yname)
    #if len(info) > 3: 
    for i in range(len(info[4:])):
        #print(3+i)
        if dataSet._set[info[4+i].split()[1]]._unit == dataSet._set[info[3].split()[2]]._unit:
            ylabel1 = info[4+i].split()[0]
            y1 = dataSet._set[info[4+i].split()[1]]._valueList
            plt.plot(x,y1,label=ylabel1)
    plt.grid()
    plt.legend()
    plt.savefig(title1, dpi=1000)
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
