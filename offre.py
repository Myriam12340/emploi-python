# -*- coding: utf-8 -*-
"""
Created on Thu May 13 17:37:36 2021

@author: achraf
"""

class offre():
    def __init__(self,idoffre,titre,description,niveao_etude,domaine,nombre_de_poste,region,pays,entreprise,experience,remunerationproposee,date_debut,dureé,typeoffre):
        self.idoffre=idoffre
        self.titre=titre
        self.description=description
        self.niveao_etude=niveao_etude
        self.domaine=domaine
        self.nombre_de_poste=nombre_de_poste
        self.region=region
        self.pays=pays
        self.entreprise=entreprise
        self.experience=experience
        self.remunerationproposee=remunerationproposee
        self.date_debut=date_debut
        self.dureé=dureé
        self.typeoffre=typeoffre
        
        
    def offre_pays(self,pays):
       if self.pays==pays :
           return True
       return False

    def offre_region(self,region):
       if self.region==region :
           return True
       return False  
   
    def offre_domaine(self,domaine):
      if self.domaine==domaine :
          return True
      return False
  
    def offre_stage(self):
       if self.typeoffre=="stage":
           return True
       return False
   
    def offre_emploi(self):
       if self.typeoffre=="emploi":
           return True
       return False
          
   
def liste_offre_stage(liste):
   liste_stage=[]
   for stage in liste :
       if stage.offre_stage() :
           liste_stage.append(stage)
   return(liste_stage)       
       
def liste_to_offer(liste):
   return  offre(None,liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],liste[6],liste[7],liste[8],liste[9],liste[10],liste[11],liste[12])       
        
       
     