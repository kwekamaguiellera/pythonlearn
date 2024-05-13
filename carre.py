
taille_depart=int(input("entrez une taille de depart:"))
nombre_de_marches=int(input("eentrez le nombre de marches que vous voulez:"))

import turtle
t=turtle.Turtle()

def carre (taille_depart, nombre_de_marches):
    for i in range (0,nombre_de_marches):
        t.forward(taille_depart)
        t.left(90)
        t.forward(taille_depart)
        t.left(90)
        t.forward(taille_depart)
        t.left(90)
        t.forward(taille_depart)
        t.left(90)
        taille_depart=taille_depart+10
    return t,nombre_de_marches
carre(taille_depart,nombre_de_marches)
turtle.done()