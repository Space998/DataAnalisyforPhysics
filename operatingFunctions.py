from dataList import DList
from dataSet import DSet

dataSet_dict = {}

def operation(file):
    for i in range(len(file)):
        line = file[i].split()
        if line[0] in functionDict:
            functionDict[line[0]](line[1:])

def newData(data):
    if data[0] not in dataSet_dict:
        dataSet_dict[data[0]] = DSet(data[0])
    dataSet = dataSet_dict[data[0]]
    for i in range(1,len(data[1:]),2):
        i = DList(data[i], data[i+1])
        dataSet._set.append(i)  
 
def printData(set):
    for i in range(len(set)):
        dataSet = dataSet_dict[set[i]]
        for i in dataSet._set:
            print(i._name, ' ', i._unit, '\t\u03C3Err(', i._name, ')', end = '\t')
        print()
        for i in dataSet._set:
            for j in range(len(dataSet._set[0]._list)):
                print(dataSet._set[i]._list[j],_value, '\t', dataSet._set[i]._list[j],_error, end = '\t')
        print()

def function(expr):
    expr = " ".join(expr)
    print(expr)

functionDict = {'FUNCTION': function, 'NEWDATA': newData, 'PRINTDATA': printData}
#add ability to create custom dataSets