# coding: utf-8
import random ,  copy

from  Rangement_bloc_ID import  Rangement_bloc_ID

def test_rangement_bloc_ID () :
    liste = []
    for i in range (0, 10, 2) :
        liste.append([i, i+1])
        
    voulu = copy.copy (liste)    
    random.shuffle (liste)
       
    R = Rangement_bloc_ID ()
    
    
    R.memorisation_blocs (liste)
        
    resultat = R.get_resultat ()
    
    assert resultat == voulu
    
    liste = []
    for i in range (0, 10, 2) :
        liste.append([i, i+1])
        
    liste.extend ([[11, 12], [13,13]])
        
    voulu = copy.copy (liste)
    
    R = Rangement_bloc_ID ()
       
    R.memorisation_blocs (liste)
        
    resultat = R.get_resultat ()
    
    assert resultat == voulu
    
        
    
        
        
    
    
if __name__ == '__main__' :
    test_rangement_bloc_ID ()
    print ('fin test_rangement_bloc_ID ()')    
    
