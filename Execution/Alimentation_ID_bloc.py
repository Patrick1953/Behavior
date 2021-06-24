# coding: utf-8
# coding: utf-8
import sys
path = "../Calcul"
if path not in sys.path : 
    sys.path.append (path)
    
from Alimentation_bloc import Alimentation_bloc

class Alimentation_ID_bloc (Alimentation_bloc ) :
    
    def __init__ (self, arg ) :
        
        super().__init__ (arg)
        
        self.nombre_ID_par_bloc = self.dico_systeme ['calcul'] ['nombre_ID_par_bloc']
        if self.nombre_ID_par_bloc <= 1 :
            self.nombre_ID_par_bloc = 2
            
        
        
    def lecture_ID (self,) :
        
        memoire = {}
        liste_ID = []
        for ligne in self.get_ligne(" ") :
            
            ID = ligne ['ID']
            if ID in memoire :
                continue
            liste_ID.append (ID)
            memoire [ID] = None
        
        del memoire
        liste_ID.sort()
        return liste_ID
            
                
        
    
    def get_liste_bornes_ID (self,) :
        
        
        liste_ID = self.lecture_ID ()
        
        isDebut_bloc = True
        resultat = []
        nombre_en_cours = self.nombre_ID_par_bloc
        ID_courant = ""
        for ID in liste_ID :
            ID_courant = ID
            nombre_en_cours -= 1
            
            if isDebut_bloc :
                debut_bloc = ID
                isDebut_bloc = False
                continue
            if nombre_en_cours <= 0 :
                # on recommence avec parametres equivallent du debut 
                resultat.append ([debut_bloc, ID])
                isDebut_bloc = True
                nombre_en_cours = self.nombre_ID_par_bloc
                continue
            
            continue
        
        if nombre_en_cours != self.nombre_ID_par_bloc :
            resultat.append ([debut_bloc, ID, ])
        
        
        nombre_ID = len(liste_ID)
        del liste_ID
        return resultat, nombre_ID
        


            
            
            
            
           
