u0=0
un=1
def u(i):
        
        
a=int(input("entrer un nombre: ")) 
for i in range(1,int(a+1)):
               ua=i
               ub=i-1
               ua=un+ub
               print(ua)
               un=ua
