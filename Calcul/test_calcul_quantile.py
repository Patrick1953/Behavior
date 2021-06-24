# coding: utf-8
import random, time, copy, json
from datetime import datetime

from Calcul_quantile import Calcul_quantile, Description_travail_quantile

import sys
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Kernel_BE import Kernel
from Entree_sortie_disque import Entree_sortie_disque

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


def  test_calcul_quantile () :
    arg = {}
    arg ['isTrace'] = False
    dicoEvenements = Entree_sortie_disque ('../data/test/parametres/dico_evenements_2.json').readParametres()
    dicoSysteme = Entree_sortie_disque ('../data/test/parametres/dico_systeme_2.json').readParametres()
    arg ['pathDico_evenements'] = dicoEvenements
    arg ['pathDico_systeme'] = dicoSysteme
    
    #  variable pour alimentation bloc dans calcul quantile

    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = 'asc'
    arg ['isReference'] = False

    arg ['isVariable'] =  True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00.000000'
    arg ['variable_max'] = '2021-03-30 00:00:00.000000' #gaffe en 2030
    arg ['variable_sort'] = 'asc' # pour l'instant inused

    arg ['isID'] = False
    arg ['ID_min'] = "couple_cadre_0"
    arg ['ID_max']  = "couple_cadre_1"
    arg ['ID_sort']  = None
    
    C = Calcul_quantile (arg)
    
    resultat = C.creation_quantile ()
    
    #P(resultat)
    
    voulu = {   'prix': [   {'nom': 'quartile', 'separateurs': [29.08, 54.4, 93.97]},
                {   'nom': 'decile',
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
    
    assert voulu == resultat
    
    
    D = Description_travail_quantile ()
    
    resultat = D.get_liste_travail_quantile ()
    voulu = ['quartile', 'quintile', 'decile', 'vingtile', 'cinquantile', 'centile', 'manuel' ]
    assert voulu == resultat
    
    return

    
    
if __name__ == '__main__' :
    t = time.time()
    test_calcul_quantile ()
    print ('duree =', time.time() - t)
    print ('fin test calcul_quantique')      
