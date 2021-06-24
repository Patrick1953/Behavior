# coding: utf-8
import json, time, sys

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
from detruirePath import detruirePath
from validationPath import validationPath


from Sortie_fichier import Sortie_fichier

def test_sortie_fichier() :
    


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

    pas = 'semaine'
    pas_date = '2021-02-08 00:00:00.000000'.replace (':', '.').replace (' ', '_')
    arg ['pathLuigi_file'] = '../data/test/data/'+ pas + '/' + pas_date + '/'

    arg['pathModele'] = '../data/test/data/'+ pas + '/' +'Modele_test2.model'

    arg ['Path_corpus']  = 'mon_corpus.txt'
    arg ['nombre_ID'] = 24
    
    arg = {}
    parametres = dico_systeme ['environnement'] [nom_environnement] ['parametres_ecriture']
    arg ['parametres'] = parametres
    path_data = pas + '/' + pas_date + '/'
    arg ['nom_data'] = path_data  + 'test.txt'
    
    
    
    
    
    
    
    
    
    S = Sortie_fichier (arg)
    
    S.init_ecriture ()
    voulu = []
    for i in range(0, 10) :
        data = 'test'+str(i)
        S.ecrire (data)
        voulu.append(data)
    S.close()
    
    f = open (S.pathFile, 'r')
    resultat = []
    for ligne in f :
        resultat.append (ligne [:-1])
        
    assert resultat == voulu
    
    path = parametres ['path_sortie'] + path_data
    
    detruirePath (path)
    
if __name__ == '__main__':
    test_sortie_fichier()
    
    
