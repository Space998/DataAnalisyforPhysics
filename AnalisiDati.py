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
print("Prova: ", 2*d)

print("Somma: ", d + 10)
print("Somma: ", 10 + d)
#print(2/4)
print("Somma: ", d - 10)
print("Somma: ", 10 - d)

print("Somma: ", d / 10)
print("Somma: ", 10 / d)

print("Somma: ", d ** 2)
print("Somma: ", 2 ** d)

print(-d)
print(~2)

e += 1

print("Test: ", (d + 8) * 5)
print("Test: ", d + 8 * 5)
print("e: ", e)

f = Data(10, 4)
print(f)
print(d+f)
