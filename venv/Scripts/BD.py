import sqlite3


con = sqlite3.connect("TopGame.db")

curs = con.cursor()


curs.execute("""CREATE TABLE games  
                  (id INTEGER PRIMARY KEY, 
                  name TEXT, 
                  release_date DATE, 
                  platform TEXT,
                  FOREIGN KEY (name) REFERENCES companies(name),
                  FOREIGN KEY (platform) REFERENCES genere(name))""")

curs.execute("""CREATE TABLE compani
                  (id INTEGER PRIMARY KEY,
                  name TEXT,
                  country TEXT,
                  annua.lincome FLOAT)
                  """)

curs.execute("""CREATE TABLE genre 
                  (id INTEGER PRIMARY KEY,
                  name TEXT)
                  """)

curs.execute('INSERT INTO game (name,release_date,platform) VALUES ("GTA5", "17.09.2013", "PS4/PC")')
curs.execute('INSERT INTO game (name,release_date,platform) VALUES ("Dota2", "09.07.2013", "PC")')
curs.execute('INSERT INTO game (name,release_date,platform) VALUES ("Battlefield5", "04.09.2018", "PS4/PC")')
curs.execute('INSERT INTO game (name,release_date,platform) VALUES ("AssassinsCreed", "13.11.2007", "PC")')
curs.execute('INSERT INTO companies (name,country,anual_income) VALUES ("Valve", "USA", 4.3)')
curs.execute('INSERT INTO companies (name,country,anual_income) VALUES ("RocstarGame", "USA", 1.7)')
curs.execute('INSERT INTO companies (name,country,anual_income) VALUES ("Ubisoft", "France", 1.0)')
curs.execute('INSERT INTO companies (name,country,anual_income) VALUES ("ElectronicArts", "USA", 1.2)')
curs.execute('INSERT INTO genere (name) VALUES ("RPG")')
curs.execute('INSERT INTO genere (name) VALUES ("Shooters")')
curs.execute('INSERT INTO genere (name) VALUES ("platformers")')
curs.execute('INSERT INTO genere (name) VALUES ("Moba")')
curs.execute('INSERT INTO genere (name) VALUES ("BattleRoyale")')
curs.execute('INSERT INTO genere (name) VALUES ("MMO")')
curs.execute('INSERT INTO genere (name) VALUES ("Online")')
curs.execute('INSERT INTO genere (name) VALUES ("Strategies")')


con.commit()

curs.close()
con.close()

