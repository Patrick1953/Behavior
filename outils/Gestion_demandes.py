# coding: utf-8
import os
from os import path
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



class Gestion_demandes () :
    def __init__ (self, pathDico_systeme, time_test = 2, isSoft = False ) :
        
        """
        gestion des demandes par createur  (avec lock)
        il y a plusieurs createur possibles 
        createur = source de données
                
        {'createur' : {'demande_1' : {'parametres' :  parametres,
                                        'etat' : etat soit (open, running, close)} }
        
        """
        
                
        self.isSoft = isSoft
        
        self.parametres_lock = Parametres (pathDico_systeme, listeData = ['parametres_demandes'])
        self.path = self.parametres_lock ['lock'] ['path']
        self.timeout = self.parametres_lock ['lock'] ['timeout']
        self.name_file = self.parametres_lock ['demandes'] ['name_file']
        self.time_test = time_test

        self.pathFile = self.path + '/' + self.name_file
        self.pathFile_lock = self.pathFile + '.lock'
        
        if not path.exists(self.pathFile) :
            print (self.pathFile)
            creation_file_demandes (self.pathFile)
            
        return
    
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
    
    def execution_with_lock (self, fonction ):
        """
        lit les demandes 
        execute la fonction (demandes) => demandes, resultat 
        en mode lock
        """
        if self.isSoft :
            from filelock import SoftFileLock as FileLock 
        else :
            from filelock import FileLock as FileLock
        
            
        lock = FileLock(self.pathFile_lock, timeout=self.timeout)
        try:
            with lock.acquire():
                demandes = self.lire ()
                resultat, demandes = fonction (demandes)
                self.ecrire (demandes)
        except :
            if self.isSoft :
                os.remove(self.pathFile_lock)
            else:
                lock.release()
            raise
        
        
        return resultat
    
    def fonction_test (self, dico) :
        time.sleep (self.time_test)
        return "done", dico
    
    def creation_new_nom_demande (self, dico) :
        if len(dico) == 0 :
            return str(1)
        liste = [nom_demande for nom_demande in dico.key()]
        liste_numero = [int(nom_demande.split('_')[1]) for nom_demande in liste.keys()]
        numero = max(liste_numero) + 1
        
        
        
