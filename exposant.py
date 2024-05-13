def expo(nombre,exposant):
    s=1
    for i in range (exposant):
        s=s*nombre
    print("la solution de", nombre, "exposant", exposant, "est: ", s)
nbr=int(input("entrer un nombre:"))    
exp=int(input("entrer lexposant en question: "))
expo(nbr,exp)