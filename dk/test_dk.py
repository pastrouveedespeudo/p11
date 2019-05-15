import dklabyrinthe as script
import classes as script1



class TestClass(object):
    
    def test_trait_list(self):
        parametre = [(1, "['droite', 'droite', 'bas', 'droite', 'droite']")]

        sortie = ['droite', 'droite', 'bas', 'droite', 'droite']
        assert script.trait_list(parametre) == sortie


    def test_fichier(self):

        sortie = 'requete2.py'
        assert script.fichier() == sortie



















































