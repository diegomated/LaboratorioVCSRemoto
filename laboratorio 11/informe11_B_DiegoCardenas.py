import numpy as np

def ordenarM(c,a):
    for e in range(0,3,1):
        mayor=0
        for i in range(0,6,1):
            for i in range(0,5,1):
                if c[a][e][i]>c[a][e][i+1]:
                    mayor=c[a][e][i]
                    c[a][e][i]=c[a][e][i+1]
                    c[a][e][i+1]=mayor

def ordenarG(c,a):
    for e in range(0,3,1):
        mayor=0
        for i in range(0,6,1):
            for i in range(5,0,-1):
                if c[a][e][i]>c[a][e][i-1]:
                    mayor=c[a][e][i]
                    c[a][e][i]=c[a][e][i-1]
                    c[a][e][i-1]=mayor

clases=np.random.randint(10,19, size=144).reshape(8,3,6)
ordenarG(clases,0); ordenarG(clases,4); ordenarG(clases,6); ordenarG(clases,7)
ordenarM(clases,1); ordenarM(clases,2); ordenarM(clases,3); ordenarM(clases,5)
clase=np.random.randint(8, size=1)
personaje=np.random.randint(3, size=1)
categoria=clases[clase[0]][personaje[0]][:]

nametag=input("nametag: ")
if clase==0:
    cat="Barbaro"
elif clase==1:
    cat="Bardo"
elif clase==2:
    cat="Clerigo"
elif clase==3:
    cat="Druida"
elif clase==4:
    cat="Guerrero"
elif clase==5:
    cat="Mago"
elif clase==6:
    cat="Paladin"
elif clase==7:
    cat="Picaro"
print("\nUsuario: ",nametag)
print("Categoria: ",cat)
print("FUE\tDES\tCON\tINT\tSAB\tCAR")
print(categoria[0],"\t",categoria[1],"\t",categoria[2],"\t",categoria[3],"\t",categoria[4],"\t",categoria[5])

#           0        1          2       3       4          5        6          7
#       Bárbaros, Bardos, Clérigos, Druidas, Guerreros, Magos, Paladines y Pícaro

#       Bárbaro, Guerrero, Paladín y Pícaro         Fuerza, Destreza, Constitución
#       Bardo, Clérigo, Druida, Mago                Inteligencia, Sabiduría y Carisma