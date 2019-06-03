import mysql.connector

from config import HOST
from config import USER
from config import PASSWORD
from config import DATABASE



    
class create_base:
    


    def database(self):

        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD,
                                                 database='dkdk2')

        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""insert into move (moving)
                            VALUE("['droite', 'droite', 'bas', 'droite', 'droite']")""")
        self.connexion.commit()



    def database2(self):
    
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD,
                                                 database='dkdk2')

        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""delete from move;""")
        self.connexion.commit()


        
create_base = create_base()
create_base.database2()
create_base.database()
