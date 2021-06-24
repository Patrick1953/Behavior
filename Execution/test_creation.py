# coding: utf-8
from Creation import Creation_paragraphe, Creation_paragraphe_simulation
import json, luigi, os, sys

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

def test_creation () :
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
    arg ['ID_sort']  = 'asc'
    
    arg ['isTrace'] = False


    





    nom_environnement = 'test'
    arg ['etape'] = 'creation'
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
    
    pas_date = '2021-02-08 00:00:00.000000'.replace (':', '.').replace (' ', '_')
    arg ['pathLuigi_file'] = '../data/test/data/' + pas_date + '/'


    arg_json = json.dumps (arg)
    
    luigi.build([Creation_paragraphe (arg_travail = arg_json)],
                 workers=1, local_scheduler = True)
    
    liste_file = os.listdir(arg ['pathLuigi_file'])
    
    
    nom_file = liste_file [0]
    pas_date = '2021-02-08 00:00:00.000000'.replace (':', '.').replace (' ', '_')
    path = '../data/test/data/' + pas_date + '/'

    pathFile = path + nom_file
    
    #P(pathFile)

    f = open (pathFile, 'r')

    r = []
    for ligne in f :
        dico = json.loads (ligne)
        r.append([cle for cle in dico.keys()][0] )
        
    r.sort()
        
    voulu = ["couple_cadre_0", "couple_cadre_1", "couple_cadre_sup_0", "couple_cadre_sup_1",
             "couple_enfant_cadre_0", "couple_enfant_cadre_1", "couple_enfant_cadre_sup_0",
             "couple_enfant_cadre_sup_1", "couple_enfant_ouvrier_0", "couple_enfant_ouvrier_1",
             "couple_ouvrier_0", "couple_ouvrier_1", "femme_cadre_0", "femme_cadre_1", "femme_cadre_sup_0",
             "femme_cadre_sup_1", "femme_ouvrier_0", "femme_ouvrier_1", "homme_cadre_0", "homme_cadre_1",
             "homme_cadre_sup_0", "homme_cadre_sup_1", "homme_ouvrier_0", "homme_ouvrier_1"]
    
    
    
    assert r == voulu
    
    os.remove(pathFile)
    pathFile
    
    return 





if __name__ == '__main__' :
    test_creation ()
    print ('fin de creation')  
    
    
