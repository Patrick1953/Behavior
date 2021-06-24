# coding: utf-8
import os, sys, json
from datetime import datetime

path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from Interface_parametres import Interface_parametres_engine

  
    
    
    
class  Interface_executions ( Interface_parametres_engine ) :
    
    def __init__ (self,) :
        
        self.dico_saisie = {}
        super ().__init__ ()
        
        
       
    
        
        
    
    def get_dico_evenements (self, nom_environnement ) :
        return self.call_dico_evenements ( nom_environnement)    
        
            

    
    def get_liste_environnements (self,) :
        
        liste = self.call_liste_environnements ()
        liste.sort()
        
        return liste
    
    def put_dico_evenements (self,nom_environnement, dico_evenements) :
        
        raise ValueError
            
        self.send_dico_evenements (nom_environnement, old_dico_evenements)
        
        return
    
    def get_liste_fichiers (self,nom_environnement, end = 'json') :
        
        dico_evenements = self.get_dico_evenements (nom_environnement )
        #print(dico_evenements ['environnement'] ['parametres_lecture'] ['path_fichier'])
        pathFichiers = dico_evenements ['environnement'] ['parametres_lecture'] ['path_fichier']
        
        liste_fichiers = [] 
        for file in os.listdir (pathFichiers):
            if file.endswith(end):
                liste_fichiers.append (file)
        
        return liste_fichiers
    
        
        
    
    
    
        
        
        
    
    def is_good_date (self, format_string) :
          
        date_now = datetime.now()
        date_time_str = 'erreur de lecture du format'
        date_str =  'erreur de passage en format standard'
              
        try:
            date_time_str = date_now.strftime(format_string)
            date = datetime.strptime(date_time_str, format_string)
            date_str = date.strftime(format_string)
        except:
            return False
        if date_time_str != date_str :
            return False
        return True
    
    

            
            
 
    
        
        
        
        
