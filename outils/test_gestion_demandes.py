# coding: utf-8
import time
from Gestion_demandes import Gestion_demandes

def test_gestion_demandes () :
    
    
    
    pathDico_systeme = '../data/dico_systeme_2.txt'
    G = Gestion_demandes (pathDico_systeme, time_test = 1, isSoft = False )
    
    resultat = G.execution_with_lock (G.fonction_test  )
    
    assert  resultat == 'done'

    
if __name__ == '__main__' :
    test_gestion_demandes ()
    print ('fin test_gestion_demandes')
