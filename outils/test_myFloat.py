# coding: utf-8
import json
from myFloat import myFloat

def test_myFloat ():
    
    def lire_file (pathFile) :
        f = open (pathFile, 'r')
        data = f.read()
        return json.loads (data)
    
    pathSysteme = '../data/test/parametres/dico_systeme_2.json'
    dico_systeme = lire_file (pathSysteme)
    D = myFloat(dico_systeme)
    
    F = "12 234.456"
    assert D.test_float (F, 'standard' )
    
    resultat = D.convert_float (F,  'standard')
    assert (resultat ==  12234.456)
    return
    
    
if __name__ == '__main__' :
    test_myFloat ()
    print ('fin test float')    
