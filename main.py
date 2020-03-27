import math
a = int(input("numero a: "))
b = int(input("numero b: "))
c = int(input("numero c: "))

d=b**2-4*a*c

if(d>0):
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print("x1= ",x1)
    print("x2= ",x2)
elif(d==0):
    print("x1 es igual a x2")
    x1=-b/2*a
    print("x= ",x1)
else:
    print("no existe una solucion para esta ecuacion")

