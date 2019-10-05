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
print("e: ",e)
print(e + 13)
print(e +100)

print(d.sqrt())
print(d.sqrt(3))
print(d)
print(d.sin())
print(d.cos())
print(d.exp())

print(d+12)
print((d+12).sin())

a = (12+d).sin()
print(a)
print(a*2)
print(2*a)

print(d)
print(d + 36)
print((d+36).sin())
print((a*2).sin())

