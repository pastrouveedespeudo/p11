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


LISTE_CHOIX  = []
LISTE_CASE = []


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



    def trying(self, dk):

        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
  
            if event.type == QUIT:
                    continuer_jeu = 0
                    continuer = 0
        

        if requete0.REQUETE0 >= 5:
            a = visualisation_table.visualisation(self)
            a = str(a)
            a = a[7:-4]
            
            listeeee = []
            for i in a:

                if i == "'" or i == ",":
                    pass
                else:
                    listeeee.append(i)
            
            listeeee = "".join(listeeee)
            listeeee = listeeee.split()

         
            print(len(listeeee))
            for i in listeeee:
                print(i)
                dep = dk.deplacer(str(i))
                
                with open('requete0.py', 'w') as file:
                    file.write('REQUETE0 = ')
                    file.write(str(requete0.REQUETE0 + 1))
                importlib.reload(requete0)


    def game(self, dk, fenetre, fond, niveau):
        
        continuer_jeu = 1
        while continuer_jeu:
            
            liste = ['right', 'left', 'top', 'bot']
            choix = random.choice(liste)


            if choix == 'right':
                a = dk.deplacer('droite')
                LISTE_CHOIX.append('droite')

                try:
                    if a[1] == 's':
                        print(a[0])
                        print(len(LISTE_CHOIX))
                        
                        if a[0] >= len(LISTE_CHOIX):
                            print("oui")
                            insertion_table.insertion_climat(self, str(LISTE_CHOIX))
                            continuer_jeu = 0
                            
                        elif a[0] < len(LISTE_CHOIX):
                            continuer_jeu = 0
                            
                        if a[0] == len(LISTE_CHOIX):
                            if REQUETE0 == 5:
                                pass
                            else:
                                with open('requete0.py', 'w') as file:
                                    file.write('REQUETE0 = ')
                                    file.write(str(REQUETE0 + 1))
                                
                except:
                    pass
                if a == 'STOP':
                    continuer_jeu = 0
                if a == 'M':
                    liste1 = ['left', 'top', 'bot']
                    choix = random.choice(liste1)

                    dep = dk.deplacer(choix)
       
                    


                    
            elif choix == 'left':
                b = dk.deplacer('gauche')
                LISTE_CHOIX.append('gauche')


                try:
                    if c[1] == 's':
                        print(b[0])
                        print(len(LISTE_CHOIX))
                        
                        if b[0] >= len(LISTE_CHOIX):
                            print("oui")
                            insertion_table.insertion_climat(self, str(LISTE_CHOIX))
                            continuer_jeu = 0
                            
                        elif a[0] < len(LISTE_CHOIX):
                            continuer_jeu = 0
                            
                        if a[0] == len(LISTE_CHOIX):
                            if REQUETE0 == 5:
                                pass
                            else:
                                with open('requete0.py', 'w') as file:
                                    file.write('REQUETE0 = ')
                                    file.write(str(REQUETE0 + 1))
                except:
                    pass
                
                if b == 'STOP':
                    continuer_jeu = 0
                if b == 'M':
                    liste1 = ['right', 'top', 'bot']
                    choix = random.choice(liste1)
             
                    dep = dk.deplacer(choix)
          



          
            elif choix == 'top':
                c = dk.deplacer('haut')
                LISTE_CHOIX.append('haut')
          
                try:
                    if c[1] == 's':
                        print(c[0])
                        print(len(LISTE_CHOIX))
                        
                        if c[0] >= len(LISTE_CHOIX):
                            print("oui")
                            insertion_table.insertion_climat(self, str(LISTE_CHOIX))
                            continuer_jeu = 0
                            
                        elif a[0] < len(LISTE_CHOIX):
                            continuer_jeu = 0
                            
                        if a[0] == len(LISTE_CHOIX):
                            if REQUETE0 == 5:
                                pass
                            else:
                                with open('requete0.py', 'w') as file:
                                    file.write('REQUETE0 = ')
                                    file.write(str(REQUETE0 + 1))
                except:
                    pass
                
                if c == 'STOP':
                    continuer_jeu = 0
                if c == 'M':
                   liste1 = ['right','left', 'bot']
                   choix = random.choice(liste1)

                   dep = dk.deplacer(choix)
          
                   
            elif choix == 'bot':
                d = dk.deplacer('bas')
                LISTE_CHOIX.append('bas')
      
                try:
                    if d[1] == 's':
                        print(d[0])
                        print(len(LISTE_CHOIX))
                        if  d[0] >= len(LISTE_CHOIX):
                            print('oui')
                            insertion_table.insertion_climat(self, str(LISTE_CHOIX))
                            continuer_jeu = 0
                            
                        elif a[0] < len(LISTE_CHOIX):
                            continuer_jeu = 0
                            
                        if a[0] == len(LISTE_CHOIX):
                            if REQUETE0 == 5:
                                pass
                            else:
                                with open('requete0.py', 'w') as file:
                                    file.write('REQUETE0 = ')
                                    file.write(str(REQUETE0 + 1))
                except:
                    pass
                    
                if d == 'STOP':
                    continuer_jeu = 0
                if d == 'M':
                    liste1 = ['right', 'left', 'top']
                    choix = random.choice(liste1)
            
                    dep = dk.deplacer(choix)
            

   
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
    main.trying(perso[0])
    main.game(perso[0], choice[1], perso[1], perso[2])



















































