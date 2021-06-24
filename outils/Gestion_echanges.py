# coding: utf-8
import os
import json , time

from filelock import Timeout
from validationPath import validationPath
from Parametres import Parametres


def creation_file_demandes (pathFile) :
    validationPath  (pathFile) 
    dico = {}
    data = json.dumps (dico)
    f = open (pathFile, 'w')
    f.write(data)
    f.close()
    return


class Entree_sortie_lock () :
    
    def __init__ (self, arg) :
        
        
        
        self.pathFile = arg ['pathFile']
        
        
        if not self.exists() :
            self.creation_file_demandes ()
        
    def lire (self,):
        f = open(self.pathFile, "r")
        data =f.read ()
        f.close()
        return json.loads  (data)
    
    def ecrire (self, demandes) :
        data = json.dumps (demandes)
        f = open(self.pathFile, "w")
        f.write (data)
        f.close()
        return
    
    def creation_file_demandes (self,) :
        validationPath  (self.pathFile) 
        dico = {}
        data = json.dumps (dico)
        f = open (self.pathFile, 'w')
        f.write(data)
        f.close()
        return
    
    def exists (self,)  :
        return os.path.exists(self.pathFile)
        
        
        
        
        
        



class Gestion_echanges (Entree_sortie_lock) :
    def __init__ (self, arg, ) :
        
        """
        gestion des demandes par createur  (avec lock)
        il y a plusieurs createur possibles 
        createur = source de données
                
        {'createur' : {'demande_1' : {'parametres' :  parametres,
                                      'etat' : etat soit (open, running, close)} }
        
        """
        
        super().__init__ (arg)
        
                
        
        dico_lock =  arg['dico_lock']
        self.isSoft = dico_lock ['isSoft']
        self.time_out = dico_lock ['time_out']
        
        self.pathFile = arg ['pathFile']
        self.pathFile_lock = self.pathFile + '.lock'
        
        if not self.exists() :
            self.creation_file_demandes ()
            
        return
    
    
    
    def execution_with_lock (self, fonction, data = None ):
        """
        lit les demandes execute le travail == fonction (parametre)
        execute la fonction (demandes) => demandes, resultat 
        en mode lock
        """
        if self.isSoft :
            from filelock import SoftFileLock as FileLock 
        else :
            from filelock import FileLock as FileLock
        
            
        lock = FileLock(self.pathFile_lock, timeout=self.time_out)
        try:
            with lock.acquire():
                echanges = self.lire ()
                dico, resultat = fonction (echanges, data)
                self.ecrire (echanges)
        except Timeout:
            if self.isSoft :
                os.remove(self.pathFile_lock)
            else:
                lock.release()
            dico = None, "time out" 
        return dico, resultat
    
    
    
    
    
    
    
        
        
        
