#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame
from pygame.locals import *
import mysql.connector
from classes import *
from constantes import *
from database import *
import random
import os
import requete0
import importlib
import time

def écriture(fichier, liste):
    with open(fichier, 'w') as file:
        file.write('a = ')
        file.write(str(liste))
        
def fichier():
    liste2 = []
    liste = os.listdir()
    for i in liste:
        if i == 'classes.py'\
           or i == 'config.py'\
           or i == 'constantes.py'\
           or i == 'database.py'\
           or i == 'databasedk.py'\
           or i == 'dklabyrinthe.py'\
           or i == 'essais.py'\
           or i == 'images'\
           or i == 'n1'\
           or i == 'n2'\
           or i == '__pycache__':
                pass
        else:
                liste2.append(i)

    nb = liste2[-1][-4]
    nb = int(nb)
    nouvau_nb = nb + 1
    nouveau_file = 'requete' + str(nouvau_nb) + '.py'
    print(nouveau_file)
    return nouveau_file


def trait_list(a):
    print(a)
    a = str(a)
    a = a[7:-4]
    
    listeeee = []
    for i in a:

        if i == "'" or i == ",":
            pass
        else:
            listeeee.append(i)
    print(listeeee)
    listeeee = "".join(listeeee)
    listeeee = listeeee.split()

 
    print(len(listeeee))
    print(listeeee)

    return listeeee


LISTE_CHOIX  = []
LISTE_CASE = []
LISTE_POS = ['right', 'left', 'top', 'bot']

class main:

    def menu(self):
        
        pygame.init()
        print(requete0.REQUETE0)

        fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
  
        icone = pygame.image.load(image_icone)
        pygame.display.set_icon(icone)
  
        pygame.display.set_caption(titre_fenetre)


        FILE = fichier()
 
        continuer = 1
        while continuer:	
  
            accueil = pygame.image.load(image_accueil).convert()
            fenetre.blit(accueil, (0,0))

            pygame.display.flip()
         
            level = Niveau.choice_level(self)

            return level, fenetre



    def generate_level(self, choix, fenetre):

        print(choix)
     
        if choix != 0:

            fond = pygame.image.load(image_fond).convert()

            niveau = Niveau(choix)
            niveau.generer()
            niveau.afficher(fenetre)

      
            dk = Perso("images/dk_droite.png", "images/dk_gauche.png", 
            "images/dk_haut.png", "images/dk_bas.png", niveau)

            return dk, fond, niveau



    def trying(self, dk, fenetre, fond, niveau):

        print(requete0.REQUETE0 >= 100)
        
        if requete0.REQUETE0 >= 100:
            a = visualisation_table.visualisation(self)
            listeeee = trait_list(a)

            for i in listeeee:
                print(i)
                dep = dk.deplacer(str(i))
                
                with open('requete0.py', 'w') as file:
                    file.write('REQUETE0 = ')
                    file.write(str(requete0.REQUETE0 + 1))
                importlib.reload(requete0)

                fenetre.blit(fond, (0,0))
                niveau.afficher(fenetre)
                fenetre.blit(dk.direction, (dk.x, dk.y)) 
                pygame.display.flip()



    def moving(self, direction, listed, dk):
        self.direction = direction
        self.listed = listed
        self.dk = dk

        
        a = self.dk.deplacer(self.direction)
        LISTE_CHOIX.append(self.direction)
        try:
            if a[1] == 's':
                if a[0] >= len(LISTE_CHOIX):
                    print(LISTE_CHOIX)
                    insertion_table.insertion_move(self, str(LISTE_CHOIX))
                    continuer_jeu = 0
                    return continuer_jeu
                
                elif a[0] < len(LISTE_CHOIX):
                    continuer_jeu = 0
                    return continuer_jeu
                    
                if a[0] == len(LISTE_CHOIX):
                    if REQUETE0 >= 100:
                        with open('requete0.py', 'w') as file:
                            file.write('REQUETE0 = ')
                            file.write(str(requete0.REQUETE0 + 1))      
        except:
            pass
        if a == 'M':
            choix = random.choice(self.listed)
            dep = dk.deplacer(choix)




    def game(self, dk, fenetre, fond, niveau):
        print("yoooooooooooooooooooooooooooooooooo")
        
        continuer_jeu = 1
        while continuer_jeu:
            
            choix = random.choice(LISTE_POS)

            listed = ['left', 'top', 'bot']
            listeh = ['left', 'right', 'bot']
            listeb = ['left', 'top', 'right']
            listeg = ['right', 'top', 'bot']
            
            if choix == 'right':
                cont = main.moving('droite', listed, dk)
                if cont == 0:
                    continuer_jeu = 0
            if choix == 'left': 
                cont = main.moving('gauche', listeg, dk)
                if cont == 0:
                    continuer_jeu = 0
            if choix == 'bot':
                cont = main.moving('bas', listeb, dk)
                if cont == 0:
                    continuer_jeu = 0
            if choix == 'top':
                cont = main.moving('haut', listeh, dk)
                if cont == 0:
                    continuer_jeu = 0

   
            fenetre.blit(fond, (0,0))
            niveau.afficher(fenetre)
            fenetre.blit(dk.direction, (dk.x, dk.y)) 
            pygame.display.flip()


            if niveau.structure[dk.case_y][dk.case_x] == 'a':
                continuer_jeu = 0
                print(LISTE_CHOIX)
                print(LISTE_CASE)
           






if __name__ == '__main__':
    
    main = main()
    choice = main.menu()
    perso = main.generate_level(choice[0], choice[1])

    if requete0.REQUETE0 >= 5:
        main.trying(perso[0], choice[1], perso[1], perso[2])
    else:
        main.game(perso[0], choice[1], perso[1], perso[2])



















































