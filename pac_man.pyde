from random import randint
from pc import *
TAILLE_GRILLE = 21
TAILLE_CASE = 40
afficher = "accueil"


def setup():
    size(TAILLE_GRILLE*TAILLE_CASE,TAILLE_GRILLE*TAILLE_CASE)
    background(0)
    f = createFont("crackman.ttf",24)
    textFont(f)
    frameRate(7) 
    
with open("grille1.csv", "r") as fichier :
    grille = []
    for ligne in fichier :
        l = ligne.split(',')
        for i in range(len(l)):
            l[i]=l[i].strip("\r\n")
        grille.append(l)

def draw():
    global afficher
    if afficher == "accueil":
        ecran_accueil()
        fermer()
    elif afficher == "rejouer":
        bouton_rejouer()
    elif afficher == "jouer":
        jeu()
        
def jeu():
    afficher_grille(grille)
    afficher_pacman(p) 
    entree_clavier(p)
    avancer(p)
    
        
            
def afficher_grille(grille):
    global mur,vide
    y = 0
    for i in range(len(grille)) :
        x = 0
        for j in range(len(grille[i])) :
            if grille[i][j] == "10":
                mur(y,x)
            elif grille[i][j] == "1":
                vide(y,x)
            elif grille[i][j] == "5":
                vide(y,x)
                pastille(x,y)
            elif grille[i][j] == "7":
                bloque(y,x)
            elif grille[i][j] == "3":
                vide(y,x)
                bonbon(x,y)
            x = x + TAILLE_CASE
        y = y + TAILLE_CASE

        
def mur(x,y):
    global TAILLE_CASE
    stroke(0,53,255)
    fill(0)
    square(y,x,TAILLE_CASE)

def vide(x,y):
    global TAILLE_CASE
    noStroke()
    fill(0,53,255)
    square(y,x,TAILLE_CASE)
    
def bloque(x,y):
    global TAILLE_CASE
    noStroke()
    fill(0,189,255)
    square(y,x,TAILLE_CASE)
    
def pastille(x,y):
    global TAILLE_CASE
    fill(255,234,0)
    circle(x+TAILLE_CASE//2,y+TAILLE_CASE//2,TAILLE_CASE//1.5)

def bonbon(x,y):
    global TAILLE_CASE
    fill(255,234,0)
    circle(x+TAILLE_CASE//2,y+TAILLE_CASE//2,TAILLE_CASE//2-10)
    
def entree_clavier(p):
    if key == CODED :
        if keyCode == RIGHT :
            p["d"] = "droite"
        elif key == LEFT :
            p["d"] = "gauche"
        elif key == UP :
            p["d"] = "haut"
        elif key == DOWN :
            p["d"] = "bas"
    return p
            
    
############################Fonction du menu####################################

def ecran_accueil():
    global afficher
    texte_menu()
    if bouton() == True:
        afficher = "jouer"
            
def bouton():
    if  152< mouseX < 152 + 240 and  500< mouseY < 500 + 100 :
        textSize(60)
        fill (200,200,0)
        rect(152,500,230,100,8)
        fill(0,0,0)
        text("Jouer",170,570,0)
        if mousePressed :
            return True
    else:
        textSize(60)
        fill (255,243,0)
        rect(152,500,230,100,8)
        fill(0,0,0)
        text("Jouer",170,570,0)
    return False

def fermer():
        if  450< mouseX < 440 + 240 and  500< mouseY < 500 + 100 :
            textSize(55)
            fill (200,200,0)
            rect(450,500,230,100,8)
            fill(0,0,0)
            text("Fermer",460,565,0)
            if mousePressed :
                exit()
        else:
            textSize(55)
            fill (255,243,0)
            rect(450,500,230,100,8)
            fill(0,0,0)
            text("Fermer",460,565,0)    
    
def texte_menu():
    fill(255,243,0)
    textSize(140)
    text("pac-man",100,250,0)
    textSize(40)
    text("Utilisez les touches: z-q-s-d",80,380) 
    text("pour vous deplacez.",190,420)
       
def texte_rejouer():
    fill(255,0,0)
    textSize(50)
    text("Vous etes mort",150,130,0)
    fill(255,255,255)
    textSize(40)
    text("Votre record :",150,200,0)
    text(recor,430,200,0) 
    text("Votre score :",150,260,0)
    text(score_bis,430,260,0) 

def rejouer():
    if  88< mouseX < 88 + 200 and  345< mouseY < 345 + 100 :
        textSize(45)
        fill (255,255,255)
        rect(88,345,200,100,8)
        fill(0,0,0)
        text("Rejouer",105,410,0)
        if mousePressed :
            return True
    else:
        textSize(45)
        fill (255,255,255)
        rect(88,345,200,100,8)
        fill(0,0,0)
        text("Rejouer",105,410,0)
    return False

def menu():
        if  350< mouseX < 300 + 200 and  345< mouseY < 345 + 100 :
            textSize(50)
            fill (255,255,255)
            rect(350,345,200,100,8)
            fill(0,0,0)
            text("Menu",380,410,0)
            if mousePressed :
                return True
        else:
            textSize(50)
            fill (255,255,255)
            rect(350,345,200,100,8)
            fill(0,0,0)
            text("Menu",380,410,0)  
        return False

def bouton_rejouer():
    global afficher
    texte_rejouer()
    rejouer()
    menu()
    if rejouer() == True:
        afficher = "jouer"
    elif menu() == True:
        afficher = "accueil"
        
        

    
