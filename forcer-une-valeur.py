n=int(input("combien de personnes voudrez vous enregistrere:"))
taille=0
def demander_age():
 ageint = 0.5
 while ageint == 0:
   age1= input("entreer un age valide:")
   try:
     ageint =int(age1)
   except:
     print("vous devez entrer un age valide")  
 return ageint

def demander_taille():
  taille=input("quelle est votre taille:")
  return taille

def demander_info(age, nom, taille):
   if age == 17 :
     print("vous etes presque majeur")
   elif 1<= age <5:
      print("vous etes un bebe")
      print("vous vous appeler " +str(nom) + " et vous evez " + str(age) + " ans" +" et vous faites " +taille+ "M" ) 
   elif 60<age or age>=5:
      print("vous etes totalement prise en charge par votre entourage")   
      print("vous vous appeler " +str(nom) + " et vous evez " + str(age) + " ans" +" et vous faites " +taille+ "M" )  
   elif age < 18 :
       print("vous etes mineur")
       print("vous vous appeler " +str(nom) + " et vous evez " + str(age) + " ans" )
   elif age == 18:
      print("vous venez a peine detre majeur")    
   else:
     print("vous etes majeur")  
     print("vous vous appeler " +str(nom) + " et vous evez " + str(age) + " ans" )
    

def demander_nom():
 nomde =""
 while nomde == "":
   nomde = input("entrer votre nom:")
   #try:
     #if nomde  is not None:
      # print("votre nom est: "+ str(nomde) +" et vous avez " + str(age) +" ans" ) 
   #except:
    # print("ERROR:vous etes obliger dentrer un nom pour ontinuer") 
 return nomde 



for i in range(0,n):
  #personne="personne " + str(i+1)
  age = demander_age()
  nom = demander_nom()
  taille=demander_taille()
  demander_info(age,nom, taille)