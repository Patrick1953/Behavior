# coding: utf-8
import os
import json , time

from Lock import Lock
from validationPath import validationPath
from lire_dico_json import lire_dico_json




class Entree_sortie_lock (Lock) :
    
    def __init__ (self, arg) :
        
        """
        dans pathfile le chemin vers le fichier à proteger
        
        """
         
        
        self.pathFile = arg ['pathFile']
        validationPath (self.pathFile)
        
        if not os.path.isfile(self.pathFile) :
            self._ecrire_lock ({})
            
        
        pathFile_lock = self.pathFile + '.lock'
        validationPath (pathFile_lock)
            
        
        # lit les parametres du lock
        path_general = '../data/general/parametres/'
        pathLock = path_general + 'dico_lock.json'
        dico_lock = lire_dico_json (pathLock)
                
        
        time_out = dico_lock ['time_out']
        super ().__init__ (pathFile_lock, time_out)
        
        
        
    def execution_with_lock (self, fonction, data = None ):
        """
        lit les demandes execute le travail == fonction (parametre)
        execute la fonction (demandes) => demandes, resultat 
        en mode lock
        """
                 
        
        try:
            self.acquire ()
            dico = self._lire_lock () # lire sous lock
            dico, resultat = fonction (dico, data)
            self._ecrire_lock (dico) # ecrire sous lock
            self.unlock_lire ()
        except :
            raise
             
        return dico, resultat
    
     
    
    def _lire_lock (self, ) :
        f = open(self.pathFile, "r")
        data =f.read ()
        f.close()
        dico = json.loads  (data)
        return dico
    
    def _ecrire_lock (self, dico) :
        data = json.dumps (dico)
        f = open(self.pathFile, "w")
        f.write (data)
        f.close()
        return dico
    
    def lire_with_lock (self,) :
                   
        try:
            self.acquire ()
            dico = self._lire_lock () # lire sous lock
            return dico
        except :
            raise
        
             
        return
    
    
    def ecrire_with_unlock (self, dico) :
        self._ecrire_lock ( dico)
        return self.unlock_lire ()
        
        
    def unlock_lire (self,) :
        try:
            self.release ()
        except:
            pass
        return
    

    
        
        
        
        
    
    
    
    
