
# -*- coding: utf-8 -*-

import sqlite3
con=sqlite3.connect("projet.db")
cur=con.cursor()
req='''create table user
(
 cin INT PRIMARY KEY,
 nom TEXT,
 prenom TEXT,
 date_Naissance DATE,
 domaine TEXT,
 region TEXT,
 pays TEXT,
 centre_Interet TEXT,
 preference TEXT,
 login TEXT,
 password TEXT,
 email TEXT
 )
'''

req1='''create table offre
(id_offre INTEGER   PRIMARY KEY AUTOINCREMENT ,
 titre TEXT,
 description TEXT,
 niveau TEXT,
 domaine TEXT,
 region TEXT,
 pays TEXT,
 societe TEXT,
 type_offre TEXT,
 experience TEXT,
 date_debut DATE NULL,
 duree TEXT NULL,
 nb_poste INT,
 salaire FLOAT
  )
 '''
cur.execute(req)
cur.execute(req1)
con.commit()

