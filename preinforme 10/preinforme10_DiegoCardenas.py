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

acu=0
kellogs2=np.array([27834,23789,30189,30967,32501,32701,31665,17155,4614,834])
for i in range (0,10,1):
    for i in range (0,9,1):
        if kellogs2[i]>kellogs2[i+1]:
            acu=kellogs2[i]
            kellogs2[i]=kellogs2[i+1]
            kellogs2[i+1]=acu

m1=kellogs2.size/2
m2=(kellogs2.size/2)+1
med=(kellogs2[int(m1)-1]+kellogs2[int(m2)-1])/2

print("la mediana es: ", med)

acuD=0
for i in range(0,10,1):
    acuD=acuD+kellogs[i]

prom=0
anio=2009
for i in range(0,10,1):
    prom=(100*kellogs[i])/acuD
    print("Porcentaje año", anio, ": ", round(prom,2), "%")
    anio+=1

print("El deficit del año 2017 respecto al año pasado es de: ", kellogs[9]-kellogs[8])

anio=2009
for i in range (1,10,1):
    p_defi=((kellogs[i]-kellogs[i-1])/kellogs[i-1])*100
    print("Porc. Def año ", anio,": ", round(p_defi,2), "%")
    anio+=1