# coding: utf-8
import sys

from Lanceur import Lanceur

path = "../Execution"
if path not in sys.path :
    sys.path.append (path)
from Execution import Execution

def Lanceur_execution (arg) :
    
    '''
    nom_environnement = '#test'
       
    arg = {}
    arg ['date_min'] = '2021-02-01 00:00:00.000000'
    arg ['date_max'] = '2021-02-09 00:00:00.000000'
    arg ['pas'] = 'semaine'
    arg ['nom_environnement'] = nom_environnement
    arg ['nom_tache_execution'] = nom_environnement

    arg ['workers'] = 6
    arg ['local_scheduler'] = True
    

    -start () => execution Alimentation
    -is_alive () => True if running else False

    '''
    job = Execution  (arg).run
    lanceur = Lanceur (job)
    lanceur.start ()
    
    return lanceur
        
        
        
        
        
        
        
        
    
        

        
