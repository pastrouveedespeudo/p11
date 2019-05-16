from classes import *

import dklabyrinthe as script
import classes as script1



                    
from database import *

class TestClass(object):

    def test_writting(self):
        parametre = 'test.py'
        parametre1 = 'test'
        sortie = ["a = 'test'"]
        
        assert script.writting(parametre,parametre1) == sortie



    def test_trait_list(self):
        parametre = [(1, "['droite', 'droite', 'bas', 'droite', 'droite']")]
        sortie = ['droite', 'droite', 'bas', 'droite', 'droite']
        
        assert script.trait_list(parametre) == sortie


    def test_fichier(self):
        sortie = 'requete2.py'
    
        assert script.file() == sortie

    def test_choice_level(self):
        'We verify the min move from database'
        out = 6

        assert script1.help_method.traitement_dattodowne(self) == out


    def test_s_point_1(self):
        'We verify the min move from database\
        if dk moving on s from the bottom'
        
        self.y = 1
        parametre = self.y
        out = (6, 's')

        assert script1.help_method.s_point_1(self, parametre) == out

    def test_s_point_1(self):
        'We verify the min move from database if\
        dk moving on s from the right'
        
        self.x = 1
        parametre = self.x
        out = (6, 's')

        assert script1.help_method.s_point_1(self, parametre) == out

    def test_s_point_2(self):
        'We verify the min move from database\
        if dk moving on s from the left'
        
        self.x = 1
        parametre = self.x
        out = (6, 's')

        assert script1.help_method.s_point_1(self, parametre) == out



    def test_s_point_2(self):
        'We verify the min move from database if\
        dk moving on s from the top'
        
        self.y = 1
        parametre = self.y
        out = (6, 's')

        assert script1.help_method.s_point_1(self, parametre) == out


    def test_right(self):
        'we check that if dk is not on arrival he can move to right'

      
        self.case_x = 30
        self.case_y = 30
        self.x = 0
        self.y = 0
        
        out = None

        assert script1.Perso.torigth(self) == out


    def test_bot(self):
        'we check that if dk is not on arrival he can move to bottom'
        
      
        self.case_x = 30
        self.case_y = 30
        self.x = 0
        self.y = 0
        
        out = None

        assert script1.Perso.todown(self) == out


    def test_left(self):
        'we check that if dk is not on arrival he can move to left'
        
      
        self.case_x = 0
        self.case_y = 30
        self.x = 0
        self.y = 0
        
        out = None

        assert script1.Perso.toleft(self) == out

    def test_top(self):
        'we check that if dk is not on arrival he can move to top'
        
        self.case_x = 0
        self.case_y = -30
        self.x = 0
        self.y = 0
        
        out = None

        assert script1.Perso.totop(self) == out

























