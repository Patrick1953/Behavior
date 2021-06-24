# coding: utf-8
import sys

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from validationPath import validationPath

class Sortie_fichier () :
    
    def __init__(self, arg) :
        
        
        parametres_sortie = arg ['parametres']
        self.pathFile = parametres_sortie ['path_sortie'] + arg ['nom_data']
        validationPath (self.pathFile)
        
        
    def init_ecriture (self,) :
        self.f = open (self.pathFile, "w")
        
    def ecrire (self, data) :
        self.f.write (data + '\n')
        
    def close (self,) :
        self.f.close()
    
