a= int (input ("entrer un nombre:"))
st=0

for i in range(1,int((a/2)+1)) :
    s=a%i
    if s == 0:
        st=st+1
    
if st == 1:
     print(str(a) + " est premier")
else:
   print(str(a) + " nest pas premier") 
