# -*- coding: utf-8 -*-


class utilisateur():
    
    def __init__(self,cin,nom,prenom,datenaissance,domaine,region,pays,centre_Interet,preference,login,password,email,photo):
        self.cin=cin
        self.nom=nom
        self.prenom=prenom
        self.datenaissance=datenaissance
        self. domaine=domaine
        self.region=region
        self.pays=pays
        self.centre_Interet=centre_Interet 
        self.preference=preference 
        self.login=login
        self.password=password 
        self.email=email 
       
       
    def test(self):
     return self.nom    
        
        
        
