"""Je viens davoir une idee pas mal a mettre on devrais rajouter un parametre de plus dans toutes nos listes qui nous permettent d'identifier le joueur 0 pour le dealer 1 pour joueur 1 etc."""
stand_value=False
play_check=True
playerbank=[100,100]
moneybet=[0,0]
joueurs=0
import random
"""Toutes les valeurs de cartes de cartes sont des str on genere donc str"""

Decks = {
  "dealer": [[[]]], 
  "player1": [[[]]], 
  "player2": [[[]]], 
  "player3": [[[]]], 
  "player4": [[[]]]
}

Banks = {
  "dealer": 100, 
  "player1": 100, 
  "player2": 100, 
  "player3": 100, 
  "player4": 100
}

Bets = {
  "dealer": 0, 
  "player1": 0, 
  "player2": 0, 
  "player3": 0, 
  "player4": 0
}

def generer_jeu():
    jeu = []
    couleurs = ["COEUR", "CARREAU", "PIQUE", "TREFLE"]
    valeurs = [str(i) for i in range(1, 11)] + ['V', 'D', 'R']
    for col in couleurs:
        for val in valeurs:
            jeu.append((val, col))
    return jeu

def melanger(L):   
    for i in range(1, len(L)):
        j = random.randint(0, i)
        if j < i:
            L[i], L[j] = L[j], L[i]

def burn_check(L):
    counter=0
    ace_counter=0
    for i in range(len(L)):
        if L[i][0]=='V':
            counter=counter+10
        elif L[i][0]=='D':
            counter=counter+10
        elif L[i][0]=='R':
            counter=counter+10
        elif L[i][0]=='1':
            counter=counter+11

        else:
            counter=counter+L[i][0]
    if counter>21 and ace_counter>0:
        while counter>21 and ace_counter>0:
            counter=counter-10
            ace_counter=ace_counter-1
        return counter
    return counter




def split_a_pair(player):    """A AMELIORER LIRE PLUS: """
    if len(Decks[player])==1 and len(Decks[player][0])==2 and Decks[player][0][0][0]==Decks[player][0][1][0] :
        temp=Decks.pop(player[0][1])
        Decks[player].append(temp)
#prend en entree la liste du joueur seulement apres la PREMIERE distribution des cartes si les deux cartes sont de memes valeurs le joueur peux "split" et avoir deux decks (implemanter compteur de manches dans le jeu et la fonction)





def stand():"""A voir: Ne pas prendre de cartes et passer au prochain joueur (je pense que l'on devrait faire une liste des joueurs ou un truc comme ca peut etre?)"""
    stand_value=True
"""Avec l'idee de mettre un truc du genre dans la boucle:
if stand_value==True:
    stand_value=False
    continue
"""




def hit():"""def hit tire une carte voir def deal card qui fait exactement ca"""
    pass




def double_down(player):"""peut seulement etre utilise pendant la premiere manche apres que les deux premierses cartes soit donnes. Double la mise"""
    if len(L)==2 and Banks[player]-2*Bets[player]>0:
        Bets[player]=2*Bets[player]
        

while play_check=True:
    while joueurs<=0:
        joueurs=int(input("Combien de joueurs veulent joueur?"))
    jeu=(joueurs/4+1)*generer_jeu()
    melanger(jeu)
    