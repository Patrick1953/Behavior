# coding: utf-8
import json, luigi, os, sys

from Creation import Creation_paragraphe, Creation_paragraphe_simulation

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

def test_creation_simulation () :
    

    arg = {}


    #  variable pour alimentation bloc

    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = None
    arg ['isReference'] = False






    arg ['isVariable'] =  True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00.000000'
    arg ['variable_max'] = '2021-02-09 00:00:00.000000'
    arg ['variable_sort'] = 'asc'

    arg ['isID'] = True
    arg ['ID_min'] = "couple_cadre_1"
    arg ['ID_max']  = "couple_cadre_sup_1"
    arg ['ID_sort']  = 'asc'
    arg ['isTrace'] = False


    arg ['pathDico_evenements'] = '../data/dico_evenements_2.txt'
    arg ['pathDico_systeme'] = '../data/dico_systeme_2.txt'





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
    

    arg_entree_sortie_lock ['pathFile'] = pathFile_systeme
    Entree_sortie_systeme = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_systeme, etat = Entree_sortie_systeme.lire()
    arg ['pathDico_systeme'] = dico_systeme

    pas_date = '2021-02-08 00:00:00.000000'. replace (':', '.').replace (' ', '_')
    arg ['pathLuigi_file'] = '../data/test/data/' + pas_date + '/'

    arg_json = json.dumps (arg)

    C = Creation_paragraphe_simulation (arg_travail = arg_json)

    r = C.requires ()
    assert r == []
    r = C.output ()
    
    name_file = C.nom_file
    
    #P(name_file)
    voulu = '../data/test/data/2021-02-08_00.00.00.000000/couple_cadre_1_couple_cadre_sup_1_2021-02-01_00.00.00.000000_2021-02-09_00.00.00.000000.json'
    assert name_file == voulu
    

    resultat = C.run_tache()



    assert resultat == 'OK'
    
    f = open (name_file, 'r')
    
    dico = C.lire_luigi_file (f)
    
    liste_ID = [ID for ID in dico.keys()]
    liste_ID.sort()
    voulu = ['couple_cadre_1', 'couple_cadre_sup_0', 'couple_cadre_sup_1']
    
    assert liste_ID == voulu
    path = C.path
       
    for name_file in os.scandir(path):
        if name_file.name.endswith(".json"):
            os.unlink(name_file.path)

    
if __name__ == '__main__' :
    test_creation_simulation ()
    print ('fin test simulation')
