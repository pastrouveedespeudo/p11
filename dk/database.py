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
        
        self.cursor.execute("""CREATE DATABASE dkdk1""")
        self.connexion.commit()

class connexion_database:
    def connexion(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)
        self.cursor = self.connexion.cursor()

        self.cursor.execute("""use dkdk1""")
        self.connexion.commit()


class table:
    def creation_table_donnée(self):
        connexion_database.connexion(self)
        self.cursor.execute("""create table move(
                            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                            move TEXT,
                            PRIMARY KEY(id) )
                            ENGINE=InnoDB;
                            
                            """)
        self.connexion.commit()




class insertion_table:
    def insertion_meteo(self, para):
        connexion_database.connexion(self)
        
        sql = ("""insert into move
                        (move)
                         values(%s);""")

        values = (para)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()


    def insertion_climat(self, para):
        connexion_database.connexion(self)

        self.cursor.execute("""UPDATE move
                            SET move=%s;""", (para,))


        self.connexion.commit()


    def insertion_polution(self, ville_pollué, REGION_INDUSTRIEL_POLLUEE, date, heure_donnée, ville):
        connexion_database.connexion(self)
        
        sql = ("""UPDATE ville
                   SET ville_pollué=%s,
                   REGION_INDUSTRIEL_POLLUEE=%s
                   WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

        values = (ville_pollué, REGION_INDUSTRIEL_POLLUEE, date, heure_donnée, ville)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()


    def insertion_sociologie(self, POPULATION_ACTIVE_HABITANT, date, heure_donnée, ville):
        
        connexion_database.connexion(self)
        
        sql = ("""UPDATE ville
                   SET POPULATION_ACTIVE_HABITANT=%s
                   WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

        values = (POPULATION_ACTIVE_HABITANT, date, heure_donnée, ville)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()


    def insertion_trafic_routier(self, TRAFIQUE, HEURE,
                                 POINTE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE,
                                 date, heure_donnée, ville):
        
        connexion_database.connexion(self)
        
        sql = ("""UPDATE ville
                   SET TRAFIQUE=%s,
                   HEURE=%s,
                   POINTE=%s,
                   WEEKEND=%s,
                   BOUCHON=%s,
                   ACTIVITE_EXEPTIONNELLE=%s
                   WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

        values = (TRAFIQUE, HEURE, POINTE, WEEKEND,
                  BOUCHON, ACTIVITE_EXEPTIONNELLE,
                  date, heure_donnée, ville)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()


    def insertion_particule_plage(self, PARTICULE_PLAGE, date, heure_donnée, ville):
        
        connexion_database.connexion(self)
        
        sql = ("""UPDATE ville
                   SET nombre_particule=%s
                   WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

        values = (PARTICULE_PLAGE, date, heure_donnée, ville)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()

    def insertion_particule(self, PARTICULE, date, heure_donnée, ville):
        
        connexion_database.connexion(self)
        
        sql = ("""UPDATE ville
                   SET particule=%s
                   WHERE (date = %s AND heure_donnée = %s AND nom_ville = %s);""")

        values = (PARTICULE, date, heure_donnée, ville)

        
        self.cursor.execute(sql, values)
        self.connexion.commit()

class visualisation_table:
    
    def visualisation(self):
        connexion_database.connexion(self)

        self.cursor.execute("""SELECT * from move;
                            """)
                           
        
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste


    def visualisation_polution(self):
        connexion_database.connexion(self)
        self.cursor.execute("""select  from """)
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste
    
    def visualisation_sociologie(self):
        connexion_database.connexion(self)
        self.cursor.execute("""select  from """)
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste


    def visualisation_trafic_routier(self):
        connexion_database.connexion(self)
        self.cursor.execute("""select  from """)
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste



    def visualisation_particule_plage(self):
        connexion_database.connexion(self)
        self.cursor.execute("""select  from """)
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste



    def visualisation_particule(self):
        connexion_database.connexion(self)
        self.cursor.execute("""select  from """)
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste

class creation_conditions:

    def visualisation_without_time(self, ville):
        connexion_database.connexion(self)

        self.cursor.execute("""SELECT pression, météo, vent, climat,
                            saison, ville_pollué,
                            REGION_INDUSTRIEL_POLLUEE,
                            POPULATION_ACTIVE_HABITANT,
                            TRAFIQUE, HEURE, POINTE, WEEKEND,
                            BOUCHON, ACTIVITE_EXEPTIONNELLE
                            FROM ville
                            WHERE nom_ville = %s
                            ORDER BY particule
                            """, (ville,))
                           
        
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste

    def recuperate_id(self, ville, pression, météo, vent, climat,
                      saison, ville_pollué, REGION_INDUSTRIEL_POLLUEE,
                      POPULATION_ACTIVE_HABITANT, TRAFIQUE, HEURE,
                      POINTE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE):
        
        connexion_database.connexion(self)

        self.cursor.execute("""SELECT id
                            FROM ville
                            WHERE (nom_ville = %s AND
                            pression LIKE %s AND
                            météo LIKE %s AND
                            vent LIKE %s AND
                            climat LIKE %s AND
                            saison LIKE %s AND
                            ville_pollué LIKE %s AND
                            REGION_INDUSTRIEL_POLLUEE LIKE %s AND
                            POPULATION_ACTIVE_HABITANT LIKE %s AND
                            TRAFIQUE  LIKE %s AND
                            HEURE LIKE %s AND
                            POINTE  LIKE %s AND
                            WEEKEND LIKE %s AND
                            BOUCHON LIKE %s AND
                            ACTIVITE_EXEPTIONNELLE LIKE %s);
                            """, (ville, pression, météo, vent, climat,
                                  saison, ville_pollué,
                                  REGION_INDUSTRIEL_POLLUEE,
                                  POPULATION_ACTIVE_HABITANT,
                                  TRAFIQUE, HEURE, POINTE, WEEKEND,
                                  BOUCHON, ACTIVITE_EXEPTIONNELLE))
                           
        
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste

    def recuperate_particle(self, ville, pression, météo, vent, climat,
                          saison, ville_pollué, REGION_INDUSTRIEL_POLLUEE,
                          POPULATION_ACTIVE_HABITANT, TRAFIQUE, HEURE,
                          POINTE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE):
        
        connexion_database.connexion(self)

        self.cursor.execute("""SELECT particule
                            FROM ville
                            WHERE (nom_ville = %s AND
                            pression LIKE %s AND
                            météo LIKE %s AND
                            vent LIKE %s AND
                            climat LIKE %s AND
                            saison LIKE %s AND
                            ville_pollué LIKE %s AND
                            REGION_INDUSTRIEL_POLLUEE LIKE %s AND
                            POPULATION_ACTIVE_HABITANT LIKE %s AND
                            TRAFIQUE  LIKE %s AND
                            HEURE LIKE %s AND
                            POINTE  LIKE %s AND
                            WEEKEND LIKE %s AND
                            BOUCHON LIKE %s AND
                            ACTIVITE_EXEPTIONNELLE LIKE %s);
                            """, (ville, pression, météo, vent, climat,
                                  saison, ville_pollué,
                                  REGION_INDUSTRIEL_POLLUEE,
                                  POPULATION_ACTIVE_HABITANT,
                                  TRAFIQUE, HEURE, POINTE, WEEKEND,
                                  BOUCHON, ACTIVITE_EXEPTIONNELLE))
                           
        
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste

    def recuperate_hour(self, ville, pression, météo, vent, climat,
                          saison, ville_pollué, REGION_INDUSTRIEL_POLLUEE,
                          POPULATION_ACTIVE_HABITANT, TRAFIQUE, HEURE,
                          POINTE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE):
        
        connexion_database.connexion(self)

        self.cursor.execute("""SELECT heure_donnée
                            FROM ville
                            WHERE (nom_ville = %s AND
                            pression LIKE %s AND
                            météo LIKE %s AND
                            vent LIKE %s AND
                            climat LIKE %s AND
                            saison LIKE %s AND
                            ville_pollué LIKE %s AND
                            REGION_INDUSTRIEL_POLLUEE LIKE %s AND
                            POPULATION_ACTIVE_HABITANT LIKE %s AND
                            TRAFIQUE  LIKE %s AND
                            HEURE LIKE %s AND
                            POINTE  LIKE %s AND
                            WEEKEND LIKE %s AND
                            BOUCHON LIKE %s AND
                            ACTIVITE_EXEPTIONNELLE LIKE %s);
                            """, (ville, pression, météo, vent, climat,
                                  saison, ville_pollué,
                                  REGION_INDUSTRIEL_POLLUEE,
                                  POPULATION_ACTIVE_HABITANT,
                                  TRAFIQUE, HEURE, POINTE, WEEKEND,
                                  BOUCHON, ACTIVITE_EXEPTIONNELLE))
                           
        
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste


class mean_data:
    
    def creation_table_mean(self):

        connexion_database.connexion(self)
        self.cursor.execute("""create table paris_donnees(
                            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                            pression varchar(100),
                            vent varchar(100),
                            météo varchar(100),
                            climat varchar(100),
                            saison varchar(100),
                            ville_pollué varchar(100),
                            REGION_INDUSTRIEL_POLLUEE varchar(100),
                            POPULATION_ACTIVE_HABITANT varchar(100),
                            TRAFIQUE varchar(100),
                            HEURE varchar(100),
                            POINTE varchar(100),
                            WEEKEND varchar(100),
                            BOUCHON varchar(100),
                            ACTIVITE_EXEPTIONNELLE varchar(100),
                            PRIMARY KEY(id) )
                            ENGINE=InnoDB;
                            
                            """)
        self.connexion.commit()
                            

    def creation_table_paris_particule(self):

        connexion_database.connexion(self)
        self.cursor.execute("""create table paris_donnees_particule(
                            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                            id_condition INT UNSIGNED,
                            particule varchar(100),
                            PRIMARY KEY(id),
                            FOREIGN KEY (id_condition) REFERENCES paris_donnees(id) )
                            ENGINE=InnoDB;
                            
                            """)
        self.connexion.commit()



    def visualisation_paris_donnees(self, pression, météo, vent, climat,
                                    saison, ville_pollué, REGION_INDUSTRIEL_POLLUEE,
                                    POPULATION_ACTIVE_HABITANT, TRAFIQUE, HEURE,
                                    POINTE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE):

        
        connexion_database.connexion(self)

        self.cursor.execute("""SELECT *
                            FROM paris_donnees
                            WHERE (pression LIKE %s AND
                            météo LIKE %s AND
                            vent LIKE %s AND
                            climat LIKE %s AND
                            saison LIKE %s AND
                            ville_pollué LIKE %s AND
                            REGION_INDUSTRIEL_POLLUEE LIKE %s AND
                            POPULATION_ACTIVE_HABITANT LIKE %s AND
                            TRAFIQUE  LIKE %s AND
                            HEURE LIKE %s AND
                            POINTE  LIKE %s AND
                            WEEKEND LIKE %s AND
                            BOUCHON LIKE %s AND
                            ACTIVITE_EXEPTIONNELLE LIKE %s);
                            """, (pression, météo, vent, climat,
                                  saison, ville_pollué,
                                  REGION_INDUSTRIEL_POLLUEE,
                                  POPULATION_ACTIVE_HABITANT,
                                  TRAFIQUE, HEURE, POINTE, WEEKEND,
                                  BOUCHON, ACTIVITE_EXEPTIONNELLE))
                           
        
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste


    
    def insertion_paris_donnees(self, pression, météo, vent, climat,
                                saison, ville_pollué, REGION_INDUSTRIEL_POLLUEE,
                                POPULATION_ACTIVE_HABITANT, TRAFIQUE, HEURE,
                                POINTE, WEEKEND, BOUCHON, ACTIVITE_EXEPTIONNELLE):

        
        connexion_database.connexion(self)

        self.cursor.execute("""INSERT INTO paris_donnees
                                  pression, météo, vent, climat,
                                  saison, ville_pollué,
                                  REGION_INDUSTRIEL_POLLUEE,
                                  POPULATION_ACTIVE_HABITANT,
                                  TRAFIQUE, HEURE, POINTE, WEEKEND,
                                  BOUCHON, ACTIVITE_EXEPTIONNELLE;""",
                                  (pression, météo, vent, climat,
                                  saison, ville_pollué,
                                  REGION_INDUSTRIEL_POLLUEE,
                                  POPULATION_ACTIVE_HABITANT,
                                  TRAFIQUE, HEURE, POINTE, WEEKEND,
                                  BOUCHON, ACTIVITE_EXEPTIONNELLE))
                           
        self.connexion.commit()




class clean_data:
    
    def clean_data(self):
        connexion_database.connexion(self)
        
        self.cursor.execute("""DELETE FROM ville
                            WHERE particule IS NULL;""")


        self.connexion.commit()
        print('données nulles effacées')


    
class suppression_table:
    def suppression(self):
        connexion_database.connexion(self)
        
        self.cursor.execute("""drop table paris_donnees;
                            """)
        self.connexion.commit()


class creation_condition:

    def creation_table_condition_paris(self):
        self.cursor.execute("""create table ville()""")


    def creation_table_condition_paris(self):
        self.cursor.execute("""create table ville()""")


    def creation_table_condition_paris(self):
        self.cursor.execute("""create table ville()""")

    def modif(self):
        connexion_database.connexion(self)
        self.cursor.execute("""insert into move (move)
                            VALUES ('JBJBJBJB')""")
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
