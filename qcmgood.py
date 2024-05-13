score=0
def qcm(question,r1,r2,r3, bonne_reponse):
    global score
    print(question)
    print(r1)
    print(r2)
    print(r3)
    reponse=input("quelle est votre reponse entre A B C:")
    if reponse == bonne_reponse:
        print("bonne reponse")
        score+=1
    else:
        print("la bonne reponse etait:", bonne_reponse)  

 

qcm("quelle est la capitale du cameroun:","A. buea ","B. douala","C. yaounde","c")
qcm("qui est le president du cameroun:","A. paul biya","B. hamadou ahidjo","C. watara","a")
qcm("en quelle annee le cameroun obtient son independance:","A. 1945","B. 1961","C. 1960","c")
qcm("en quelle annee le comeroun passe de provinces aux regions:","A. 1999","B. 2008","C. 2015","b")
print("votre score est de:", score)