# coding: utf-8
import random, time, copy, json, sys
from datetime import datetime

from Paragraphe_quantile import  Paragraphe_quantile


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)

from Entree_sortie_lock import Entree_sortie_lock
from Kernel_BE import Kernel


from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


def  test_paragraphe_quantile () :
    arg = {}
    nom_environnement = 'test'
    arg ['nom_environnement'] =  'nom_environnement'
    
    
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
    
    
    
    #  variable pour alimentation bloc

    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = 'asc'
    arg ['isReference'] = False






    arg ['isVariable'] =  True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00'
    arg ['variable_max'] = '2021-02-04 00:00:00'
    arg ['variable_sort'] = 'asc'

    arg ['isID'] = True
    arg ['ID_min'] = "couple_cadre_1"
    arg ['ID_max']  = "couple_cadre_sup_1"
    arg ['ID_sort']  = None
    arg ['isTrace'] = False

    C = Paragraphe_quantile (arg)
    nom_variable = 'prix'
    ligne =  {nom_variable : 15.}

    resultat = C.calcul_sous_vecteur_quantile (nom_variable, ligne )
    
    
    
    voulu = ['prix_quartile_1', 'prix_decile_2', 'prix_manuel1_2']
    assert voulu == resultat
    
if __name__ == '__main__' :
    
    test_paragraphe_quantile ()
    print ('test_paragraphe_quantile OK')
    
