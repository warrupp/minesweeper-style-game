#travail fait par:
#yassine benbouabid 20257585
#ines amelia chafai 20265344
#nom du programme: jeu des pieces
import time
nbErreur=0
def init(): #la function init initialise le jeu, j'ai aussi ajoute quelque variable a remettre a zero  
    global nbErreur #pour reinitialiser le jeu lorqu'on perd, gagne ou appuie sur le bouton nouvelle partie
    nbErreur=0
    global main
    main = document.querySelector("#main")
    main.innerHTML = """
      <button onclick="init()">Nouvelle partie</button>
      <div id="jeu" class="centered">
      <h1 id="msg"></h1>
      <table>"""+'<pre id="nbsous" ></pre>' + grille()
    Scoreboard()

def piece():#la fonction piece choisi un nombre aleatoire entre 15 et 20 pour le nombre de pieces
    global nb #nb est le nombre de piece
    nb=int(random()*6+15)
    global pos
    pos=[]#on initialise un tableau pour stocker la position des pieces
    global posVoisine
    posVoisine=[0]#on initialise un tableau pour stocker la position des cases voisines
    while len(pos) != nb:#pour eviter de mettre une piece a cote de l'autre et aussi pour le attribue un indicateur plustard
        x=int(random()*100)#on choisi de facon aleatoire une position entre a 1 et 100 pour placer une piece dedans
        if x in posVoisine or x in pos:#si cette position est deja choisi ou est adjacente on l'ignore
            pass
        else:#une fois une position choisi on enregistre les positions adjacentes dans notre tableaux
            if x%10==1:#si cette position est dans la premiere column on ne doit pas enregister les positions a gauche
              pos.append(x)#sinon notre code enregistrera la case a l'oppose qui n'est pas vraiment adjacente
              posVoisine.append(x-10)
              posVoisine.append(x+10)
              posVoisine.append(x-9)
              posVoisine.append(x+11)
              posVoisine.append(x+1)
            elif x%10==0:#meme chose si la case est dans la derniere column on ne doit pas enregistrer les cases a sa droite
              pos.append(x)#sinon on a le meme probleme
              posVoisine.append(x-1)
              posVoisine.append(x-10)
              posVoisine.append(x+10)
              posVoisine.append(x-11)
              posVoisine.append(x+9)
            else:  
              pos.append(x)#si la case est dans les column du millieux la y'a pas de probleme tout les cases peuvent etre enregistrer
              posVoisine.append(x-1)
              posVoisine.append(x+1)
              posVoisine.append(x+10)
              posVoisine.append(x-10)
              posVoisine.append(x+11)
              posVoisine.append(x-11)
              posVoisine.append(x+9)
              posVoisine.append(x-9)
    posVoisine = list(filter(lambda x: x > 0 and x<=100, posVoisine))#notre code peut enregistrer des positions de cases qui sont hors de notre grille
    return pos,posVoisine  # du coup on va juster les filtrer 

def grille():#cette fonction cree notre grille et assigne a chaque case un ID
    piece()
    indications()    
    s=0
    grille=""
    for n in range(10):
        grille+="<tr>"
        for i in range(10):
            s+=1
            if s in pos:
                grille+='<td id="case'+str(s)+'" onclick="victoire('+str(s)+')"></td>'#on a deux type de cases celle avec les pieces et les autres
            else:#celle avec les pieces on met dedans les pieces cache et on enregistre si il on etait cliquer ou pas 
                grille+='<td id="case'+ str(s)+'"onclick="clicAutre()">'+str(ind[s-1])+'</td>'#les autres on enregistre seulement si il sont cliquer
        grille+="</tr>"
    grille+="<table>"
    return grille    

def indications():#cette fonction cree un tableaux qui indique les chiffres a mettre dans les cases pour indiquer les positions des cases
    global ind#on prend le tableaux de positions voisine est on verifie combien de fois une case apparait dedans tout simplement 
    ind=[0]*100#si par exemple elle apparait de fois dans posVoisine alors cette case devra avoir le chiffre 2 dedans
    for i in posVoisine:
        ind[i-1]+=1
    for t in range(len(ind)):
        if ind[t]==0:
            ind[t]=""
    return ind#on retourne ce tableaux des indicateurs qu'on mettra dans nos cases



def clicAutre():#cette fonction enregistre si on a cliquer une cases qui n'a pas de pieces si on repete 3 fois on perd
    h1=document.querySelector('#msg')
    global nbErreur
    nbErreur+=1
    Scoreboard()
    if nbErreur==3:
        h1.innerHTML="Vous avez perdu!"#si on fait 3 erreur on affiche le message de defaite
        main.innerHTML+='<div id="overlay"><div>'#on ajoute une couche invisible sur notre page qui nous bloque de cliquer d'autre case
        sleep(10)#on utilise la fonction sleep pour arreter le jeu pendant 10 secondes
        nbErreur=0
        init()#apres les 10 seconds on reinitialise le jeu 
        
    
      
def element(id):#cette fonction nous retourne l'element avec l'ID rechercher
    return document.querySelector('#' + id)



def case(index):#cette fonction nous retourne la case avec le chiffre rechercher
    return element('case' + str(index))



def Scoreboard():#cette fonction affiche le nombre d'erreur et de pieces restante
    sb=document.querySelector('#nbsous')
    sb.innerHTML="Erreur:"+str(nbErreur)+"                             sous cache:"+str(nb)



def victoire(index):#cette fonction enregistre si on a cliquer une case avec une piece
    global nb
    case(index). innerHTML = '<img  src="symboles\coste.svg">'#si une piece est cliquer on l'affiche
    h1=document.querySelector('#msg')
    nb=nb-1#est on retire 1 au nombre de pieces restante
    Scoreboard()
    if nb==0:#si tout les pieces sont trouver on affiche le message de victoire et on relance de jeux apres 10secondes
        h1.innerHTML="Vous avez Gagne!"
        main.innerHTML+='<div id="overlay"><div>'#on utilise encore l'overlay pour eviter d'enregistrer d'autres clique pour eviter des bugs
        sleep(10)
        nbErreur=0
        init()
        
def Test():#dans notre code on a seulement 2 fonction de calcul
    piece()  # du coup on s'assure que piece nous donne toujours un nombre de piece entre entre 15 et 20
    PosLen = len(pos)
    assert 15 <= PosLen <= 20
    indications()#on verifie que les cases ont des indications 1,2,3 ou 4 ou pas d'indications si aucune piece est adjacentes
    for q in ind:
        assert q in [1,2,3,4,""]



Test()#on appel notre fonction de test
    