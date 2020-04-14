import numpy as np 
kellogs=np.array([27834,23789,30189,30967,32501,32701,31665,17155,4614,834])
p1=(kellogs[0]+kellogs[1])/2
p2=(kellogs[9]+kellogs[8])/2

print("Diferencia de los 2 primeros años a los 2 ultimos años: ", p1-p2)

mayor=0
menor=0
for i in range (0,10,1):
    if i==0 :
        mayor=kellogs[0]
    elif kellogs[i]>mayor:
        mayor=kellogs[i]

    if i==0 :
        menor=kellogs[0]
    elif kellogs[i]<menor:
        menor=kellogs[i]

print("Diferencia de la mayor y menor utilidad: ", mayor-menor)