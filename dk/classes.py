"""Classes for the game dk"""

import pygame
from pygame.locals import * 
from constantes import *
from database import *



class Niveau:
    """Classe who create level"""
    
    def __init__(self, file):
        self.file = file
        self.structure = 0
        
    def choice_level(self):
        'here user can choice his level'
        
        continue_game = 1
        continuer_home = 1

        while continuer_home:
            
            pygame.time.Clock().tick(30)
            
            for event in pygame.event.get():
            
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continuer_home = 0
                    continue_game = 0
                    continuer = 0
                    choice = 0
                        
                elif event.type == KEYDOWN:				
              
                    if event.key == K_F1:
                        continuer_home = 0
                        choice = 'n1'		
                        return 'n1'
                    
                    elif event.key == K_F2:
                        continuer_home = 0
                        choice = 'n2'
                        return 'n2'



    def generate(self):
        'from n1 we generating wall and free way'
        
        with open(self.file, "r") as file:
            structure_niveau = []
            
            for line in file:
                line_niveau = []
      
                for sprite in line:
                    if sprite != '\n':
                        line_niveau.append(sprite)

                structure_niveau.append(line_niveau)
            self.structure = structure_niveau

    
    def display(self, window):
        'we displaying wall, window ...'
        
        mur = pygame.image.load(image_wall).convert()
        depart = pygame.image.load(image_departure).convert()
        arrivee = pygame.image.load(image_arrival).convert_alpha()
        
        num_line = 0
        for line in self.structure:
            num_case = 0
            
            for sprite in line:
                x = num_case * size_sprite
                y = num_line * size_sprite
                
                if sprite == 'm' or sprite == 'M':		   
                    window.blit(mur, (x,y))
                elif sprite == 'd':		   
                    window.blit(depart, (x,y))
                elif sprite == 's':		   
                    window.blit(arrivee, (x,y))
                num_case += 1
            num_line += 1
                    
                    
LISTE = []

class help_method:
    'methods called by program'
    
    def traitement_dattodowne(self):
        'we called data from database here it\'s the minimum of moves'
        
        visuel = visualisation_table.visualisation(self)
        visuel = str(visuel)
        visuel = visuel.split()

        return len(visuel)

    def s_point_1(self, case):
        'the case is the arrival ? for right and\
        down moves, if yes we return minimum of moves'
        
        self.case = case
        
        number_minimal_movement = help_method.traitement_dattodowne(self)
        self.case += 1
        return number_minimal_movement, 's'   


    def s_point_2(self, case):
        'the case is the arrival ? for left and\
        top moves, if yes we return minimum of moves'
        
        self.case = case
        
        self.case -= 1
        number_minimal_movement = help_method.traitement_dattodowne(self)
        return number_minimal_movement, 's'
    

          
class Perso:
    """Class who create perso"""
    
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
    

    def torigth(self):
        'here we can move to the right if it\s not a wall, if it\'s arrival we\
        return s_point function'
        
        if self.case_x < (nombre_sprite_cote - 1):
            if self.niveau.structure[self.case_y][self.case_x+1] == 's':

                checkpoint = help_method.s_point_1(self, self.case_x)
                return checkpoint

            if self.niveau.structure[self.case_y][self.case_x+1] != 'M':
                self.case_x += 1
                LISTE.append((self.x, self.y))
                self.x = self.case_x * size_sprite


    def toleft(self):
        'here we can move to the left if it\s not a wall, if it\'s arrival we\
        return s_point function'
        
        if self.case_x > 0:
             if self.niveau.structure[self.case_y][self.case_x-1] == 's':

                 checkpoint = help_method.s_point_2(self, self.case_x)
                 return checkpoint

             if self.niveau.structure[self.case_y][self.case_x-1] != 'M':
                self.case_x -= 1
                LISTE.append((self.x, self.y))
                self.x = self.case_x * size_sprite
                
            
    def todown(self):
        'here we can move to the bottom if it\s not a wall, if it\'s arrival we\
        return s_point function'
        
        if self.case_y < (nombre_sprite_cote - 1):
            if self.niveau.structure[self.case_y + 1][self.case_x] == 's':

                checkpoint = help_method.s_point_1(self, self.case_y)
                return checkpoint

            if self.niveau.structure[self.case_y+1][self.case_x] != 'M':
                self.case_y += 1
                LISTE.append((self.x, self.y))
                self.y = self.case_y * size_sprite


    def totop(self):
        'here we can move to the top if it\s not a wall, if it\'s arrival we\
        return s_point function'
        
        if self.case_y > 0:
            if self.niveau.structure[self.case_y-1][self.case_x] == 's':

                checkpoint = help_method.s_point_2(self, self.case_y)
                return checkpoint
                    
            if self.niveau.structure[self.case_y-1][self.case_x] != 'M':
                self.case_y -= 1
                LISTE.append((self.x, self.y))
                self.y = self.case_y * size_sprite


    def deplacement(self, direction):
        """Methode who deplace the perso"""
        
        LISTE = []

        filee = []

        b = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

        MOVE = []

        if int(self.x)/30 == 0 and  int(self.y)/30 == 0:
            pass

        if direction == 'droite':
            sauve = Perso.torigth(self)
            return sauve
        
        elif direction == 'gauche':
            sauve = Perso.toleft(self)
            return sauve
        
        elif direction == 'haut':      
            sauve = Perso.totop(self)
            return sauve
        
        elif direction == 'bas':
            sauve = Perso.todown(self)
            return sauve
        








		
