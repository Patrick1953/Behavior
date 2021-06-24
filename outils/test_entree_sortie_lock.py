# coding: utf-8
import os, time, json 

from Entree_sortie_lock import Entree_sortie_lock

def fonction_test (dico, data) :
    time.sleep (1)
    assert data == "OK"
    return  dico, 'done'


def test_Entree_sortie_lock  () :
    
    nom_environnement = "test"
    pathFile = 'echanges/echanges.json'
    path = '../data/'+ nom_environnement + '/parametres/'
    pathName = 'test.txt'   
    pathFile = path + pathName
    if os.path.exists(pathFile) :
        os.remove (pathFile)
    
    pathFile_lock = pathFile + '.lock'
    if os.path.exists(pathFile_lock) :
        os.remove (pathFile_lock)
        
    f = open (pathFile, 'w')
    dico = {}
    data = json.dumps (dico)
    f.write(data)
    f.close()
    
        
    arg = {}
    arg ['pathFile'] = pathFile
    
      
    
    G = Entree_sortie_lock (arg)
      
    dico, resultat = G.execution_with_lock (fonction_test, data = "OK" )
    assert dico == {}
    assert resultat == 'done'
    
    
    dico = G.lire_with_lock()
    assert dico == {}
    assert resultat == 'done'
    
    dico ['test'] = 'OK'
    G.ecrire_with_unlock (dico)
    
    
    dico = G.lire_with_lock()
    G.unlock_lire ()
    assert dico == {'test' : 'OK'}
    # on nettoie
    if os.path.exists(pathFile) :
        os.remove (pathFile)
    
     
    
    
        
    
    
    
    
if __name__ == '__main__' :
    test_Entree_sortie_lock ()
    print ('fin test_Entree_sortie_lock')
