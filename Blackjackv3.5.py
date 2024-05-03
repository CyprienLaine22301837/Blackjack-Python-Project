"""Je viens davoir une idee pas mal a mettre on devrais rajouter un parametre de plus dans toutes nos listes qui nous permettent d'identifier le joueur 0 pour le dealer 1 pour joueur 1 etc."""
stand_value=False
play_check=True
playerbank=[100,100]
moneybet=[0,0]
joueurs=0
nb_de_packets=0
over_check = False
import random
"""Toutes les valeurs de cartes de cartes sont des str on genere donc str"""
yesorno=""
Decks = {
  "dealer": {'nom': 'Mike', 'score':"0", 'cards': [[]], 'fini':False},
  "player1": {'nom': 'player1', 'score':"0", 'money':100, 'bet':0, 'Use':False, 'victories':0, 'fini':True, 'split':0, 'splitfini':True, 'cards': [[]]},  
  "player2": {'nom': 'player2', 'score':"0", 'money':100, 'bet':0, 'Use':False, 'victories':0, 'fini':True, 'split':0, 'splitfini':True, 'cards': [[]]}, 
  "player3": {'nom': 'player3', 'score':"0", 'money':100, 'bet':0, 'Use':False, 'victories':0, 'fini':True, 'split':0, 'splitfini':True, 'cards': [[]]}, 
  "player4": {'nom': 'player4', 'score':"0", 'money':100, 'bet':0, 'Use':False, 'victories':0, 'fini':True, 'split':0, 'splitfini':True, 'cards': [[]]}, 
  "player5": {'nom': 'player5', 'score':"0", 'money':100, 'bet':0, 'Use':False, 'victories':0, 'fini':True, 'split':0, 'splitfini':True, 'cards': [[]]}, 
  "player6": {'nom': 'player6', 'score':"0", 'money':100, 'bet':0, 'Use':False, 'victories':0, 'fini':True, 'split':0, 'splitfini':True, 'cards': [[]]}, 
  "player7": {'nom': 'player7', 'score':"0", 'money':100, 'bet':0, 'Use':False, 'victories':0, 'fini':True, 'split':0, 'splitfini':True, 'cards': [[]]}, 
}



def generer_jeu():
    jeu = []
    couleurs = ["COEUR", "CARREAU", "PIQUE", "TREFLE"]
    valeurs = [str(i) for i in range(1, 4)] + ['V', 'D', 'R']
    for col in couleurs:
        for val in valeurs:
            jeu.append((val, col))
    return jeu

def melanger(L):   
    for i in range(1, len(L)):
        j = random.randint(0, i)
        if j < i:
            L[i], L[j] = L[j], L[i]
    return L

def counter_check(L):
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
            counter=counter+int(L[i][0])
    if counter>21 and ace_counter>0:
        while counter>21 and ace_counter>0:
            counter=counter-10
            ace_counter=ace_counter-1
        return counter
    return counter



def fini_check(Decks, joueurs):
    for i in range(joueurs):
        if Decks["player"+str(i+1)]['fini'] == False:
            return False
        if Decks["player"+str(i+1)]['splitfini'] == False:
            return False
    return True


"""A AMELIORER LIRE PLUS: """
def split_a_pair(player, Decks, split_area):    
    if Decks[player]['cards'][split_area][0][0]==Decks[player]['cards'][split_area][1][0] and Decks[player]['split']<=3:
        temp=Decks[player]['cards'][split_area].pop(1)
        Decks[player]['cards'].append([temp])
#prend en entree la liste du joueur seulement apres la PREMIERE distribution des cartes si les deux cartes sont de memes valeurs le joueur peux "split" et avoir deux decks (implemanter compteur de manches dans le jeu et la fonction)




"""A voir: Ne pas prendre de cartes et passer au prochain joueur (je pense que l'on devrait faire une liste des joueurs ou un truc comme ca peut etre?)"""
def stand():
    stand_value=True
"""Avec l'idee de mettre un truc du genre dans la boucle:
if stand_value==True:
    stand_value=False
    continue
"""



"""def hit tire une carte voir def deal card qui fait exactement ca"""
def hit(L, jeu):
    temp=jeu.pop()
    L.append(temp)
    return L


"""peut seulement etre utilise pendant la premiere manche apres que les deux premierses cartes soit donnes. Double la mise"""
def double_down(player):
    if len(L)==2 and Banks[player]-2*Bets[player]>0:
        Bets[player]=2*Bets[player]
        

while play_check == True:
    
    while joueurs <= 0 or joueurs > 7:
        joueurs = input("Combien de joueurs veulent joueur? (tapez un nombre entre 1 et 7) ")
        joueurs = int(joueurs)
    
    for i in range(joueurs):
        Decks["player"+str(i+1)]['score'] = '0'
        Decks["player"+str(i+1)]['fini'] = False
        Decks["player"+str(i+1)]['splitfini'] = True
        if Decks["player"+str(i+1)]['Use']==True:
            yesorno = str(input("Le joueur"+Decks["player"+str(i+1)]['nom']+"a deja ete utilise voulez vous garder le compte precedent?(y/n)"))
            
            if yesorno == 'n':
                Decks["player"+str(i+1)]['nom'] = input("Choisissez un nom: ")
                Decks["player"+str(i+1)]['money'] = 100
                Decks["player"+str(i+1)]['bet'] = 0
                    
                if Decks["player"+str(i+1)]['money'] <= 24:
                    print("Votre argent est en dessous du minimum necessaire. Vous etes ejecte du casino. Vous sacrifiez vos victoires pour un nouveau depart.")
                    Decks["player"+str(i+1)]['money'] = 100
                    Decks["player"+str(i+1)]['bet'] = 0
                    Decks["player"+str(i+1)]['victories'] = 0
        
        else:
            Decks["player"+str(i+1)]['Use'] = True
            Decks["player"+str(i+1)]['nom'] = input("Choisissez un nom Nouveau Joueur: ")
            
        while Decks["player"+str(i+1)]['bet'] <= 24 or Decks["player"+str(i+1)]['bet'] > Decks["player"+str(i+1)]['money']:
                Decks["player"+str(i+1)]['bet'] = input("Combien vous voulez parier "+Decks["player"+str(i+1)]['nom'])
                Decks["player"+str(i+1)]['bet'] = int(Decks["player"+str(i+1)]['bet']) 
            
    nb_de_packets = 0

    while nb_de_packets < 3:
        print("Ce casino utilise un minimum de 3 Packets.")
        nb_de_packets = int(input("Combien de Packets voulez vous utiliser pour jouer?"))
    
    jeu = nb_de_packets*generer_jeu()
    
    print("Nous prenons "+str(nb_de_packets)+" packets")
    
    jeu = melanger(jeu)
    
    print(" ")
    print(" ")
    print("Packet melange")
    print(" ")


    for i in range(joueurs):
        Decks["player"+str(i+1)]['cards'][0] = hit(Decks["player"+str(i+1)]['cards'][0], jeu)

        print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][0][0][0])+" "+str(Decks["player"+str(i+1)]['cards'][0][0][1]))

        Decks["player"+str(i+1)]['cards'][0] = hit(Decks["player"+str(i+1)]['cards'][0], jeu)
        
        print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][0][1][0])+" "+str(Decks["player"+str(i+1)]['cards'][0][1][1]))
        print(" ")
    Decks["dealer"]['cards'][0] = hit(Decks["dealer"]['cards'][0],jeu)
    Decks["dealer"]['cards'][0] = hit(Decks["dealer"]['cards'][0],jeu)

    print("Le dealer a tire "+str(Decks["dealer"]['cards'][0][0][0])+" "+str(Decks["dealer"]['cards'][0][0][1]))

    
    

    for i in range(joueurs):
        print("TOUR DE JOUEUR "+str(Decks["player"+str(i+1)]['nom']))
        if counter_check(Decks["player"+str(i+1)]['cards'][0]) == 21:
            print("Blackjack!!! Bravo "+str(Decks["player"+str(i+1)]['nom']))
            Decks["player"+str(i+1)]['score']="Blackjack"
        
        yesorno="n"
        if Decks["player"+str(i+1)]['cards'][0][0][0] == Decks["player"+str(i+1)]['cards'][0][1][0]:
            yesorno=input("Vous avez deux cartes identiques voulez vous split a pair? (y/n)? ")

            if yesorno == "y":
                split_a_pair("player"+str(i+1), Decks, 0)
                print(Decks)
                Decks["player"+str(i+1)]['split'] = Decks["player"+str(i+1)]['split']+1
                Decks["player"+str(i+1)]['cards'][0] = hit(Decks["player"+str(i+1)]['cards'][0], jeu)
                Decks["player"+str(i+1)]['cards'][1] = hit(Decks["player"+str(i+1)]['cards'][1], jeu)
                Decks["player"+str(i+1)]['splitfini'] = False
                print(" ")
                print("Packet 1")
                print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][0][0][0])+" "+str(Decks["player"+str(i+1)]['cards'][0][0][1]))
                print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][0][1][0])+" "+str(Decks["player"+str(i+1)]['cards'][0][1][1]))
                print(" ")
                print("Packet2")
                print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][1][0][0])+" "+str(Decks["player"+str(i+1)]['cards'][1][0][1]))
                print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][1][1][0])+" "+str(Decks["player"+str(i+1)]['cards'][1][1][1]))
                print(" ")
                
                yesorno="n"
                yesorno=input("tirer une carte pour le premier mini packet? (y/n?)")
                if yesorno == "y":
                    Decks["player"+str(i+1)]['cards'][0] = hit(Decks["player"+str(i+1)]['cards'][0], jeu)
                    print(" ")
                    print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][0][0][0])+" "+str(Decks["player"+str(i+1)]['cards'][0][0][1]))
                    print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][0][1][0])+" "+str(Decks["player"+str(i+1)]['cards'][0][1][1]))
                    print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][0][2][0])+" "+str(Decks["player"+str(i+1)]['cards'][0][2][1]))

                yesorno="n"
                yesorno=input("tirer une carte pour le deuxieme mini packet? (y/n?)")
                if yesorno == "y":
                    Decks["player"+str(i+1)]['cards'][1] = hit(Decks["player"+str(i+1)]['cards'][1], jeu)
                    print(" ")
                    print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][1][0][0])+" "+str(Decks["player"+str(i+1)]['cards'][1][0][1]))
                    print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][1][1][0])+" "+str(Decks["player"+str(i+1)]['cards'][1][1][1]))
                    print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][1][2][0])+" "+str(Decks["player"+str(i+1)]['cards'][1][2][1]))
                
                yesorno="y"




        
        if yesorno != "y":
            yesorno=input("Abandonner? Ceci vous fera perdre la moitie de votre pari. (y/n)?")
            if yesorno == "y":
                Decks["player"+str(i+1)]['fini'] = True
                Decks["player"+str(i+1)]['money'] = Decks["player"+str(i+1)]['money']-Decks["player"+str(i+1)]['bet']
            else:
                yesorno = input("Voulez vous doubler la mise et tirer une derniere carte? (y/n)?")
                if yesorno == "y":
                    Decks["player"+str(i+1)]['fini'] = True
                    Decks["player"+str(i+1)]['bet'] = Decks["player"+str(i+1)]['bet']*2
                    Decks["player"+str(i+1)]['cards'][0] = hit(Decks["player"+str(i+1)]['cards'][0], jeu)
                    print(" ")
                    print(Decks["player"+str(i+1)]['cards'])
                    print(" ")
                else:
                    yesorno="n"
                    print("Vous avez")
                    print(Decks["player"+str(i+1)]['cards'])
                    yesorno=input("tirer une carte? (y/n?)")
                    if yesorno == "yes":
                        Decks["player"+str(i+1)]['cards'][0] = hit(Decks["player"+str(i+1)]['cards'][0], jeu)
                    
                    if counter_check(Decks["player"+str(i+1)]['cards'][0]) > 21:
                        print("BURN "+str(Decks["player"+str(i+1)]['nom']))
                        Decks["player"+str(i+1)]['score'] = counter_check(Decks["player"+str(i+1)]['cards'][0])
                        Decks["player"+str(i+1)]['fini'] = True

    over_check = False
    over_check=fini_check(Decks, joueurs)
    while over_check == False:
        for i in range(joueurs):
            if Decks["player"+str(i+1)]['fini'] == False:
                print("TOUR DU JOUEUR "+str(Decks["player"+str(i+1)]['nom']))
                print("Vos cartes sont:")
                print(Decks["player"+str(i+1)]['cards'])
                if Decks["player"+str(i+1)]['split'] == 0:
                    yesorno=input("Voulez vous rester?. (y/n)?")
                    if yesorno == "y":
                        Decks["player"+str(i+1)]['fini'] = True
                        yesorno=="n"
                    else:
                        Decks["player"+str(i+1)]['cards'][0] = hit(Decks["player"+str(i+1)]['cards'][0], jeu)
                        if counter_check(Decks["player"+str(i+1)]['cards'][0]) > 21:
                                    print("BURN "+str(Decks["player"+str(i+1)]['nom']))
                                    Decks["player"+str(i+1)]['score'] = counter_check(Decks["player"+str(i+1)]['cards'][0])
                                    Decks["player"+str(i+1)]['fini'] = True

                if Decks["player"+str(i+1)]['split'] == 1:
                    if Decks["player"+str(i+1)]['fini'] == False:
                        yesorno="n"
                        yesorno=input("Voulez vous tirer une carte? (y/n)?")
                        if yesorno == "y":    
                            Decks["player"+str(i+1)]['cards'][0] = hit(Decks["player"+str(i+1)]['cards'][0], jeu)
                            for j in range(len(Decks["player"+str(i+1)]['cards'][0])):
                                print(" ")
                                print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][0][j][0])+" "+str(Decks["player"+str(i+1)]['cards'][0][j][1]))

                                if counter_check(Decks["player"+str(i+1)]['cards'][0]) > 21:
                                    print("BURN "+str(Decks["player"+str(i+1)]['nom']))
                                    Decks["player"+str(i+1)]['score'] = counter_check(Decks["player"+str(i+1)]['cards'][0])
                                    Decks["player"+str(i+1)]['fini'] = True

                        else:
                            if counter_check(Decks["player"+str(i+1)]['cards'][0]) > 21:
                                    print("BURN "+str(Decks["player"+str(i+1)]['nom']))
                                    Decks["player"+str(i+1)]['score'] = counter_check(Decks["player"+str(i+1)]['cards'][0])
                                    Decks["player"+str(i+1)]['fini'] = True
                            if Decks["player"+str(i+1)]['fini'] == False: 
                                Decks["player"+str(i+1)]['fini'] = True
                                print(str(str(Decks["player"+str(i+1)]['nom'])+" reste."))
                    
                    if Decks["player"+str(i+1)]['splitfini'] == False:
                        yesorno="n"
                        yesorno=input("Voulez vous tirer une carte? (y/n)?")
                        if yesorno == "y":    
                            Decks["player"+str(i+1)]['cards'][1] = hit(Decks["player"+str(i+1)]['cards'][1], jeu)
                            for j in range(len(Decks["player"+str(i+1)]['cards'][1])):
                                print(" ")
                                print("Le Joueur "+Decks["player"+str(i+1)]['nom']+" a tire "+str(Decks["player"+str(i+1)]['cards'][1][j][0])+" "+str(Decks["player"+str(i+1)]['cards'][1][j][1]))

                                if counter_check(Decks["player"+str(i+1)]['cards'][1]) > 21:
                                    print("BURN "+str(Decks["player"+str(i+1)]['nom']))
                                    Decks["player"+str(i+1)]['score'] = counter_check(Decks["player"+str(i+1)]['cards'][1])
                                    Decks["player"+str(i+1)]['splitfini'] = True

                        else:
                            if counter_check(Decks["player"+str(i+1)]['cards'][1]) > 21:
                                    print("BURN "+str(Decks["player"+str(i+1)]['nom']))
                                    Decks["player"+str(i+1)]['score'] = counter_check(Decks["player"+str(i+1)]['cards'][1])
                                    Decks["player"+str(i+1)]['splitfini'] = True
                            if Decks["player"+str(i+1)]['splitfini'] == False:
                                Decks["player"+str(i+1)]['splitfini'] = True
                                print(str(str(Decks["player"+str(i+1)]['nom'])+" reste."))
        over_check=fini_check(Decks, joueurs)

    print("game over")


