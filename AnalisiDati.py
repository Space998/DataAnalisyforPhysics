from data import Data
import sys

if len(sys.argv) != 2:
    print ("Errore inserire nome del file")
    exit()

print ("Nome del file:",sys.argv[1])

#test data.py class
d = Data(12, 5, "A", "m")
print (d)
e = Data(11, 4, "A", "m")
print(e)
print("Somma: ", d + e)
print("Sottrazione: ", d - e)
print("Moltiplicazione: ", d * e)
print("Divisione: ", d/e)
#print(2/4)

f = Data(10, 4, "B", "m")
print(f)
print(d+f)
