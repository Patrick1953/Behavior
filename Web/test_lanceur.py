# coding: utf-8
import time, sys

from Lanceur import Lanceur

def travail_ok():
    return

def raises():
    time.sleep(1)
    return sys.exit(1)
    

def test_lanceur () :
    jobs = []
    L = Lanceur (travail_ok) 
    L.start ()
    time.sleep(1)
    resultat = L.is_alive ()
    assert resultat == False
    
    resultat = L.get_exitcode ()
    
    assert resultat == 0
    
    L = Lanceur (raises)
    L.start ()
    resultat = L.is_alive ()
    voulu = True
    assert resultat == voulu
    
    time.sleep(2)
    
    resultat = L.is_alive ()
    assert resultat == False
    
    
    resultat = L.get_exitcode ()
    assert resultat == 1
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
if __name__ == '__main__':
    test_lanceur ()
    print ('test_lanceur fini')
    
    
    
    
