# coding: utf-8
import json, sys, time
import luigi

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
from detruirePath import detruirePath

from Reunion import Reunion_paragraphe

def test_reunion_paragraphe (nombre_worker = 1) :
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
    arg ['ID_min'] = "couple_cadre_0"
    arg ['ID_max']  = "homme_ouvrier_1"
    arg ['ID_sort']  = None
    arg ['isTrace'] = False

    arg ['pathListe_ID'] =  "../data/listeID.txt"
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

    pas_date = '2021-02-04 00:00:00.000000'.replace (':', '.').replace (' ', '_')
    arg ['pathLuigi_file'] = '../data/test/data/' + pas_date + '/'

    arg_json = json.dumps (arg)

    t = time.time ()
    luigi.build([Reunion_paragraphe (arg_travail = arg_json)],
                 workers = nombre_worker, local_scheduler = True)
    
    delaie = time.time () - t
    

    dir_path = arg ['pathLuigi_file']
    
    detruirePath (dir_path)
    
    return delaie
    
    
if __name__ == '__main__':
    
    delaie = test_reunion_paragraphe (nombre_worker = 1)
    print ('avec 1 worker delaie =', delaie)
    print ()
    delaie = test_reunion_paragraphe (nombre_worker = 3)
    print ('avec 3 worker delaie =', delaie)
    print ()
    print ('fin test_reunion_paragraphe')
