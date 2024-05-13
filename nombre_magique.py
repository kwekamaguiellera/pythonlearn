import random

tour=str("oui")

nbr = 0

def demander_nbr(min,max):
        nb=int(input("quel est le nombre magique entre " + str(min) + " et " +str(max) + ": "))
        return nb
def minmax():
    min=int(input("entrerz un nombre min : "))
    max=int(input("entrerz un nombre max : "))
    return min, max


while tour==str("oui"):
    valeur=minmax()
    #print(valeur[0])
    if valeur[0]>valeur[1]:
        print("vous devez entrer un nim plus petit que max")
        #valeur=minmax()
        continue
    else:
        nombre_magique=random.randint(valeur[0], valeur[1])
        #print(nombre_magique)
        
        chances=int(input("en combien de chances pouvez vous trouver le nombre magique? "))
        chances=chances+1

        for i in range(0,chances):
            if nombre_magique==0:
                print("votre nombre magique est exlus")
            if nbr is not nombre_magique:
                chances=chances-1
        
        
                if chances==0:
                    print("vous avez perdu le nombre magique etait: "+ str(nombre_magique))
                    tour = input("voulez vous une second tour oui ou non? ")
                else:  
                    print("il vous reste "+ str(chances) + "  vies")  
                    nbr=demander_nbr(min,max)
                    if nbr > nombre_magique:
                        print("le nombre magique est plus petit que " + str(nbr))
        
                    elif  nbr < nombre_magique:
                        print("le nombre magique est plus grand que " + str(nbr))
        
                    elif nbr == nombre_magique:
                        print("BRAVO VOUS EVEZ TROUVER LE NOMBRE MAGIQUE")
                        tour= str("non")
if tour == str("non"):
    print("bye bye")                    
        
    
