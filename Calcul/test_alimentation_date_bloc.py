# coding: utf-8
import time, json, os, json, sys
from datetime import datetime


from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
    
from Entree_sortie_lock import Entree_sortie_lock

from Alimentation_date_bloc import Alimentation_date_bloc

def test_alimentation_date_bloc () :
    
    arg = {}
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
    arg ['ID_min'] = "couple_cadre_0"
    arg ['ID_max']  = "couple_cadre_1"
    arg ['ID_sort']  = None
    

    arg['isTrace'] = False
    
    # on recupere le dico_systeme et dico_evenements
    
    nom_environnement = 'test'
    
    pathFile_evenements = '/dico_evenements_2.json'
    pathFile_systeme = '/dico_systeme_2.json'

    arg_entree_sortie_lock = {} 
    arg_entree_sortie_lock ['nom_environnement'] = nom_environnement
    arg_entree_sortie_lock['pathFile'] = pathFile_evenements
    Entree_sortie_evenements = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_evenements, etat = Entree_sortie_evenements.lire()
    arg ['pathDico_evenements'] = dico_evenements
    #P (dico_evenements)

    arg_entree_sortie_lock ['pathFile'] = pathFile_systeme
    Entree_sortie_systeme = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_systeme, etat = Entree_sortie_systeme.lire()
    arg ['pathDico_systeme'] = dico_systeme
    
    A = Alimentation_date_bloc(arg)
    
    resultat = A.get_liste_date_bloc ()
    
    voulu = [   ['2021-02-01 00:00:00', '2021-02-02 00:00:00'],
    ['2021-02-02 00:00:00', '2021-02-03 00:00:00'],
    ['2021-02-03 00:00:00', '2021-02-04 00:00:00']]
    
    assert voulu == resultat
    
    
    
    
if __name__ == '__main__' :
    
    #test_alimentation_date_bloc  ()
    print ('fin test_alimentation_date_bloc ', )      
    
