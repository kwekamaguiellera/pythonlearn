print("vous devez repondre aux questions suivantes en vous servant de lindicatif de la reponse que vous aurez choisis")


questions= ("quelle est la capitale du cameroun:",
           "qui est le president du cameroun:",
           "en quelle annee le cameroun obtient son independance:",
           "en quelle annee le comeroun passe de provinces aux regions:")

options= (("A. buea ","B. douala","C. yaounde"),
          ("A. paul biya","B. hamadou ahidjo","C. watara"),
          ("A. 1945","B. 1961","C. 1960"),
          ("A. 1999","B. 2008","C. 2015"))

answer= ("C" "A" "C" "B")
question_num=0
score=0
guesses=[]

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter (A,B,C):").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score+=1
        print("CORRECT")
        question_num+=1
    else:
        print("cest faux")
        question_num+=1

print("votre score est de:", score)    