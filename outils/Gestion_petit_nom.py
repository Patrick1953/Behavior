# coding: utf-8
import json, copy, glob
from pathlib import Path

from Entree_sortie_disque import Entree_sortie_disque

class Gestion_petit_nom (Entree_sortie_disque) :
    
    def __init__ (self,nomParametres, path = "", listeData = []) :
        
        self.listeData = listeData
        self.path = path
        self.nomParametres = nomParametres # Evenements ou Systeme
           
               
        return
    
    
    
    def get_all_petit_nom (self,) :
        
        liste_file = glob.glob(self.path + '/*.json')
        
        resultat = []
        for nom in liste_file:
            monPath = Path (nom)
            ll = monPath.parts
            
            l = ll[len(ll)-1].split ("_")
            if l[0] == self.nomParametres :
                resultat.append (l[1] [:-5] )
            continue
        return resultat
    
    def read_parametres (self, petit_nom ) :
        path_file = self.path + '/'+ self.nomParametres + '_' + petit_nom + '.json'
        super ().__init__ (path_file)
        return self.readParametres () 
    
    def save_parametres (self, petit_nom, dico_parametres) :
        path_file = self.path + '/'+ self.nomParametres + '_' + petit_nom + '.json'
        super ().__init__ (path_file)
        self.saveParametres (dico_parametres)
        return

    
   
        
        
        

class Gestion_petit_nom_evenements (Gestion_petit_nom) :
    
    def __init__ (self,  path  , listeData = []) :
        super().__init__ ("Evenements" , path = path , listeData = listeData )

        
class Gestion_petit_nom_systeme (Gestion_petit_nom) :
    
    def __init__ (self,  path  , listeData = []) :
        super().__init__ ("Systeme" , path = path , listeData = listeData )
