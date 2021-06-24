# coding: utf-8
import time

from Lanceur_apprentissage import Lanceur_apprentissage

def test_lanceur_apprentissage () :
    nom_environnement = 'test'
    arg = {}
    arg ['isTrace'] = False
    path = '../data/' + nom_environnement +'/parametres/'
    arg ['nom_environnement'] = nom_environnement
    
    arg ['date_min'] = '2021-02-01 00:00:00.000000'
    arg ['date_max'] = '2021-02-09 00:00:00.000000'
    arg ['nom_tache_apprentissage'] = 'test'
    
    lanceur = Lanceur_apprentissage (arg)
      
    
    resultat = lanceur.is_alive ()
    assert resultat == True
    
    while (resultat) :
        resultat = lanceur.is_alive ()
    
    assert resultat == False
    
    
    
if __name__ == '__main__' :
    t = time.time()
    test_lanceur_apprentissage ()
    # fin test_alimentation en  0.6238605976104736
    print ('fin test_lanceur_apprentissage  en ', time.time () - t)       
    
    
