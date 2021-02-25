import random
import cartes as c
jeu1 = c.jeu_de_carte()
jeu2 = c.jeu_de_carte()

random.shuffle(jeu1)
random.shuffle(jeu2)

gagnat = ""
score1 = 0
score2 = 0

for i in range(len(jeu1)):
    if(jeu1[i][1] == jeu2[i][1]):
        gagnant = "Personne"
    elif(jeu1[i][1] > jeu2[i][1]):
        score1 += 1
        gagnant = "Joueur 1"
    else:
        score2 += 1
        gagnant = "Joueur 2"
    
    print("Jeu de carte 1: {}".format(c.str_carte(jeu1[i])))
    print("Jeu de carte 2: {}".format(c.str_carte(jeu2[i])))
    print("Gagnant: {}\n\n".format(gagnant))

print("Les Points:")
print("Joueur 1: {}".format(score1))
print("Joueur 2: {}".format(score2))

if(score1 == score2):
    print("EGALITE!")
elif(score1 > score2):
    print("GAGNANT: Joueur1")
else:
    print("GAGNANT: Joueur2")
