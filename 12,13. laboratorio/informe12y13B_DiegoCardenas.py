import random
ponderado={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
simbolos=["♥","♦","♣","♠"]

def combinar (numero,simbolo):
    baraja={}
    for i in range(0,len(simbolo)):
        for a in numero:
            baraja.update({a+simbolo[i]:numero[a]})
    return baraja

def revolver (dict):
    num_clave=[[clave,dict[clave]] for clave in dict]
    random.shuffle(num_clave)
    nuevodict={num_clave[i][0]:num_clave[i][1] for i in range(0,len(num_clave))}
    return nuevodict

def repartir (dict,jug):
    a=not jug
    cartas=dict.copy()
    cartas=[[clave,dict[clave]] for clave in dict]
    if (a==True):
        carta_uno=cartas.pop(random.randint(0,len(cartas)-1))
        carta_dos=cartas.pop(random.randint(0,len(cartas)-1))
        nuevodict={cartas[i][0]:cartas[i][1] for i in range(0,len(cartas))}
        return nuevodict,carta_uno,carta_dos
    else :
        carta_uno=cartas.pop(random.randint(0,len(cartas)-1))
        nuevodict={cartas[i][0]:cartas[i][1] for i in range(0,len(cartas))}
        return nuevodict,carta_uno

def sumar_cartas (dict):
    suma=0;ac=True;ac1=0
    for i in range(0,len(dict)):
        if(dict[i][0][0]=='A'):
            suma=suma+11
        else:
            suma=suma+dict[i][1]
        
        if(suma>21):
            for a in range(ac1,i+1):
                if(ac==True and dict[a][0][0]=='A'):
                    suma=suma-10
                    ac1=i
                if(suma<21):
                    ac=False
    return suma

def mostrar (cartas):
    suma=(sumar_cartas(cartas))
    print("\nCartas: ")
    for i in range(0,len(cartas)):
        print("  ["+cartas[i][0]+"]")
    if (suma>11 and suma<21):
        print("->",suma,"<-"," Probabilidad de pasarse ",(100-(21-suma)*8),"%")
    else:
        print("->",suma,"<-"," Probabilidad de pasarse 0%")
    return suma

turno=True
ronda=0
contG=0
contP=0

while(turno==True):

    baraja=combinar(ponderado,simbolos)
    baraja=revolver(baraja)
    cartas_jugador=[]
    cartas_tallador=[]
    ronda+=1
    print("\n// ----- // RONDA ",ronda,"// ----- //")
    turn='YES'

    while(turn=='YES'):
        b=not cartas_jugador
        if (b==True):
            baraja,carta_uno,carta_dos=repartir(baraja,cartas_jugador)
            cartas_jugador.append(carta_uno);cartas_jugador.append(carta_dos)
        else:
            baraja,carta_uno=repartir(baraja,cartas_jugador)
            cartas_jugador.append(carta_uno)

        suma=mostrar(cartas_jugador)

        if (suma==21):
            print("Winner winner chicken dinner")
            break
        elif (suma>21):
            print("Te pasaste de 21, F")
            break
        while(True):
            turn=input("Desea sacar otra carta?(YES)(NO): ")
            if (turn=="YES" or turn=="NO"):
                break

    print("\n------- Turno del repartidor --------\n")

    razon=True
    while(razon!=False):
        b=not cartas_tallador
        if (b==True):
            baraja,carta_uno,carta_dos=repartir(baraja,cartas_tallador)
            cartas_tallador.append(carta_uno);cartas_tallador.append(carta_dos)
        else:
            baraja,carta_uno=repartir(baraja,cartas_jugador)
            cartas_tallador.append(carta_uno)
        suma2=mostrar(cartas_tallador)

        if (suma2==suma or suma2==21 or (suma2>suma and suma2<21 and suma!=21) or (suma2<suma and suma2>21 and suma!=21)):
            razon=False
            print("PERDISTE ESTA RONDA")
            contP+=1
        elif (suma2>21):
            razon=False
            print("GANASTE ESTA RONDA")
            contG+=1
    
    while(True):
        turno=input("\nDesea jugar otra ronda?(YES)(NO): ")
        if (turno=="YES" or turno=="NO"):
                break

    if (turno=='YES'):
        turno=True
    else:
        turno=False

print("\nRondas jugadas: ",ronda)
print("Ganadas: ",contG)
print("Perdidas:",contP)