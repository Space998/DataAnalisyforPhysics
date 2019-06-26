from dataErr import Data
import sys
import genericFunctions 

print(genericFunctions.checkFile())

instruction = genericFunctions.checkFile()
formatInstruction = genericFunctions.formatFile(instruction)

print(formatInstruction)

#if len(sys.argv) != 2:
#    print ("Errore inserire nome del file")
#    exit()

#print ("Nome del file:",sys.argv[1])

#test data.py class
d = Data(12, 5)
print (d)
e = Data(11, 4)
print(e)
print("Somma: ", d + e)
print("Sottrazione: ", d - e)
print("Moltiplicazione: ", d * e)
print("Divisione: ", d/e)
print("Prova: ", d*2)
#print(2/4)

f = Data(10, 4)
print(f)
print(d+f)
