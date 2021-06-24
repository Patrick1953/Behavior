# coding: utf-8
import sys

from Lanceur import Lanceur

path = "../Alimentation"
if path not in sys.path :
    sys.path.append (path)
from Alimentation import Alimentation

def Lanceur_alimentation (arg) :
    
    '''
    nom_environnement = 'test'
       
    arg = {}
    arg ['nom_environnement'] = nom_environnement
    arg ['isPurge_existing_index'] = True
    arg ['nom_fichier'] =  'evenements.txt'
    arg ['nom_tache_alimentation'] = 'test'

    -start () => execution Alimentation
    -is_alive () => True if running else False

    '''
    job = Alimentation  (arg).run
    lanceur = Lanceur (job)
    lanceur.start ()
    
    return lanceur
        
        
        
        
        
        
        
        
    
        

        
