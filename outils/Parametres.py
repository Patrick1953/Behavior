# coding: utf-8
import json, copy, glob
from pathlib import Path
from pathlib import Path




class Entree_sortie () :
    
    
    def __init__ (self,dicoParametres ) :
        """
        Warning ne fait plus rien car parametres dans arg
        """
        
        self.dicoParametres = dicoParametres
        
        
    
    def readParametres (self,) :
        #modif pour executeur simplifie
        """
        f = open (self.pathParametres, "r")
        data = f.read()
        f.close()
        """
        
        return self.dicoParametres
    
    def saveParametres (self, dico ) :
        #modif pour executeur simplifie  ne fait rien
        '''
        data = json.dumps(dico)
        f = open(self.pathParametres, 'w')
        f.write (data)
        f.close()
        '''
        
        return
    
    
    

class Parametres (Entree_sortie) :
    """
    lit et ecrit un sous ensemble de parametres (systemes ou evenenements)
    pathParametres  path du fichier json (string)
    listeData liste des noms qui permettent d'obtenir le sous dico (si [], la totale)
    
    save(dico) : sauve
    get_dico : donne le sous ensemble
    
    warning 
    """
    
    def __init__ (self, dicoParametres, listeData = []) :
        
        self.pathParametres = dicoParametres
        
        super().__init__ (dicoParametres)
        
        self.listeData = listeData
        
        self.dicoComplet = self.readParametres () 
        self.dico = self.calcul_dico ()
        
        
            
    def __getitem__ (self, cle):
        return  self.dico [cle]
    
    def __setitem__ (self, cle, val):
        self.dico [cle] = val
        return
    
    
        
    
    def calcul_dico (self,) :
        """
        utilise effet de bord du dictionnaire
        self.dico est inclu dans dicoComplet
        les modifications son réalisé dans dico 
        et inclu dans dico_complet par effet de bord (passage par adresse)
        
        Warning lecture ecriture par une seule tache........à faire si necessaire
        sinon faire lecture en lock, modif rapide puis ecriture
        """
        
        # descend dans l arbre pour presenter le bon niveau (on sauve l'ensemble)
        if len(self.listeData) != 0 :
            dico = self.dicoComplet [self.listeData[0]]
            for data in self.listeData [1:] :
                dico = dico [data]
                continue
        else :
            dico = self.dicoComplet
        return dico

    def save (self,):
        
        self.saveParametres (self.dicoComplet)
        return

        
   
        

        


        

        
  
                          
        
        
        
        
