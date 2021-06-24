# coding: utf-8
import time

from Gestion_echanges import Gestion_echanges


def fonction_test (dico, data) :
    time.sleep (1)
    return "done", dico


def test_gestion_echanges () :
        
    
    arg = {}
    arg ['pathFile'] = '../data/test/echanges.json'
    
    dico_lock = {}
    dico_lock ['isSoft'] = False
    dico_lock ['time_out'] = 10
    arg ['dico_lock'] = dico_lock
    
    G = Gestion_echanges (arg)
       
    resultat, echanges = G.execution_with_lock (fonction_test  )
    
    assert  resultat == 'done'
    assert echanges == {}
    
if __name__ == '__main__' :
    test_gestion_echanges ()
    print ('fin test_gestion_echanges')
