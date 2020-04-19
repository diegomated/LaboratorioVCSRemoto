import numpy as np
def generador(min, max):
    arreglo = np.random.randint(min, max, size=48).reshape(4,12)
    return arreglo 

def imprimir(a):
    print(" ---[Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic]")
    print("Buc",a[0][:])
    print("Flo",a[1][:])
    print("Gir",a[2][:])
    print("Pie",a[3][:])

def calcular(a,b):
    r=np.ones(48, dtype=int).reshape(4,12)
    for i in range(0,4,1):
        for e in range(0,12,1):
            r[i][e]=a[i][e]-b[i][e]
    return r

def mejorciudad(b):
    acu2=0
    ciudad=0
    for i in range(0,4,1):
        acu1=0
        acu1=np.sum(b[i])
        if(acu1>acu2):
            acu2=acu1
            ciudad=i
    print("\nMejor ciudad: ", ciudad, " con ", acu2, "ganancias")

def peorciudad(b):
    acu=0
    acu2=0
    ciudad2=0
    for i in range(0,4,1):
        acu=0
        acu=np.sum(b[i])
        if(i==0):
            acu2=acu
        if(acu<acu2):
            acu2=acu
            ciudad2=i
    print("Peor ciudad: ", ciudad2, " con ", acu2, "ganancias\n")

def mejormes(b):
    for i in range(0,4,1):
        for a in range(0,11,1):
            if(a==0):
                acu=b[i][a]
            if(acu<b[i][a+1]):
                acu=b[i][a+1]
                mes=a
        print("Mejor mes ciudad ",i+1,": ",mes+2," con ",acu," ganancias")

def imprimir_personalizado(a,b,c):
    print("\nmes ",b," al mes ",c)
    for i in range(0,4,1):
        print("ciudad ",i+1,": ",a[i][b-1:c-1])

ingresos = generador(100,180)
egresos = generador(60,130)
ganancias = calcular(ingresos,egresos)

print("Ingresos")
imprimir(ingresos)
print("Egresos")
imprimir(egresos)
mejorciudad(ganancias)
peorciudad(ganancias)
mejormes(ganancias)
imprimir_personalizado(ingresos,3,6)