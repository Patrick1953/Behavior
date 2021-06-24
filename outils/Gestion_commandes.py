# coding: utf-8
import os, json

from validationPath import validationPath
from Entree_sortie_lock import Entree_sortie_lock



class Gestion_messages (Entree_sortie_lock):
    """
    format message dict
    {
     arg : dico pour tache,
     tache : string,
     }
    
    les messages sont dans une file []
     
    """
    
    def __init__ (self,nom) :
               
        # calcul le nom du fichier qui est partagé entre tous les environnements de travail
        # du type 'xxxx|yyyy' ou yyyy designe l'environnement de travail pour une commande
        
        
        pathFile = '../data/general/echanges/' + nom + '.json'
        self.pathFile = pathFile
        arg = {}
        arg ['pathFile'] = pathFile
        
        if not os.path.exists (pathFile) :
            validationPath (pathFile)
            liste_commande = []
            data = json.dumps (liste_commande)
            with open (pathFile, 'w') as f :
                f.write (data)
                
        
        super().__init__ (arg)
        
        
        
        
        
        
    def get_message (self,) :
        
        liste_message =  self.lire_with_lock ()
        try:
            message = liste_message.pop(0)
            self.ecrire_with_unlock (liste_message)
            return message
        except:
            self.unlock_lire ()
            return None
        
    
    def put_message (self,message) :
        
        liste_message =  self.lire_with_lock ()
        liste_message.append (message)
        self.ecrire_with_unlock (liste_message)
        return
    
    def clean_message (self,) :
        if os.path.exists (self.pathFile) :
            liste_commande = []
            data = json.dumps (liste_commande)
            with open (self.pathFile, 'w') as f :
                f.write (data)
        
        
    
    
    
class Gestion_commandes (Gestion_messages) :
    """
    format commandes dict
    {
     
     arg : dico pour tache,
     tache : string,
     }
     
    """
    
    def __init__ (self,) :
        
        super ().__init__ ( 'commandes')
        
class Gestion_reponses (Gestion_messages) :
    """
    format reponses dict
    {
     arg : dico pour tache,
     tache : string,
     }
     
    """
    
    def __init__ (self,) :
        
        super ().__init__ ( 'reponses')
        
        
class Gestion_erreurs (Gestion_messages) :
    """
    format reponses dict
    {
     arg : dico pour tache,
     tache : string,
     }
     
    """
    
    def __init__ (self,) :
        
        super ().__init__ ( 'erreurs')
        

        
        
        
        
        
    
    
    

        
        
        
