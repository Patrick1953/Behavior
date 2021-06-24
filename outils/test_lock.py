# coding: utf-8
import time
from Lock import Lock

def test_lock () :
    pathLock = 'test_lock.lock'
    time_out = 30
    L = Lock(pathLock,time_out)
    
    L.acquire ()
    
    resultat = L.is_locked()
    
    assert resultat == True
    
    L.release ()
    resultat = L.is_locked()
    
    assert resultat == False
    
    L.acquire ()
    
    t = time.time ()
    
    try:
        L.acquire ()
    except:
        L.release ()
    
    delaie = time.time () - t
    assert delaie >= 30
    

        
    
    
if __name__ == '__main__' :
    test_lock ()
    print ('fin test_lock ')       
    
    
    
    
