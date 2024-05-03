# PROJET BLACK JACK
import random


### but du jeu obtenir un score supérieur a la banque sans dépasser 21
j1=[]# packet du joueur
b=[] # packet de la banque
pack=["As",2,3,4,5,6,7,8,9,10,"roi","dame","valet"] #packet de carte
miseJ=int(input("combien voulez vous miser"))#mise du joueur
miseJ2=0
miseV2=0
miseV3=0
#distribution de carte aléatoirement au joueur et à la banque
for k in range(2):
    valeur_ajoutee = random.choice(pack)  # Choix aléatoire d'une valeur
    j1.append(valeur_ajoutee)
for k in range(1):
    vj=random.choice(pack)
    b.append(vj)

#score de la banque et du joueur
scorej1=0
scorebanque=0       

#calcul du score après distribution
for n in j1:
    if n == "valet" or n == "roi" or n == "dame":
        scorej1 += 10
    elif n == "As":
        if scorej1 + 11 <= 21:
            scorej1 += 11
        else:
            scorej1 += 1
    else:
        scorej1 += n


for n in b:
    if n == "valet" or n == "roi" or n == "dame":
        scorebanque += 10
    elif n == "As":
        if scorebanque + 11 <= 21:
            scorebanque += 11
        else:
            scorebanque += 1
    else:
        scorebanque += n


print(j1,"joueur1 a ",scorej1,"point")
print(b,"Banque a ",scorebanque,"point")

#ajoute une carte caché à la banque
carte=random.choice(pack)    
b.append(carte)
# ajoute des cartes à la banque tant que le score n'a pas atteint 17 ou plus
while scorebanque<17:
    cart=random.choice(pack)
    b.append(cart)
    if cart == "valet" or cart== "roi" or cart== "dame":
        scorebanque += 10
    elif cart == "As":
        if scorebanque + 11 <= 21:
            scorebanque += 11
        else:
            scorebanque += 1
    else:
        scorebanque += cart

# si le joueur n'a pas fait un blackjack ou n'a pas atteint un score au dessus de 21 il tire une carte s'il le veut    
if scorej1<21:
    m=str(input("joueur 1 voulez-vous tirez une carte? "))
    if m=="oui" or m=="OUI" or m=="Oui":
        valeur_ajouteee = random.choice(pack)
        j1.append(valeur_ajouteee)
        print("--------------")
        wx=j1[2]
        if wx == "valet" or wx == "roi" or wx == "dame":
                scorej1 += 10
        elif wx == "As":
                if scorej1 + 11 <= 21:
                    scorej1 += 11
                else:
                    scorej1 += 1
        else:
                scorej1 += wx
        print(j1,"joueur1 a ",scorej1,"point")       

# si le joueur a deux meme carte (exemple: [8,8]) il peut choisir de deviser son pack en deux mains 
sco1=0
sco1b=0    
if j1[0]==j1[1] and len(j1)==2:
         choix=str(input("voulez vous split votre packet"))
         miseJ2=miseJ
         if choix=="oui" or choix== "OUI"  or choix=="Oui":
            c=j1[1]
            tab1=[]
            tab1.append(c)
            tab3=[]
            tab3.append(c)
            print("le packet du joueur 1 a été séparer",tab3,tab1,"mise packet 1:",miseJ,"mise packet 2:",miseJ2)
            abc=0
            pi=str(input("voulez vous piocher pour le premier paquet"))
            if pi=="oui" or pi=="OUI" or pi=="Oui":
                 baka= random.choice(pack)
                 tab1.append(baka)
                 cdg=0
                 if c=="roi" or c=="dame" or c=="valet":
                  abc=10
                  if baka == "valet" or baka == "roi" or baka == "dame": #essai de voir si tu peux pas mettre ça dans les if c==.... genre tu fais les baka dans les if c== comme ça ça peut marcher
                    sco1 += 10+abc
                  elif baka == "As":
                    if abc + 11 <= 21:
                        sco1 += 11+abc
                    else:
                        sco1 += 1+abc                 
                  else:
                    sco1+=baka+abc
                 if c=="As":
                      if baka!="valet" or baka!="roi" or baka!="dame" or baka!="As":
                           if sco1+baka+11<=21:
                                abc=11
                                sco1+=baka+abc
                           else:
                                abc=1
                                sco1+=baka+abc
                      if baka=="valet" or baka=="roi" or baka=="dame" or baka=="As":
                            cdg=10
                            if sco1+cdg+11<=21:
                                 abc=11
                                 sco1+=cdg+abc
                            else:
                                 abc=1
                                 sco1+=cdg+abc
                      if baka=="As":
                           cdg=1
                           sco1+=cdg+11    
                 if c!="valet" and c!="roi" and c!="dame" and c!="As":
                        if baka=="valet" or baka=="roi" or baka=="dame":
                                cdg=10
                                sco1+=cdg+c
                        if baka=="As":
                            if sco1+c+11<=21:
                                sco1+=c+11
                            else:
                                sco1+=c+1
                        if baka!="valet" and baka!="roi" and baka!="dame" and baka!="As":
                            sco1+=c+baka
                 print("premier paquet du joueur 1",tab1,sco1)
                 ad=str(input("voulez vous repiocher"))
                 if ad=="oui" or ad=="OUI" or ad=="Oui":
                     baka= random.choice(pack)
                     tab1.append(baka)
                     if baka == "valet" or baka == "roi" or baka == "dame":
                        sco1 += 10
                     elif baka == "As":
                        if sco1 + 11 <= 21:
                            sco1 += 11
                        else:
                            sco1 += 1
                     
                     else:
                        sco1+=baka
                     print("le premier paquet du joueur 1",tab1,sco1)

                 
              
            co= str(input("voulez vous piocher pour le deuxieme paquet"))
            if co!="oui" or co!="OUI" or co!="Oui":
                print("le deuxieme paquet du joueur 1",tab3,sco1b)    
            if co=="oui" or co=="OUI" or co=="Oui":
                bakaa= random.choice(pack)
                tab3.append(bakaa)
                cdg=0
                abc=0
                if c=="roi" or c=="dame" or c=="valet":
                  abc=10
                  if bakaa == "valet" or bakaa == "roi" or bakaa == "dame":
                    sco1b += 10+abc
                  elif bakaa == "As":
                    if abc + 11 <= 21:
                        sco1b += 11+abc
                    else:
                        sco1b += 1+abc                 
                  else:
                    sco1b+=bakaa+abc
                if c=="As":
                      if bakaa!="valet" or bakaa!="roi" or bakaa!="dame" or bakaa!="As":
                           if sco1b+bakaa+11<=21:
                                abc=11
                                sco1b+=bakaa+abc
                           else:
                                abc=1
                                sco1b+=bakaa+abc
                      if bakaa=="valet" or bakaa=="roi" or bakaa=="dame" or bakaa=="As":
                            cdg=10
                            if sco1b+cdg+11<=21:
                                 abc=11
                                 sco1b+=cdg+abc
                            else:
                                 abc=1
                                 sco1b+=cdg+abc
                      if bakaa=="As":
                           cdg=1
                           sco1b+=cdg+11    
                if c!="valet" and c!="roi" and c!="dame" and c!="As":
                        if bakaa=="valet" or bakaa=="roi" or bakaa=="dame":
                                cdg=10
                                sco1b+=cdg+c
                        if bakaa=="As":
                            if sco1b+c+11<=21:
                                sco1b+=c+11
                            else:
                                sco1b+=c+1
                        if bakaa!="valet" and bakaa!="roi" and bakaa!="dame" and bakaa!="As":
                            sco1b+=c+bakaa
                print("le deuxieme paquet du joueur 1",tab3,sco1b)
                add=str(input("voulez vous repiocher"))
                if add=="oui" or add=="OUI" or add=="Oui":
                    bakaa= random.choice(pack)
                    tab3.append(bakaa)
                    if bakaa == "valet" or bakaa == "roi" or bakaa == "dame":
                        sco1b += 10
                    elif bakaa == "As":
                        if sco1b + 11 <= 21:
                            sco1b += 11
                        else:
                            sco1b += 1
                     
                    else:
                        sco1b+=bakaa
                    print("le deuxieme paquet du joueur 1",tab3,sco1b)
            #compare les scores pour savoir qui a gagné        
            if sco1>21:
                print("la premiere main du joueur 1 a perdu")
            elif sco1==21:
                miseV3=miseJ*2.5
                print("la premiere main du joueur 1 a fait un blackjack sa mise gagné est",miseV3)
            if sco1b>21:
                print("la deuxieme main de joueur 1 a perdu donc cette main perd sa mise")
            elif sco1b==21:
                miseV4=miseJ2*2.5
                print("la deuxieme main du joueur 1 a gagné")
            if scorebanque>sco1:
                 print("la banque a gagné sur la premiere main la premiere mise est perdu")
            if scorebanque<sco1:
                 print("la premiere main a gagné et joueur gagne sa mise",miseJ)
            if scorebanque>sco1b:
                 print("la banque a gagné sur la deuxieme main et le joueur perd sa mise")
            if scorebanque<sco1b:
                 print("la deuxieme main a gagné a gagné et le joueur gagne sa mise",miseJ2)
            if scorebanque==sco1b:
                 print("PUSH")
            if scorebanque==sco1:
                 print("PUSH")
print(b,"le score de la banque est",scorebanque)    
#compare les scores pour savoir qui a gagné                    
if scorebanque<=21 :
                if scorebanque>scorej1:
                    print("la banque a gagner, et le joueur perd sa mise")
if scorej1<=21: 
     if scorebanque<scorej1:
                    print("le joueur a gagné, le joueur gagne sa mise",miseJ)
     if scorebanque>21:
          print("le joueur a gagné, le joueur gagne sa mise car la banque a BUST",miseJ)
#cas ou le joueur fait un blackjack ou la banque
def blackjack(sco1,sco1b,scorebanque,scorej1):
    if sco1==21:
        miseV2=miseJ*2.5
        print("la premiere main a fait un blackjack",miseV2)
    if sco1b==21:
        #miseJ2=*2.5
        print("la deuxieme main a fait un blackjack",miseJ2)
    if scorebanque==21:
        print("la banque a fait un blackjack")
    if scorej1==21:
        print("le joueur a fait un blackjack")
        miseV2=miseJ*2.5
        print("le joueur gagne 2.5 fois sa mise","mise gagné:",miseV2)
print(blackjack(sco1,sco1b,scorebanque,scorej1))

#cas ou le joueur ou la banque a perdu
def perdu(scorej1,scorebanque):
     if scorej1>21:
          print("joueur 1 a bust donc il perd sa mise")
     if scorebanque>21:
          print("banque perdu")
     if scorej1>21 and scorebanque>21:
          print("la banque et le joueur ont bust")
perdu(scorej1,scorebanque)
#cas d'égalité
if scorebanque==scorej1:
     print("Push, le joueur récupère rien et ne perd rien")