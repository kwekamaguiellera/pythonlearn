def multiplication(nombre):
    for i in range(12):
        s=nombre*i
        print(i,"*",nombre,"=",s)

def addition(nombre):
    for i in range(12):
        s=nombre+i
        print(i,"+",nombre,"=",s)


nbr=int(input("vous voulez la tablede multiplication de combien: "))
nb=int(input("vous voulez la table daddition de combien: "))
multiplication(nbr)     
print("")
addition(nb)   
