import random
COULEUR = ('Pique', 'Coeur', 'Carreau', 'Trefle')
VALEUR = {2: 'Deux', 2: 'Deux', 3: 'Trois', 4: 'Quatre', 5: 'Cinq', 6: 'Six',
7: 'Sept', 8: 'Huit', 9: 'Neuf', 10: 'Dix',
11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As'}

def str_carte(carte):
    if (carte[0] not in COULEUR):
        return print("Invalide Couleur!")
    if (carte[1] < 2 or carte[1] > 14):
        return print("Invalide Valeur!")
    return "{} de {}".format(VALEUR[carte[1]], carte[0])

def jeu_de_carte():
    arr = []
    for i in range(len(COULEUR)):
        for j in VALEUR:
            arr.append((COULEUR[i], j))
    return arr
