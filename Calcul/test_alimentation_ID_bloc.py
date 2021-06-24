# coding: utf-8
import random, time, copy, json, sys
from datetime import datetime
from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Alimentation_ID_bloc import Alimentation_ID_bloc

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock

def test_alimentation_ID_bloc ():
    arg = {}
    arg ['isTrace'] = False
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
    
    #  variable pour alimentation bloc_date

    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = None
    arg ['isReference'] = False






    arg ['isVariable'] =  True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00.000'
    arg ['variable_max'] = '2021-02-08 00:00:00.000'
    arg ['variable_sort'] = None

    arg ['isID'] = False
    arg ['ID_min'] = ""
    arg ['ID_max']  = ""
    arg ['ID_sort']  = 'asc'
    
    arg ['isTrace'] = False
    
    
    
    A = Alimentation_ID_bloc (arg)
    
    resultat = A.get_liste_bornes_ID ()
    
    
    
    liste_test =     ["couple_cadre_0", "couple_cadre_1", "couple_cadre_sup_0",
                      "couple_cadre_sup_1", "couple_enfant_cadre_0",
                    "couple_enfant_cadre_1", "couple_enfant_cadre_sup_0", "couple_enfant_cadre_sup_1",
                    "couple_enfant_ouvrier_0", "couple_enfant_ouvrier_1", "couple_ouvrier_0",
                      "couple_ouvrier_1",
                    "femme_cadre_0", "femme_cadre_1", "femme_cadre_sup_0", "femme_cadre_sup_1",
                      "femme_ouvrier_0",
                    "femme_ouvrier_1", "homme_cadre_0", "homme_cadre_1", "homme_cadre_sup_0",
                    "homme_cadre_sup_1", "homme_ouvrier_0", "homme_ouvrier_1"]

    liste_test.sort()
    nombre_ID_par_bloc = A.nombre_ID_par_bloc
    
    for ID_debut, ID_fin in resultat [:-1]:
        index_debut = liste_test.index (ID_debut)
        index_fin  = liste_test.index (ID_fin)
        assert (index_fin - index_debut) + 1 == nombre_ID_par_bloc
    
    ID_debut, ID_fin = resultat [len(resultat) - 1]    
    index_debut = liste_test.index (ID_debut)
    index_fin  = liste_test.index (ID_fin)
    assert (index_fin - index_debut) + 1 <= nombre_ID_par_bloc
    

    
    
if __name__ == '__main__' :
    test_alimentation_ID_bloc ()
    print ('fin test_alimentation_bloc')    
