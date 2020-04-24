import math

def menor_mayorP(a):
    a1=a.copy()
    a1.sort()
    menor=a1[0]
    mayor=a1[-1]
    return mayor, menor

def media(a):
    promedio=sum(a)/len(a)
    return promedio

def mediana(a):
    a1=a.copy()
    a1.sort()
    pm=int(len(a1)/2)
    median=(a1[pm]+a1[pm+1])/2
    return median

def nuevalista(a,b):
    lista1=[]
    lista2=[]
    p=0
    for i in range (0,52):
        if a[i]<b:
            lista1.append(i+1)
        elif a[i]>b and a[i-1]<b:
            lista2.append(lista1[p:i])
            p=i
        if a[i]>b:
            lista1.append(i+1)
        elif a[i]<b and a[i-1]>b:
            lista2.append(lista1[p:i])
            p=i
        if i==51:
            lista2.append(lista1[p:i+1])
    return lista2

def temperatura(a):
    temp=[]
    for i in range(0,len(a)):
        temp.append(round(((a[i]*(1/101.3))*510)/(17.16*0.082),2))
    return temp

def desviacion(temp):
    prom=sum(temp)/len(temp)
    desv=0
    for i in range(len(temp)):
        desv=desv+(temp[i]-prom)**2/len(temp)
    desv=round(math.sqrt(desv),2)
    return desv

def nuevalista2(a,b):
    lista1=[]
    lista2=[]
    p=0
    for i in range (0,52):
        if a[i]<b:
            lista1.append(a[i])
        elif a[i]>b and a[i-1]<b:
            lista2.append(lista1[p:i])
            p=i
        if a[i]>b:
            lista1.append(a[i])
        elif a[i]<b and a[i-1]>b:
            lista2.append(lista1[p:i])
            p=i
        if i==51:
            lista2.append(lista1[p:i+1])
    return lista2

presiones=[110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85]
mayor, menor=menor_mayorP(presiones)

print("Diferencia de la menor y mayor presion: ",round(mayor-menor,2))
print("Promedio: ", round(media(presiones),2))
print("Mediana: ", round(mediana(presiones),2),"\n")
print("Semanas: ")
print(nuevalista(presiones,round(media(presiones),2)),"\n")
print("Desviacion estandar temperatura: ", desviacion(temperatura(presiones)),"\n")
temp_nueva=nuevalista2(temperatura(presiones),round(media(temperatura(presiones)),2))
print("Desviacion de los rangos de temperaturas: ")
for i in range(len(temp_nueva)):
    print("Desviacion ",i+1,": ",desviacion(temp_nueva[i]))
