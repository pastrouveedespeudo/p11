import mysql.connector

from config import HOST
from config import USER
from config import PASSWORD
from config import DATABASE

class TestClass:
    
    def test_mysql_connection(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)

        self.cursor = self.connexion.cursor()


    def test_creation_database(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                         user=USER,
                                         password=PASSWORD)

        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""CREATE DATABASE test_dk""")
        self.connexion.commit()

    def test_connexion(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)
        self.cursor = self.connexion.cursor()

        self.cursor.execute("""use test_dk""")
        self.connexion.commit()




    def test_creation_table(self):
        
        TestClass.test_connexion(self)

        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""CREATE table test(col text);""")
        self.connexion.commit()


    def test_insertion_database(self):
        TestClass.test_connexion(self)
        
        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""insert into test(col) value('test');""")
        self.connexion.commit()

    def test_visualisation(self):
        TestClass.test_connexion(self)
        
        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""select * from test;""")
    
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste

    def test_visualisation2(self):
        
        out = [('test',)]
        assert TestClass.test_visualisation(self) == out


    def test_drop(self):
        TestClass.test_connexion(self)
        
        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""drop database test_dk;""")
        self.connexion.commit()
























