# coding: utf-8
import shutil, json
from Kernel_BE import Kernel
import pprint as p
from PARAMETRAGES import Get_new_dico_evenements, Update_create__environnement


def test_PARAMETRAGES ():
    
    dico_position = {'test' : 1}
    dico_type = {'test' : 2}
    nom_environnement_complet = '#test'
    path_fichier = '../data/' + nom_environnement_complet + '/data_alimentation/'
    new_dico_evenements = Get_new_dico_evenements (  nom_environnement_complet,
                                                     dico_position = dico_position,
                                                     dico_type =dico_type)
    
    
    
    #p.pprint (new_dico_evenements)
    
    assert new_dico_evenements ['environnement'] ['parametres_lecture'] ['path_fichier'] ==  path_fichier
    
    assert new_dico_evenements ['creation_dictionnaire'] ==   {'ID' : {'travail' : None,
                                                                'parametres' : []},
                                                     'date_evenement' : {'travail' : 'date',
                                                                        'parametres' : []},
                                                     }
    assert new_dico_evenements ['dictionnaire'] ==  {'ID' : {'travail' : None,
                                                    'parametres' : []},
                                            'date_evenement' : {'travail' : 'date',
                                                                'parametres' : []},
                                            }
    
    assert new_dico_evenements ['pas'] ==  {}
    
        
    
    assert new_dico_evenements ['apprentissage'] == {'liste_execution' : [],
                                                     
                                                     }
    
    voulu = {'alimentation': {'execution': {'date_debut_alimentation': '2021-02-01 '
                                                           '00:00:00',
                                'dico_ajout': {},
                                'index_data': 'data_fake',
                                'nombre_erreur_max': 0,
                                'taille_globale': [0, 0]}},
                 'apprentissage': {'liste_execution': []},
                 'creation_dictionnaire': {'ID': {'parametres': [], 'travail': None},
                                           'date_evenement': {'parametres': [],
                                                              'travail': 'date'}},
                 'dictionnaire': {'ID': {'parametres': [], 'travail': None},
                                  'date_evenement': {'parametres': [], 'travail': 'date'}},
                 'environnement': {'parametres_ecriture': {'parametres_execution': {'type_lecteur': 'fichier'},
                                                           'path_sortie': '../data/data_sortie/test/'},
                                   'parametres_lecture': {'parametres_execution': {'type_lecteur': 'fichier'},
                                                          'path_fichier': '../data/#test/data_alimentation/',
                                                          'separateur': '|'}},
                 'pas': {},
                 'position': {'test': 1},
                 'type': {'test': 2}}
    
    assert new_dico_evenements == voulu
        
        
    nom_environnement = 'ephemere'
    
    resultat = Update_create__environnement (nom_environnement)
    
    nom_environnement_complet = "#" + nom_environnement
    path = '../data/'+ nom_environnement_complet + '/parametres/'
    pathFile = path + "dico_evenements_2.json"
    
    f = open (pathFile, "r")
    data = f.read ()
    f.close()
    voulu = json.loads (data)
    
    #print ('voulu')
    #p.pprint (voulu)
    #print ('\n')
    #print ('resultat')
    #p.pprint (resultat)
    
    assert resultat == voulu
    
    
    
    voulu = Get_new_dico_evenements (nom_environnement_complet)
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
    test_PARAMETRAGES ()
    print ('end_of_job')    
