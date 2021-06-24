# coding: utf-8
import json, sys, time
from datetime import datetime

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Apprentissage import Apprentissage, Mise_a_jour_apprentissage, Apprentissage_calcul

path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock


def test_apprentissage () :
    nom_environnement = '#test'
    pathFile_evenements = 'dico_evenements_2.json'
    
    
    arg = {}
    arg ['isTrace'] = False
    path = '../data/' + nom_environnement +'/parametres/'
    arg ['nom_environnement'] = nom_environnement
    
    arg ['date_min'] = '2021-02-01 00:00:00.000000'
    arg ['date_max'] = '2021-02-09 00:00:00.000000'
    arg ['nom_tache_apprentissage'] = nom_environnement
    
    
    
    A = Apprentissage_calcul (arg)
    
    resultat = A.run()
    
    nom_environnement = nom_environnement
    arg = {}
    arg ['nom_environnement'] = nom_environnement
    
    M = Mise_a_jour_apprentissage (arg)
    M.run (resultat)
    
    arg_entree_sortie_lock = {} 
    path = '../data/' + nom_environnement +'/parametres/'
    arg_entree_sortie_lock['pathFile'] = path + pathFile_evenements
    Entree_sortie_evenements = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_evenements = Entree_sortie_evenements.lire_with_lock ()
    Entree_sortie_evenements.unlock_lire ()
    
    voulu = {   'prix': [   {'nom': 'quartile', 'separateurs': [29.08, 54.4, 93.97]},
                { 'nom': 'decile',
                    'separateurs': [   10.93,
                                       24.99,
                                       29.49,
                                       48.86,
                                       54.4,
                                       72.778,
                                       88.05799999999996,
                                       97.29200000000004,
                                       112.26]},
                {'nom': 'manuel1', 'separateurs': [10.0, 20.0, 100.0]}],
    'prix_panier': [   {   'nom': 'quartile',
                           'separateurs': [145.95, 222.25, 377.12]}]}
    
    resultat = dico_evenements ['dictionnaire']
    for nom_variable, valeur_quantile in voulu.items() :
        assert valeur_quantile == resultat [nom_variable]
        continue
        
    
    pathFile_evenements = 'dico_evenements_2.json'
    
    
    arg = {}
    arg ['isTrace'] = False
    path = '../data/' + nom_environnement +'/parametres/'
    arg ['nom_environnement'] = nom_environnement
    
    arg ['date_min'] = '2021-02-01 00:00:00.000000'
    arg ['date_max'] = '2021-02-09 00:00:00.000000'
    arg ['nom_tache_apprentissage'] = nom_environnement
    
    
    
    A = Apprentissage (arg)
    
    resultat = A.run()
    
    arg_entree_sortie_lock = {} 
    path = '../data/' + nom_environnement +'/parametres/'
    arg_entree_sortie_lock['pathFile'] = path + pathFile_evenements
    Entree_sortie_evenements = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_evenements = Entree_sortie_evenements.lire_with_lock ()
    Entree_sortie_evenements.unlock_lire ()
    
    voulu = {   'prix': [   {'nom': 'quartile', 'separateurs': [29.08, 54.4, 93.97]},
                { 'nom': 'decile',
                    'separateurs': [   10.93,
                                       24.99,
                                       29.49,
                                       48.86,
                                       54.4,
                                       72.778,
                                       88.05799999999996,
                                       97.29200000000004,
                                       112.26]},
                {'nom': 'manuel1', 'separateurs': [10.0, 20.0, 100.0]}],
    'prix_panier': [   {   'nom': 'quartile',
                           'separateurs': [145.95, 222.25, 377.12]}]}
    
    resultat = dico_evenements ['dictionnaire']
    for nom_variable, valeur_quantile in voulu.items() :
        assert valeur_quantile == resultat [nom_variable]
        continue
        
    #P(dico_evenements ['apprentissage'])
        
    resultat = dico_evenements ['apprentissage'] ['liste_execution'] [0]
    del resultat ['date_creation']
    voulu =   {  
               'date_max': '2021-02-09 00:00:00.000000',
               'date_min': '2021-02-01 00:00:00.000000',
               'nom_tache_apprentissage': '#test'}
    
        
        
    
    
    return

if __name__ == '__main__' :
    t = time.time()
    test_apprentissage ()
    print ('fin test_apprentissage en ', time.time () - t)  
    
    
    
