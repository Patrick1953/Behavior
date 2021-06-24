# coding: utf-8
import time

from Lanceur_execution import Lanceur_execution

def test_lanceur_execution () :
    nom_environnement = '#test'
    arg = {}
    arg ['date_min'] = '2021-02-01 00:00:00.000000'
    arg ['date_max'] = '2021-02-09 00:00:00.000000'
    arg ['pas'] = 'semaine'
    arg ['nom_environnement'] = nom_environnement
    arg ['nom_tache_execution'] = nom_environnement

    arg ['workers'] = 6
    arg ['local_scheduler'] = True
    
    lanceur = Lanceur_execution (arg)
      
    
    resultat = lanceur.is_alive ()
    assert resultat == True
    
    while (resultat) :
        resultat = lanceur.is_alive ()
    
    assert resultat == False
    
    
    
if __name__ == '__main__' :
    t = time.time()
    test_lanceur_execution ()
    # fin test_alimentation en  0.6238605976104736
    print ('fin test_lanceur_execution  en ', time.time () - t)       
    
    
