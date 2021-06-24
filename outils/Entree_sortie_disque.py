# coding: utf-8
import json


class Entree_sortie_disque () :
    
    
    def __init__ (self,pathParametres ) :
        """
        Warning lecture ecriture par une seule tache........à faire si necessaire
        sinon faire lecture en lock, modif rapide puis ecriture
        """
        
        self.pathParametres = pathParametres
        
        
    
    def readParametres (self,) :
        #modif pour executeur simplifie
        
        f = open (self.pathParametres, "r")
        data = f.read()
        f.close()
                
        return json.loads (data)
    
    def saveParametres (self, dico ) :
        #modif pour executeur simplifie  ne fait rien
        
        data = json.dumps(dico)
        f = open(self.pathParametres, 'w')
        f.write (data)
        f.close()
        
        
        return
