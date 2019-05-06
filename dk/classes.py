"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *
from database import *





class Niveau:
    """Classe permettant de créer un niveau"""
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
        
    def choice_level(self):
        
        continuer_jeu = 1
        continuer_accueil = 1

        while continuer_accueil:
            
            pygame.time.Clock().tick(30)
            
            for event in pygame.event.get():
            
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continuer_accueil = 0
                    continuer_jeu = 0
                    continuer = 0
                    choix = 0
                        
                elif event.type == KEYDOWN:				
              
                    if event.key == K_F1:
                        continuer_accueil = 0
                        choix = 'n1'		
                        return 'n1'
                    
                    elif event.key == K_F2:
                        continuer_accueil = 0
                        choix = 'n2'
                        return 'n2'



    def generer(self):

        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            
            for ligne in fichier:
                ligne_niveau = []
      
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)

                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau

    
    def afficher(self, fenetre):

        mur = pygame.image.load(image_mur).convert()
        depart = pygame.image.load(image_depart).convert()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()
        
        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            
            for sprite in ligne:
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                
                if sprite == 'm' or sprite == 'M':		   
                    fenetre.blit(mur, (x,y))
                elif sprite == 'd':		   
                    fenetre.blit(depart, (x,y))
                elif sprite == 's':		   
                    fenetre.blit(arrivee, (x,y))
                num_case += 1
            num_ligne += 1
                    
                    
LISTE = []
                    
class Perso:
    """Classe permettant de créer un personnage"""
    def __init__(self, droite, gauche, haut, bas, niveau):
        
        self.droite = pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
   
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
       
        self.direction = self.droite
   
        self.niveau = niveau
    


    def adroite(self):
        mokouaille = ''
        
        if self.case_x < (nombre_sprite_cote - 1):
            
       
            if self.niveau.structure[self.case_y][self.case_x+1] == '0' and\
               self.niveau.structure[self.case_y][self.case_x+2] == 'M' and\
               self.niveau.structure[self.case_y-1][self.case_x+1] == 'M' and\
               self.niveau.structure[self.case_y+1][self.case_x+1] == 'M':

                
                mokouaille = True

            if self.niveau.structure[self.case_y][self.case_x+1] == 's':
                
                a = visualisation_table.visualisation(self)
                a = str(a)
                a = a.split()
         
                self.case_x += 1
                
                return len(a),'s'


            if self.niveau.structure[self.case_y][self.case_x+1] != 'm'\
               and self.niveau.structure[self.case_y][self.case_x+1] != 'M' and\
               mokouaille != True:
                if mokouaille == True:
                    pass
                self.case_x += 1

                LISTE.append((self.x, self.y))
        
                self.x = self.case_x * taille_sprite

         
                
    def agauche(self):
         
        if self.case_x > 0:

             if self.niveau.structure[self.case_y][self.case_x-1] == 's':

                 a = visualisation_table.visualisation(self)

                 self.case_x -= 1
  
                 a = str(a)
                 a = a.split()
                 return len(a),'s'

             if self.niveau.structure[self.case_y][self.case_x-1] != '0' and\
               self.niveau.structure[self.case_y][self.case_x-2] != 'M' and\
               self.niveau.structure[self.case_y-1][self.case_x-1] != 'M' and\
               self.niveau.structure[self.case_y+1][self.case_x-1] != 'M':
                self.case_x -= 1
                
             if self.niveau.structure[self.case_y][self.case_x-1] != 'm'\
                and self.niveau.structure[self.case_y][self.case_x-1] != 'M':
                self.case_x -= 1
                LISTE.append((self.x, self.y))
                self.x = self.case_x * taille_sprite
                    

    def ahaut(self):

        if self.case_y > 0:
            if self.niveau.structure[self.case_y-1][self.case_x] == 's':

                a = visualisation_table.visualisation(self)

                self.case_y -= 1
  

                a = str(a)
                a = a.split()
                return len(a), 's'
                    
            if self.niveau.structure[self.case_y-1][self.case_x] != '0' and\
               self.niveau.structure[self.case_y-2][self.case_x] != 'M' and\
               self.niveau.structure[self.case_y-1][self.case_x-1] != 'M' and\
               self.niveau.structure[self.case_y-1][self.case_x+1] != 'M':
                self.case_y -= 1
                
            if self.niveau.structure[self.case_y-1][self.case_x] != 'm'\
               and self.niveau.structure[self.case_y-1][self.case_x] != 'M':
                self.case_y -= 1
                LISTE.append((self.x, self.y))
                self.y = self.case_y * taille_sprite
 



    def abas(self):
        
        mokouaille = ''

        if self.case_y < (nombre_sprite_cote - 1):

            try:
                if self.niveau.structure[self.case_y + 1][self.case_x] == 's':

                    a = visualisation_table.visualisation(self)
    
                    self.case_y += 1
 

                    a = str(a)
                    a = a.split()
                    return len(a), 's'
                    
                    
                if self.niveau.structure[self.case_y + 1][self.case_x] == '0' and\
                   self.niveau.structure[self.case_y + 2][self.case_x] == 'M' and\
                   self.niveau.structure[self.case_y + 1][self.case_x + 1] == 'M' and\
                   self.niveau.structure[self.case_y + 1][self.case_x - 1] == 'M':
 
                    mokouaille = True




                if self.niveau.structure[self.case_y+1][self.case_x] != 'm'\
                   and self.niveau.structure[self.case_y+1][self.case_x] != 'M' and\
                   mokouaille != True:
                    if mokouaille == True:
                        pass
                    self.case_y += 1
                    LISTE.append((self.x, self.y))
                    self.y = self.case_y * taille_sprite
                    
            except:
                pass






    def deplacer(self, direction):
        """Methode permettant de déplacer le personnage"""
        LISTE = []

        filee = []

        b = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

        MOVE = []

        if int(self.x)/30 == 0 and  int(self.y)/30 == 0:
            pass

        if direction == 'droite':
            sauve = Perso.adroite(self)
            return sauve
        
        elif direction == 'gauche':
            sauve = Perso.agauche(self)
            return sauve
        
        elif direction == 'haut':      
            sauve = Perso.ahaut(self)
            return sauve
        
        elif direction == 'bas':
            sauve = Perso.abas(self)
            return sauve
        








		
