# coding: utf-8
import json

from myString import myString

def test_myString ():
    def lire_file (pathFile) :
        f = open (pathFile, 'r')
        data = f.read()
        return json.loads (data)
    
    pathSysteme = '../data/test/parametres/dico_systeme_2.json'
    dico_systeme = lire_file (pathSysteme)
    
    D = myString (dico_systeme)
    
    S = "chaine"
    assert D.test_string(S, 'standard' )
    
    resultat = D.convert_string (S,  'standard')
    assert (resultat ==  S)
    return
    
    
if __name__ == '__main__' :
    test_myString ()
    print ('fin test date')    
