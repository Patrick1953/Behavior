# coding: utf-8
import sys

from Lanceur import Lanceur

path = "../Apprentissage"
if path not in sys.path :
    sys.path.append (path)
from Apprentissage import Apprentissage

def Lanceur_apprentissage (arg) :
    
    '''
    arg = {}
    arg ['isTrace'] = False
    path = '../data/' + nom_environnement +'/parametres/'
    arg ['nom_environnement'] = nom_environnement
    
    arg ['date_min'] = '2021-02-01 00:00:00.000000'
    arg ['date_max'] = '2021-02-09 00:00:00.000000'
    arg ['nom_tache_apprentissage'] = 'test'

    -start () => execution Alimentation
    -is_alive () => True if running else False

    '''
    job = Apprentissage  (arg).run
    lanceur = Lanceur (job)
    lanceur.start ()
    
    return lanceur
        
        
        
        
        
        
        
        
    
        

        
