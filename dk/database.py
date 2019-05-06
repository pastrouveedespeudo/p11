import mysql.connector

from config import HOST
from config import USER
from config import PASSWORD
from config import DATABASE

class create_base:
    def database(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)

        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""CREATE DATABASE dkdk2""")
        self.connexion.commit()

class connexion_database:
    def connexion(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)
        self.cursor = self.connexion.cursor()

        self.cursor.execute("""use dkdk2""")
        self.connexion.commit()


class table:
    def creation_table_donnée(self):
        connexion_database.connexion(self)
        self.cursor.execute("""create table move(
                            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                            moving TEXT,
                            PRIMARY KEY(id) )
                            ENGINE=InnoDB;
                            
                            """)
        self.connexion.commit()




class insertion_table:


    def insertion_move(self, para):
        connexion_database.connexion(self)
        print(para)
        self.cursor.execute("""UPDATE move
                            SET moving=%s;""", (para,))


        self.connexion.commit()



class visualisation_table:
    
    def visualisation(self):
        connexion_database.connexion(self)

        self.cursor.execute("""SELECT * from move;
                            """)
                           
        
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste




class clean_data:
    
    def clean_data(self):
        connexion_database.connexion(self)
        
        self.cursor.execute("""DELETE FROM ville
                            WHERE particule IS NULL;""")


        self.connexion.commit()
        print('données nulles effacées')


        self.connexion.commit()
    
#if __name__ == "__main__":


    #creation_condition = creation_condition()
    #creation_condition.modif()

    #partie database creation    
    #create_base = create_base()
    #create_base.database()


    #clean_data = clean_data()
    #clean_data.clean_data()

    #suppression_table = suppression_table()
    #suppression_table.suppression()

    #creation de la table
    #table = table()
    #table.creation_table_donnée()

    #mean_data = mean_data()
    #mean_data.creation_table_mean()
    #mean_data.creation_table_paris_particule()

    #creation_condition = creation_condition()
    #creation_condition.modif()
