# coding: utf-8
import json, time
import sys

from datetime import datetime

from pprint import PrettyPrinter
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)

from Parametres import Entree_sortie_disque
from Execution_quantile import Execution_quantile

def test_execution_quantile():
    arg = {}
    
    dicoEvenements = Entree_sortie_disque ('../data/dico_evenements_2.txt').readParametres()
    dicoSysteme = Entree_sortie_disque ('../data/dico_systeme_2.txt').readParametres()
    arg ['pathDico_evenements'] = dicoEvenements
    arg ['pathDico_systeme'] = dicoSysteme
    
    
    
    arg ['variable_min'] = '2021-02-01 00:00:00'
    arg ['variable_max'] = '2021-03-30 00:00:00' #gaffe en 2030
      
       
    new_dicoEvenement = Execution_quantile (arg).run()
    
    resultat = new_dicoEvenement ['dictionnaire']
    
    
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

if __name__ == '__main__' :
    t = time.time ()
    test_execution_quantile()
    print ('fin test date en ', time.time() - t)
