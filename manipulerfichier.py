# -*- coding: utf-8 -*-
"""
Created on Thu May 13 14:22:49 2021

@author: achraf
"""

from os import listdir
from offre import offre
import offre
    
def lire_les_fichiers():
    liste_offre=[]
    for f in listdir("offre"):
        fichier=open("offre/"+str(f),"rt")
        new_lignes=[]
        for ligne in fichier :
           if ligne =="\n" :
              off=offre.liste_to_offer(new_lignes)
              liste_offre.append(off)
              new_lignes.clear()
           else:    
              mot_ligne=ligne.split(":")
              ligne=" ".join(mot_ligne[1:])
              ligne=ligne[:-1]
              new_lignes.append(ligne)
          
        fichier.close()
        
    return(liste_offre)    
        
          
         
    
    
