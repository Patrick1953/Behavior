# coding: utf-8
import json

from Parametres import Gestion_petit_nom, Gestion_petit_nom_evenements, Gestion_petit_nom_systeme

def test_gestion_petit_nom () :
    
    def ecriture (path,nom_petit) :
        data =  json.dumps({"essai" : nom_petit})
        f = open (path +  '/'+"Evenements_" + nom_petit+ ".json", 'w')
        f.write (data)
        f.close()
        
       
    path = "./test1"
    nom_petit = "data1"
    ecriture (path, nom_petit)
    nom_petit = "data1"
    ecriture (path, nom_petit)
    nom_petit = "data2"
    ecriture (path, nom_petit)

    G = Gestion_petit_nom ("Evenements", path = path,)

    liste = G.get_all_petit_nom ()
    
    assert  liste == ['data2', 'data1']
    
    r = G.read_parametres('data1')
    assert r == {'essai' : 'data1'}
    
    r = G.read_parametres('data1')
    assert r == {'essai' : 'data1'}
    
    path = "./test2"    
    G =  Gestion_petit_nom_evenements (path) 
    
    nom_petit = "data2"
    ecriture (path, nom_petit)
    nom_petit = "data3"
    ecriture (path, nom_petit)
    nom_petit = "data4"
    ecriture (path, nom_petit)
    
    liste = G.get_all_petit_nom ()
    assert liste == ['data2', 'data4', 'data3']
    
    r = G.read_parametres('data3')
    assert r == {'essai' : 'data3'}
    r['essai'] =  'nouveau'
    G.save_parametres ( 'data3', r)
    r = G.read_parametres('data3')
    assert r == {'essai' : 'nouveau'}
    

    
    
    
if __name__ == '__main__' :
    test_gestion_petit_nom ()
    print ('fin test test_gestion_petit_nom ')    
    
    
