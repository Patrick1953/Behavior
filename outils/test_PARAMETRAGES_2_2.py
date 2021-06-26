# coding: utf-8
import shutil, json
from Kernel_BE import Kernel
import pprint as p

from PARAMETRAGES import Get_new_dico_evenements, Update_create__environnement

def test_PARAMETRAGES ():
    
    v_type = {'test' : None}
    position = {'test' : None}
    new_dico_evenement = Get_new_dico_evenements (v_type = v_type,
                                                 position = position)
    
    assert v_type == new_dico_evenement ['type']
    assert position == new_dico_evenement ['position']
    
      
    
        
    nom_environnement = 'ephemere'
    
    resultat = Update_create__environnement (nom_environnement,
                                            v_type = v_type,
                                            position = position)
    
    
    nom_environnement_complet = "#" + nom_environnement
    
    path = '../data/'+ nom_environnement_complet + '/parametres/'
    
    pathFile = path + "dico_evenements_2.json"
    
    f = open (pathFile, "r")
    data = f.read ()
    f.close()
    voulu = json.loads (data)
    
    assert new_dico_evenement == voulu
    
      
    # detruire la directory 
    path = '../data/'+ nom_environnement_complet
    shutil.rmtree(path)
     
    
    return


    
    
if __name__ == '__main__' :
    test_PARAMETRAGES ()
    print ('end_of_job')    
