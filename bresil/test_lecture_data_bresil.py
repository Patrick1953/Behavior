# coding: utf-8
import time
import pandas as pd
from Lecture_data_bresil import Lecture_data_bresil

def test_lecture_data_bresil ():
    
    L = Lecture_data_bresil ()
       
    dico_resultat = L.dico_customers ()
    
    assert L.nombre_erreur == 2765
    
    assert len(dico_resultat) == 99163
    
    
    
    
        
    
    
if __name__ == '__main__' :
    t = time.time()
    test_lecture_data_bresil ()
    print ('fin test_lecture_data_bresil en ', time.time () - t)    
