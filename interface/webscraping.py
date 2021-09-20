# importing the libraries
from bs4 import BeautifulSoup
import requests

import sys
sys.path.append('../')

import BD 


def conversion_description(ch1): 
    l=list(ch1)
    chaine=""
    for i in range(len(l)-1) :
        if l[i]==">" :
            j=i+1
            while l[j]!="<":
                chaine2=chaine+str(l[j])
                chaine=chaine2  
                j+=1
                
             
            chaine=chaine+' '
            i=j
        if l[i]=="<":
            k=i
            while l[k]!=">":
                k+=1
            i=k    
                
            
    return chaine    


def sous(titre,i):
    if i<len(titre):
     ch=str(titre[i]) 
     d=ch.index('>')+1
     f=ch.index('<',2,len(ch)-1)
    
     return ch[d:f]
url="https://www.talents.tn/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")




#print(soup.find_all("div",attrs={"class": "listings-container compact-list-layout margin-top-35"}))
href=[]
for i in soup.find_all("h3",attrs={"class": "job-listing-title"}):
    a=i.find_all("a")
    
    for a1 in a :
        href.append(a1['href'])
        


for urllink in href :
 

      html_content1 = requests.get(urllink).text
        
      # Parse the html content
      souplink = BeautifulSoup(html_content1, "lxml")
      titreB=souplink.find_all("h2")
      liste=souplink.find_all("h5")
      desB=souplink.find_all("div",attrs={"class": "user-html"})
      socB=souplink.find_all("div",attrs={"class":"job-company-logo"})
      domainB=souplink.find_all("nav",attrs={"id":"breadcrumbs"})[0].find_all("ul")[0].find_all("li")[1].find_all("a")
      emp=sous(liste,0).split(",")[0].lower()
      titre=sous(titreB,0)
      salaire=sous(liste,2)
      des=conversion_description(str(desB[0]))
      societe=socB[0].find_all("img")[0]["alt"]
      domaine=sous(domainB,0)
      if "stage" not in titre :
          typeoffre="emploi"
          
          
      else : 
           typeoffre="stage"     
      pays="tunis"  
      

      BD.ajouter_offre(titre[:-24], des," ", domaine,emp, pays, societe, typeoffre, "", "", " ", 1, salaire)
  
    
#print(domaine)
#print(societe)      
 
#print(titre)
 
#print(emp)
#print(salaire)
#print(des)

     