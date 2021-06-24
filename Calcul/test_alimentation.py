# coding: utf-8
import random, time, copy, json
from datetime import datetime
from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Alimentation_bloc import Alimentation_bloc

import sys
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)




from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


def test_alimentation ():
    
    arg = {}

    arg ['pathDico_evenements'] = '../data/dico_evenements_2.txt'
    arg ['pathDico_systeme'] = '../data/dico_systeme_2.txt'
    #  variable pour alimentation bloc

    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = 'asc'
    arg ['isReference'] = False






    arg ['isVariable'] =  True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00.000'
    arg ['variable_max'] = '2021-02-04 00:00:00.000'
    arg ['variable_sort'] = 'asc'

    arg ['isID'] = True
    arg ['ID_min'] = "couple_cadre_1"
    arg ['ID_max']  = "couple_cadre_sup_1"
    arg ['ID_sort']  = None
    arg ['isTrace'] = False

    A = Alimentation_bloc (arg)
    resultat = []
    for ligne in A.get_ligne(" ") :
        resultat.append(ligne ['ID'])
        continue
    voulu = [   'couple_cadre_sup_1',
    'couple_cadre_sup_1',
    'couple_cadre_sup_1',
    'couple_cadre_sup_1',
    'couple_cadre_sup_0',
    'couple_cadre_sup_0',
    'couple_cadre_sup_0',
    'couple_cadre_sup_0',
    'couple_cadre_sup_0',
    'couple_cadre_sup_0',
    'couple_cadre_sup_0',
    'couple_cadre_sup_0',
    'couple_cadre_sup_1',
    'couple_cadre_sup_1',
    'couple_cadre_sup_1',
    'couple_cadre_sup_1',
    'couple_cadre_sup_0',
    'couple_cadre_sup_0',
    'couple_cadre_sup_0',
    'couple_cadre_1',
    'couple_cadre_1',
    'couple_cadre_1']
    assert resultat == voulu
    
     
if __name__ == '__main__' :
    test_alimentation ()
    print ('fin test_alimentation')
