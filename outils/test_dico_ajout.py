# coding: utf-8
from Dico_ajout import Dico_ajout

def test_dico_ajout ():
    
    dico_test = {}
    dico_ajout = Dico_ajout (dico_test) 
    ajout_test = {'test' : 'test'}
    dico_ajout.put_ajout (ajout_test)
    resultat = dico_ajout ['dico_ajout']
    voulu = {'ajout_0000000000': {'test': 'test'}}
    assert voulu == resultat
    ajout_test = {'test' : 'test'}
    dico_ajout.put_ajout (ajout_test)
    resultat = dico_ajout ['dico_ajout']
    voulu = {'ajout_0000000000': {'test': 'test'}, 'ajout_0000000001': {'test': 'test'}}
    assert voulu == resultat
    dico_ajout ['test'] = 'test'
    resultat = dico_ajout ['test']
    voulu = 'test'
    assert voulu == resultat
    
    
if __name__ == '__main__' :
    test_dico_ajout ()
    print ('fin test Dico_ajout')
    
    
