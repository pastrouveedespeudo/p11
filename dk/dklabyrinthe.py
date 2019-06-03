#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
files : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
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
import argparse

def writting(file, liste):
    'function for writing into file'

    listee = []
    with open(file, 'w') as filee:
        filee.write("a = '")
        filee.write(str(liste))
        filee.write("'")
        filee.close()

    with open(file, 'r') as filee:
        a = filee.read()
        listee.append(str(a))

    return listee



def file():
    'function for write into a new file (we take last file and add + 1)'

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
           or i == '__pycache__' or i == 'test_dk.py' or i =='test_database.py'\
           or i == '.coverage' or i == 'test.py' or i=='test':
                pass
        else:
            liste2.append(i)
    print(liste2)
    nb = liste2[-1][-4]
    nb = int(nb)
    new_nb = nb + 1
    new_file = 'requete' + str(new_nb) + '.py'

    return new_file


def trait_list(a):
    'we trating list like the return from database'

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
    print(listeeee)
    return listeeee


LISTE_CHOICE  = []
LISTE_CASE = []
LISTE_POS = ['right', 'left', 'top', 'bot']

class main:
    'class main'
    
    def menu(self):
        'we generating menu, here we choice the level'
        
        pygame.init()
        print(requete0.REQUETE0)

        window = pygame.display.set_mode((side_window, side_window))
  
        icone = pygame.image.load(image_icone)
        pygame.display.set_icon(icone)
  
        pygame.display.set_caption(title_window)


        FILE = file()
 
        continuer = 1
        while continuer:	
  
            accueil = pygame.image.load(image_accueil).convert()
            window.blit(accueil, (0,0))

            pygame.display.flip()
         
            level = Niveau.choice_level(self)

            return level, window



    def generate_level(self, choice, window):
        'we generating the level thank to n1.txt'
        
        if choice != 0:

            background = pygame.image.load(image_background).convert()

            level = Niveau(choice)
            level.generate()
            level.display(window)

      
            dk = Perso("images/dk_droite.png", "images/dk_gauche.png", 
            "images/dk_haut.png", "images/dk_bas.png", level)
          
            return dk, background, level



    def trying(self, dk, window, background, level):
        'if requete0 is > 100 we let dk move alone'

        print(requete0.REQUETE0 >= 100)
        
        if requete0.REQUETE0 >= 100:
            a = visualisation_table.visualisation(self)
            listeeee = trait_list(a)

            for i in listeeee:
                print(i)
                dep = dk.deplacement(str(i))

                window.blit(background, (0,0))
                level.display(window)
                window.blit(dk.direction, (dk.x, dk.y)) 
                pygame.display.flip()


    def moving(self, direction, listed, dk):
        'Here dk can learn how found exit'

        self.direction = direction
        self.listed = listed
        self.dk = dk

        
        a = self.dk.deplacement(self.direction)
        LISTE_CHOICE.append(self.direction)
        try:
            if a[1] == 's':
                if a[0] <= len(LISTE_CHOICE):
                    insertion_table.insertion_move(self, str(LISTE_CHOICE))
                    continue_game = 0
                    return continue_game
                
                elif a[0] > len(LISTE_CHOICE):
                    continue_game = 0
                    return continue_game
                    
                if a[0] == len(LISTE_CHOICE):
                    with open('requete0.py', 'w') as file:
                        file.write('REQUETE0 = ')
                        file.write(str(requete0.REQUETE0 + 1))      
        except:
            pass
        if a == 'M':
            choice = random.choice(self.listed)
            dep = dk.deplacement(choice)




    def game(self, dk, window, background, level):
        'dk moving thank to classes.py and random choices'
        
        continue_game = 1
        while continue_game:
            
            choice = random.choice(LISTE_POS)

            listed = ['left', 'top', 'bot']
            listeh = ['left', 'right', 'bot']
            listeb = ['left', 'top', 'right']
            listeg = ['right', 'top', 'bot']
            
            if choice == 'right':
                cont = main.moving('droite', listed, dk)
                if cont == 0:
                    continue_game = 0
                    print(len(LISTE_CHOICE))
                    
            if choice == 'left': 
                cont = main.moving('gauche', listeg, dk)
                if cont == 0:
                    continue_game = 0
                    print(len(LISTE_CHOICE))
                    
            if choice == 'bot':
                cont = main.moving('bas', listeb, dk)
                if cont == 0:
                    continue_game = 0
                    print(len(LISTE_CHOICE))
                    
            if choice == 'top':
                cont = main.moving('haut', listeh, dk)
                if cont == 0:
                    continue_game = 0
                    print(len(LISTE_CHOICE))

   
            window.blit(background, (0,0))
            level.display(window)
            window.blit(dk.direction, (dk.x, dk.y)) 
            pygame.display.flip()


           

if __name__ == '__main__':
    
    main = main()
    choice = main.menu()
    perso = main.generate_level(choice[0], choice[1])

    if requete0.REQUETE0 >= 100:
        main.trying(perso[0], choice[1], perso[1], perso[2])
    else:
        main.game(perso[0], choice[1], perso[1], perso[2])
