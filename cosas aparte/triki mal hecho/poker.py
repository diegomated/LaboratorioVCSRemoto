import random
listaP=[[[" "],[" "],[" "]],
        [[" "],[" "],[" "]],
        [[" "],[" "],[" "]]]

def trazado(lista):
    for i in range(0,len(lista)):
        print("",lista[i][0][0],"|",lista[i][1][0],"|",lista[i][2][0])
        if i<len(lista)-1:
            print("-----------")

def marcar(lista):
    bol=False
    while bol==False:
        fila=int(input("Fila: "))
        columna=int(input("Columna: "))
        for i in range(0,len(lista)):
            for a in range(0,len(lista[i])):
                if (i==fila-1 and a==columna-1):
                    if (lista[i][a][0]==" "):
                        lista[i][a][0]="X"
                        bol=True
        if bol==False:
            print("Esa casilla ya esta marcada")

def marcarbot(lista):
    bol=False
    while bol==False:
        fila=random.randint(0,2)
        columna=random.randint(0,2)
        for i in range(0,len(lista)):
            for a in range(0,len(lista[i])):
                if (i==fila-1 and a==columna-1):
                    if (lista[i][a][0]==" "):
                        lista[i][a][0]="O"
                        bol=True

def ganador(lista):
    if(lista[0][0][0]==lista[0][1][0] and lista[0][1][0]==lista[0][2][0] and lista[0][0][0]!=" " and lista[0][1][0]!=" " and lista[0][2][0]!=" "):
        print("ganador ",lista[0][0][0])
        return True
    elif(lista[1][0][0]==lista[1][1][0] and lista[1][1][0]==lista[1][2][0] and lista[1][0][0]!=" " and lista[1][1][0]!=" " and lista[1][2][0]!=" "):
        print("ganador ",lista[0][0][0])
        return True
    elif(lista[2][0][0]==lista[2][1][0] and lista[2][1][0]==lista[2][2][0] and lista[2][0][0]!=" " and lista[2][1][0]!=" " and lista[2][2][0]!=" "):
        print("ganador ",lista[0][0][0])
        return True
    elif(lista[0][0][0]==lista[1][0][0] and lista[1][0][0]==lista[2][0][0] and lista[0][0][0]!=" " and lista[1][0][0]!=" " and lista[2][0][0]!=" "):
        print("ganador ",lista[0][0][0])
        return True
    elif(lista[0][1][0]==lista[1][1][0] and lista[1][1][0]==lista[2][1][0] and lista[0][1][0]!=" " and lista[1][1][0]!=" " and lista[2][1][0]!=" "):
        print("ganador ",lista[0][0][0])
        return True
    elif(lista[0][2][0]==lista[1][2][0] and lista[1][2][0]==lista[2][2][0] and lista[0][2][0]!=" " and lista[1][2][0]!=" " and lista[2][2][0]!=" "):
        print("ganador ",lista[0][0][0])
        return True
    elif(lista[0][0][0]==lista[1][1][0] and lista[1][1][0]==lista[2][2][0] and lista[0][0][0]!=" " and lista[1][1][0]!=" " and lista[2][2][0]!=" "):
        print("ganador ",lista[0][0][0])
        return True
    elif(lista[2][0][0]==lista[1][1][0] and lista[0][1][0]==lista[0][2][0] and lista[2][0][0]!=" " and lista[1][1][0]!=" " and lista[0][2][0]!=" "):
        print("ganador ",lista[0][0][0])
        return True
    else:
        return False


bol=ganador(listaP)
while bol==False :
    marcar(listaP)
    bol=ganador(listaP)
    marcarbot(listaP)
    trazado(listaP)
    bol=ganador(listaP)


