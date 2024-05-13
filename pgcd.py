a =int (input ("entrer un premier nombre:"))
b = int (input("entrer un deuxieme nombre:"))
r=0
while b > 0:
 r=a%b
 a=b
 b=r

print("la solution est "+ str(a))
