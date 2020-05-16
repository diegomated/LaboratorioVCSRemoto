import random
cartas = ["Payne" , "Hendrix" , "Stone" , "Coffey" , "Whitaker" , "Pope" ,
        "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" ,
        "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , 
        "Stonehammer" , "Smith" , "Patrick" , "Crane" , "Cargane" , "Powers" ,
        "Wade" , "Joseph" , "Savage" , "Houston" , "Merritt" , "Nuke" , 
        "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake" , "Schneider" , 
        "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" , 
        "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , 
        "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" , 
        "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , 
        "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" , 
        "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , 
        "Crimson" , "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" , 
        "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , 
        "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , 
        "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , 
        "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" ,"Mann"]

premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]

def imprimir(lista):
    print("cartas: ",len(lista))
    print(lista,"\n")

def generador(lista,cantidad):
    lista1=[]
    nuevalista=[]
    i=0
    while i<cantidad:
        a=random.randint(0,len(lista)-1)
        if i==0:
            lista1.append(a)
            i+=1
        else:
            ac=True
            for carta in lista1:
                if a==carta:
                    ac=False
            if(ac==True):
                lista1.append(a)
                i+=1
    for i in lista1:
        nuevalista.append(lista[i])
    return nuevalista

def combinador(lista1,lista2):
    lista3=[]
    for i in range(0,len(lista1)):
        lista3.append(lista1[i])
    for i in range(0,len(lista2)):
        lista3.append(lista2[i])
    random.shuffle(lista3,random.random)
    return lista3

def loteria(lista,lista2):
    a=False
    b=0
    cart=0;carta=0
    loteria=random.randint(1,10)
    for i in range(0,len(lista)):
        for e in range(0,len(lista)):
            if lista[i]==lista[e] and i!=e:
                a=True
    for i in range(0,len(lista)):
        for e in range(0,len(lista2)):
            if lista[i]==lista2[e]:
                b=b+1
                cart=e
    print(a,b,loteria)
    if (a==True and b<2 and loteria==1):
        while lista2[cart]!=carta:
            carta=random.randint(0,4)
            carta=lista2[carta]
            if lista2[cart]!=carta:
                break
        lista.append(carta)
        print(lista)
    return lista

def ordenar(lista):
    for i in range(0,len(lista)):
        for a in range(0,len(lista)-1):
            if (lista[a]>lista[a+1]):
                acu=lista[a]
                lista[a]=lista[a+1]
                lista[a+1]=acu
    return lista

def repetidas2(lista):
    lista1=[]
    lista2=[[],[]]
    lista=ordenar(lista)
    for i in range(0,len(lista)-1):
        ac=True
        if (lista[i]==lista[i+1]):
            ac=False
        if (ac==True):
            lista1.append(lista[i])
    lista1.append(lista[-1])
    for i in range(0,len(lista1)):
        ac=0
        for a in range(0,len(lista)):
            if (lista1[i]==lista[a]):
                ac+=1
        lista2[0].append(lista1[i])
        lista2[1].append(ac)
    return(lista2)

def cartasP(lista,lista2):
    lista3=[]
    print("Cartas Premium: ")
    for i in lista:
        for a in lista2:
            if i==a:
                lista3.append(i)
    for i in range(0,len(lista3)):
        print(lista3[i])
    print("")
    return lista3

def letras_alfabeto(lista):
    letras=[["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],[]]
    print("\n","letras alfabeto ingles: ")
    for i in range(0,len(letras[0])):
        acu=0
        letras[1].append(acu)
        for a in range(0,len(lista)):
            if (letras[0][i]==lista[a][0]):
                acu+=1
                letras[1][i]=acu
    for i in range(0,len(letras[0])):
        print(letras[0][i],"= ",letras[1][i])

def carta_nombreLC(lista):
    lista1=[[i,len(lista[i])] for i in range(0,len(lista))]
    for i in range(0,len(lista1)):
        for a in range(0,len(lista1)-1):
            if (lista1[a][1]>lista1[a+1][1]):
                acu=lista1[a]
                lista1[a]=lista1[a+1]
                lista1[a+1]=acu
    print("\n","Menor cantidad de letras: ",lista[lista1[0][0]])
    print(" Mayor cantidad de letras: ",lista[lista1[-1][0]],"\n")

def terminacion_letra(lista,cartasp):
    lista2=[]
    b=not cartasp
    if(b==True):
        print("no tiene cartas premium \n")
    else:
        lista1=[cartasp[i][0] for i in range(0,len(cartasp))]
        print(lista1)
        for i in range(0,len(lista1)):
            for a in range(0,len(lista)):
                if(lista1[i].lower()==lista[a][-1] or lista1[i]==lista[a][-1]):
                    lista2.append(lista[a])
        b=not lista2
        if(b==True):
            print("Ninguna letra termina por la primera de las premium \n")
        else:
            print(lista2,"\n")

def letras_consecutivas(lista):
    lista1=[]
    for i in range(0,len(lista)):
        for a in range(0,len(lista[i])-1):
            if (lista[i][a]==lista[i][a+1]):
                lista1.append(lista[i][a])
    lista2=repetidas2(lista1)
    for i in range(0,len(lista2[0])):
        print("la letra ",lista2[0][i]," se repite en pares ",lista2[1][i]," veces")

def letras_alfabeto2(lista):
    letras=[["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],[]]
    print("\n","letras de todas la carta, del alfabeto ingles: ")
    for i in range(0,len(letras[0])):
        acu=0
        letras[1].append(acu)
        for e in range(0,len(lista)):
            for a in range(0,len(lista[e])):
                if (letras[0][i]==lista[e][a] or letras[0][i].lower()==lista[e][a]):
                    acu+=1
                    letras[1][i]=acu
    for i in range(0,len(letras[0])):
        print(letras[0][i],"= ",letras[1][i])

imprimir(cartas)
imprimir(premium)

jugador=generador(cartas,10)

juego=combinador(cartas,premium)

sobre_uno=generador(juego,5)
sobre_dos=generador(juego,5)
sobre_tres=generador(juego,5)

print("Sobre 1: ",sobre_uno)
print("Sobre 2: ",sobre_dos)
print("Sobre 3: ",sobre_tres,"\n")

paquete=combinador(sobre_uno,combinador(sobre_dos,sobre_tres))
print("Paquete: ",paquete,"\n")
jugador=combinador(loteria(paquete,premium),jugador)
print("Cartas del jugador:",jugador, "\n")
cartasp=cartasP(jugador,premium)
cartasR=repetidas2(jugador)
print("Cartas: ")
for i in range(0,len(cartasR[0])):
        print("x",cartasR[1][i],cartasR[0][i])

letras_alfabeto(jugador)
carta_nombreLC(jugador)
terminacion_letra(jugador,cartasp)
letras_consecutivas(jugador)
letras_alfabeto2(jugador)