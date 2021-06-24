# coding: utf-8
class   Rangement_bloc_ID () :
    def __init__ (self,) :
        
        
        self.nombre_ID_par_bloc = 2
        
        self.resultat = []
        
    def memorisation_blocs (self,liste) :
        
        for sous_liste in liste :
            self.resultat.extend(sous_liste)
        return
    
    def get_resultat (self,) :
        
        
        
        self.resultat.sort()
        memoire = {}
        isDebut_bloc = True
        resultat = []
        nombre_en_cours = self.nombre_ID_par_bloc
        ID_courant = ""
        for ID in self.resultat :
            
            if ID in memoire :
                continue
            
            ID_courant = ID
            memoire [ID] = None
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
            resultat.append ([debut_bloc, ID,])
            
        return resultat
        
    
            
            
        
        
    
    
