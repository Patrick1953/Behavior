# coding: utf-8
import os
from Gestion_commandes import Gestion_commandes

"""appels :
    
    insertion_commande  (commande) => dico, cle
    
    get_liste_commandes (type_commande) => dico, resultat resultat = dico des commandes en attente
    
    reserve_commande ( numero_commande) => dico, resultat  si tout va bien sinon string (no exist ou etat)
    
    get_commande (numero_commande) => dico, commande ou 'no exist' (pas de filtrage)
    
    del_commande_execute ( numero_commande) => dico, commande ou no exist ou etat quand not done
    
    commande_fini (self, numero_commande) => dico, 'OK' ou 'no_exist'"""


def test_Gestion_commandes () :
    
    arg = {}
    arg ['entete'] = "commande_"
    
    # data pour gestion fichier_lock 
    try:
        os.remove('../data/test/echanges.json')
    except:
        print ('pas detruit')
        
    arg ['pathFile'] = '../data/test/echanges.json'
    
    dico_lock = {}
    dico_lock ['isSoft'] = False
    dico_lock ['time_out'] = 10
    arg ['dico_lock'] = dico_lock
    
    G = Gestion_commandes (arg)
    dico, resultat = G.get_liste_commandes ('demande')
    assert resultat == {} and dico == {}
    cle = G.get_new_numero ({})
    assert cle == 'commande_0'
    cle = G.get_new_numero ({'commande_0' : None})
    assert cle == 'commande_1'
    
    
    commande = {'nb_max_worker' : 2, 'parametres' : {}}
    
    dico, resultat = G.insertion_commande  (commande)
    assert resultat == 'commande_0'
    assert dico ['commande_0'] == commande
    dico, resultat = G.insertion_commande  (commande)
    assert resultat == 'commande_1'
    voulu = {'commande_0': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'demande', 'nb_courant_worker': 0},
             'commande_1': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'demande', 'nb_courant_worker': 0}}
    
    assert dico == voulu
    
    dico, resultat = G.reserve_commande ( 'commande_1')
    
    voulu = {'commande_0': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'demande', 'nb_courant_worker': 0},
             'commande_1': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'running', 'nb_courant_worker': 1}}
    
    assert dico == voulu
    
    voulu = {'nb_max_worker': 2, 'parametres': {}, 'etat': 'running', 'nb_courant_worker': 1}
    assert resultat == voulu
    dico, resultat = G.reserve_commande ( 'commande_1')
    voulu = {'nb_max_worker': 2, 'parametres': {}, 'etat': 'running', 'nb_courant_worker': 2}
    
    assert resultat  == voulu
    
    dico, resultat = G.reserve_commande ( 'commande_1')
    assert resultat == 'KO'
    
    dico, resultat = G.get_liste_commandes ('running')
    
    voulu = {'commande_1': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'running', 'nb_courant_worker': 2}}
    assert resultat  == voulu
    
    dico, resultat = G.commande_fini ('commande_1')
    assert resultat == 'OK'
    
    voulu = {'commande_0': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'demande', 'nb_courant_worker': 0},
             'commande_1': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'done', 'nb_courant_worker': 2}}
    
    assert dico == voulu
    
    dico, resultat = G.get_commande ('commande_1')
    
    voulu = {'nb_max_worker': 2, 'parametres': {}, 'etat': 'done', 'nb_courant_worker': 2}
    assert resultat  == voulu
    
    dico, resultat = G.get_liste_commandes ('done')
    
    voulu = {'commande_1': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'done', 'nb_courant_worker': 2}}
    assert resultat  == voulu
    
    dico, resultat = G.get_liste_commandes ('reservable')
    voulu = {'commande_0': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'demande', 'nb_courant_worker': 0}}
    assert resultat  == voulu
    dico, resultat = G.reserve_commande ( 'commande_0')
    dico, resultat = G.get_liste_commandes ('reservable')
    
    voulu = {'commande_0': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'running', 'nb_courant_worker': 1}}
    assert resultat  == voulu
    dico, resultat = G.del_commande_execute ( 'commande_1')
    voulu = {'commande_0': {'nb_max_worker': 2, 'parametres': {}, 'etat': 'running', 'nb_courant_worker': 1}}
    assert dico  == voulu
    
if __name__ == '__main__' :
    test_Gestion_commandes ()
    print ('fin test_gestion_commandes')
    
  
    
    
