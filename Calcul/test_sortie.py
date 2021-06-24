# coding: utf-8
import json, sys


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock

from Sortie import Sortie

def test_sortie () :
    
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
    
    parametres = dico_systeme ['environnement'] [nom_environnement] ['parametres_ecriture']
    arg ['parametres'] = parametres
    path_data = pas + '/' + pas_date + '/'
    arg ['nom_data'] = path_data  + 'test.txt'
    
    S = Sortie (arg)
    S.init_ecriture ()
    
    f_lecture = 'test_embedding.json'
    fin = open (f_lecture, 'r')
    
    S.ecrire_resultat (fin)
    
    S.close()
    
    # test 
    
    f = open (S.pathFile , 'r')
    nombre = 0
    for data in f :
        dico = json.loads(data)
        ID = [cle for cle in dico.keys()] [0]
        dico_out = dico [ID]
        assert len(dico_out) == 2
        nombre += 1
        assert len (dico_out [ 'vector']) == 100
        
    assert nombre == 24
    
    
        
    
    
    
    



if __name__ == '__main__':
    test_sortie()
