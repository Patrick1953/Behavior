# coding: utf-8
import random, time, copy, json
from datetime import datetime



import sys
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Kernel_BE import Kernel

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


def test_search_par_bloc() :
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
    arg ['variable_min'] = '2021-02-01 00:00:00'
    arg ['variable_max'] = '2021-02-04 00:00:00'
    arg ['variable_sort'] = 'asc'

    arg ['isID'] = True
    arg ['ID_min'] = "couple_cadre_1"
    arg ['ID_max']  = "couple_cadre_sup_1"
    arg ['ID_sort']  = None
    arg ['isTrace'] = True


    systeme = {  
              "createur" : "generic", 
              "date_emetteur" : str(datetime.now()),
              "http_auth" : None,
              "timeout" : 10,
              "host" : "localhost", 
              "port" : 9200 ,
              "zipChoisi" : 'bz2',
              "index_log_error" : "trace1",
              "index_log_warning" : "trace2",
              "index_log_trace" : "trace3",
              "index_system" : "systeme",
              "isPurge_existing_index_log" : True,
              "extra_elasticsearch_args" : None,
              "trace" : False,
              "ID_reference_base" : "000000000000000000000000000000",


                    }


    kernel = Kernel(systeme)

    debut_bloc = arg['ID_reference_min']
    fin_bloc = arg['ID_reference_max']
    ID_reference_sort = arg ['ID_reference_sort']
    isReference = arg ['isReference']



    isID = arg['isID']
    ID_min = arg ['ID_min']
    ID_max  = arg ['ID_max']
    ID_sort  = arg ['ID_sort']

    isVariable =  arg ['isVariable']
    nom_variableQuery = arg ['nom_variableQuery']
    variable_min = arg ['variable_min']
    variable_max = arg ['variable_max']
    variable_sort = arg ['variable_sort']


    isTrace = arg ['isTrace']
    
    
    size = 700
    taille_lu, hits = kernel.search_par_bloc ("data_fake_",
                                               " ", #deprecated
                                               debut_bloc,
                                               fin_bloc,
                                               size = size,
                                               isReference = isReference,
                                               ID_reference_sort = ID_reference_sort,

                                               isID = isID,
                                               ID_min = ID_min,
                                               ID_max  = ID_max ,
                                               ID_sort  = ID_sort,

                                               isVariable = isVariable,
                                               nom_variableQuery = nom_variableQuery,
                                               variable_min = variable_min,
                                               variable_max = variable_max,
                                               variable_sort = variable_sort,
                                             )


    assert taille_lu == 154, 'erreur sur search par bloc' 
    
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
    arg ['ID_reference_sort'] = None
    arg ['isReference'] = False






    arg ['isVariable'] = True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00'
    arg ['variable_max'] = '2021-02-09 00:00:00'
    arg ['variable_sort'] = None

    arg ['isID'] = False
    arg ['ID_min'] = "couple_cadre_0"
    arg ['ID_max']  = "homme_ouvrier_1"
    arg ['ID_sort']  = 'asc'
    
    arg ['isTrace'] = False
    
    debut_bloc = arg['ID_reference_min']
    fin_bloc = arg['ID_reference_max']
    ID_reference_sort = arg ['ID_reference_sort']
    isReference = arg ['isReference']



    isID = arg['isID']
    ID_min = arg ['ID_min']
    ID_max  = arg ['ID_max']
    ID_sort  = arg ['ID_sort']

    isVariable =  arg ['isVariable']
    nom_variableQuery = arg ['nom_variableQuery']
    variable_min = arg ['variable_min']
    variable_max = arg ['variable_max']
    variable_sort = arg ['variable_sort']
    

    isTrace = arg ['isTrace']
    
    
    size = 1344
    taille_lu, hits = kernel.search_par_bloc ("data_fake",
                                               " ", #deprecated
                                               debut_bloc,
                                               fin_bloc,
                                               size = size,
                                               isReference = isReference,
                                               ID_reference_sort = ID_reference_sort,

                                               isID = isID,
                                               ID_min = ID_min,
                                               ID_max  = ID_max ,
                                               ID_sort  = ID_sort,

                                               isVariable = isVariable,
                                               nom_variableQuery = nom_variableQuery,
                                               variable_min = variable_min,
                                               variable_max = variable_max,
                                               variable_sort = variable_sort,
                                             )
    
    
    
    liste_ID = []
    memoire = {}
    for hit in hits :
        enreg = hit ['_source']
        ID = enreg ['ID']
        
        if not ID in memoire :
            liste_ID.append (ID)
            memoire [ID] = None
        continue
        
    liste_ID_voulu = [ID for ID in memoire.keys()]
    liste_ID_voulu.sort ()
    
    assert liste_ID_voulu == liste_ID
    
    
    
    
        
    

if __name__ == '__main__' :
    test_search_par_bloc()
    print ('fin test search par bloc OK')
