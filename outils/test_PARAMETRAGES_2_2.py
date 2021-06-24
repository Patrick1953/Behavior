# coding: utf-8
import shutil, json
from Kernel_BE import Kernel
import pprint as p
from PARAMETRAGES_2_2 import Get_new_dico_evenements, Update_create__environnement


def test_PARAMETRAGES_2_2 ():
    
        
    nom_environnement = 'ephemere'
    
    resultat = Update_create__environnement (nom_environnement)
    nom_environnement_complet = "#" + nom_environnement
    
    path = '../data/'+ nom_environnement_complet + '/parametres/'
    
    pathFile = path + "dico_evenements_2.json"
    
    f = open (pathFile, "r")
    data = f.read ()
    f.close()
    voulu = json.loads (data)
    
    assert resultat == voulu
    
    voulu = Get_new_dico_evenements ()
    """
    print ('voulu')
    p.pprint (voulu)
    print ('\n')
    print ('resultat')
    p.pprint (resultat)
    """
       
    assert resultat == voulu
    
    # detruire la directory 
    path = '../data/'+ nom_environnement_complet
    shutil.rmtree(path)
     
    
    return


    
    
if __name__ == '__main__' :
    test_PARAMETRAGES_2_2 ()
    print ('end_of_job')    
