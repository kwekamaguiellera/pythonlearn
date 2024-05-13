t=int(input("entrez la taille de vos escaliers:"))
marches=int (input("entrerz le nombre de marches  de votre escalier:"))

import turtle
taille = turtle.Turtle()
papier = turtle.Screen()

def escalier(t, marches):
  for i in range(0,marches):
    taille.forward(t)
    taille.left(90)
    taille.forward(t)
    taille.right(90)
    t=t-10
  return taille,marches

    
solution=escalier(t,marches)

turtle.done()