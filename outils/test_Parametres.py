# coding: utf-8
from Parametres import Parametres
import json


test = {'essai1' : {'essai2' : 'OK'}}
#modif
"""
path = "./test.json"
data = json.dumps (test)
f = open(path, 'w')
f.write (data)
f.close ()
"""


def test_open () :
    
    dico = Parametres (test, [])
    
    assert (dico.dico == test)
    return 

def test_get_dico () :
    path = "./test.json"
    dico = Parametres (test, ['essai1',])
    assert dico.dico == {'essai2' : 'OK'}

def test_save() :
    
    dico= Parametres (test, ['essai1',])
    dico ['essai2']  = 'OK'
    dico.save()
    
    E = Parametres (test, ['essai1',])
    result = E ['essai2']
    assert (result == "OK")
    new_result = "KO"
    E ['essai2'] = new_result
    E.save()
    #E = Parametres (test, ['essai1'])
    result = E ['essai2']
    assert result == 'KO'
    #E['essai2'] = {'essai3' : "OK"}
    E.save ()
    #E = Parametres (test, ['essai1', 'essai2'])
    E ['essai3'] = 'KO'
    E.save()
    #E = Parametres (path, ['essai1', 'essai2'])
    result = E ['essai3']
    assert result == 'KO'
    return


if __name__ == '__main__' :
    test_open ()
    test_get_dico ()
    test_save()
    print ('test Parametres OK')
    

    
    

    
    
