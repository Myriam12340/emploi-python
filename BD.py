
# -*- coding: utf-8 -*-


import sqlite3 
con=sqlite3.connect("projet.db")
cur=con.cursor()
import sys
sys.path.append('interface/')
from offre import offre


#utlisateur
def ajouter_user(cin,nom,prenom,datenaissance,domaine,region,pays,centre_Interet,preference,login,password,email):
    req="INSERT INTO user Values(?,?,?,?,?,?,?,?,?,?,?,?)"
    emp=[(cin,nom,prenom,datenaissance,domaine,region,pays,centre_Interet,preference,login,password,email)]
    cur.executemany(req,emp)
    con.commit()
 

    
def connect_user(login,mdp):
    req='''SELECT * FROM user WHERE  login=? and  password=? '''
    cur.execute(req,(login,mdp))
    resultat=cur.fetchall()
    if(len(resultat)==0):
        return False
    else :
        return resultat
    



#offre
def ajouter_offre(titre,description,niveau_etude,domaine,region,pays,entreprise,typeoffre,experience,date_debut,dureé,nombre_de_poste,remunerationproposee):
    req="INSERT INTO offre (titre,description,niveau,domaine,region,pays,societe,type_offre,experience,date_debut,duree,nb_poste,salaire) Values(?,?,?,?,?,?,?,?,?,?,?,?,?)"
    offre=[(titre,description,niveau_etude,domaine,region,pays,entreprise,typeoffre,experience,date_debut,dureé,nombre_de_poste,remunerationproposee)]
    cur.executemany(req,offre)
    con.commit()




def offre_bd_all():
    req='''SELECT * FROM offre '''
    cur.execute(req)
    resultat=cur.fetchall()
    if(len(resultat)==0):
        return False
    else :
        list_offre=[]
        for i in  resultat:
         offrebd=offre(i[0],i[1],i[2],i[3],i[4],i[12],i[5],i[6],i[7],i[9],i[13],i[10],i[11],i[8])
         list_offre.append(offrebd)

    return list_offre 




def offre_bd(region,pays,domaine):
    req='''SELECT * FROM offre WHERE  region=? and  pays=? and domaine=? '''
    cur.execute(req,(region,pays,domaine))
    resultat=cur.fetchall()
    if(len(resultat)==0):
        return False
    else :
        list_offre=[]
        for i in  resultat:
         offrebd=offre(i[0],i[1],i[2],i[3],i[4],i[12],i[5],i[6],i[7],i[9],i[13],i[10],i[11],i[8])
         list_offre.append(offrebd)

    return list_offre  


def offre_bd_region(region):
    req='''SELECT * FROM offre WHERE  region=? '''
    cur.execute(req,(region,))
    resultat=cur.fetchall()
    if(len(resultat)==0):
        return []
    else :
        list_offre=[]
        for i in  resultat:
         offrebd=offre(i[0],i[1],i[2],i[3],i[4],i[12],i[5],i[6],i[7],i[9],i[13],i[10],i[11],i[8])
         list_offre.append(offrebd)

    return list_offre             
            

def offre_bd_type(typeoff):
    req='''SELECT * FROM offre WHERE  type_offre=? '''
    cur.execute(req,(typeoff,))
    resultat=cur.fetchall()
    if(len(resultat)==0):
        return []
    else :
        list_offre=[]
        for i in  resultat:
         offrebd=offre(i[0],i[1],i[2],i[3],i[4],i[12],i[5],i[6],i[7],i[9],i[13],i[10],i[11],i[8])
         list_offre.append(offrebd)

    return list_offre             
            
    
    
def offre_bd_pays(pays):
    req='''SELECT * FROM offre WHERE  pays=? '''
    cur.execute(req,(pays,))
    resultat=cur.fetchall()
    if(len(resultat)==0):
        return []
    else :
        list_offre=[]
        for i in  resultat:
         offrebd=offre(i[0],i[1],i[2],i[3],i[4],i[12],i[5],i[6],i[7],i[9],i[13],i[10],i[11],i[8])
         list_offre.append(offrebd)

    return list_offre    
    
def offre_bd_domaine(domaine):
    req='''SELECT * FROM offre WHERE  domaine=? '''
    cur.execute(req,(domaine,))
    resultat=cur.fetchall()
    if(len(resultat)==0):
        return []
    else :
        list_offre=[]
        for i in  resultat:
         offrebd=offre(i[0],i[1],i[2],i[3],i[4],i[12],i[5],i[6],i[7],i[9],i[13],i[10],i[11],i[8])
         list_offre.append(offrebd)

    return list_offre       
    
#print(len(offre_bd_all()))
                                          
#print(offre_bd_region("nabeul")[0].entreprise)

#ajouter_offre("offre de stage","stage en bi","bac+3","info","tunise","tunise","vermeg","stage","ing",'12/02/2021',"3mois",2,1234)

  

#ajouter_user(12345678, "achraf", "achraf",'14/01/1997', "test", "tunise", "tunis", "test","test", "achraf", "achraf", "mariem.ksouri@sesame.com.tn")


#req3=''' SELECT* FROM  user '''

#cur.execute(req3)

#print(cur.fetchall())


#print(connect_user("ellachraf","1234"))

 
