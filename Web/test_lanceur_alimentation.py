# coding: utf-8
import time

from Lanceur_alimentation import Lanceur_alimentation

def test_lanceur_alimentation () :
    nom_environnement = 'test'
    arg = {}
    arg ['nom_environnement'] = nom_environnement
    arg ['isPurge_existing_index'] = True
    arg ['nom_fichier'] =  'evenements.txt'
    arg ['nom_tache_alimentation'] = 'test'
    
    lanceur = Lanceur_alimentation (arg)
    
    
    
    
    resultat = lanceur.is_alive ()
    assert resultat == True
    
    while (resultat) :
        resultat = lanceur.is_alive ()
    
    assert resultat == False
    
    
    
if __name__ == '__main__' :
    t = time.time()
    test_lanceur_alimentation ()
    # fin test_alimentation en  0.6238605976104736
    print ('fin test_lanceur_alimentation en ', time.time () - t)       
    
    
