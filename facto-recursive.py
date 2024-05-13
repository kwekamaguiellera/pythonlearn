def facto(nombre):
    for i in range (nombre, 0, -1):
        if i>1:
             solution=i*facto(i-1)
        elif i==1:
            solution=1    
        return solution    
nbr=int(input("vous voulez le factoriel de quel nombre:" ))
t=facto(nbr)    
print ("le factoriel de", nbr, "est: ", t)