# coding: utf-8
# test 
import time
from datetime import datetime
from Alimentation_bloc import Alimentation_bloc

from Entree_sortie_lock import Entree_sortie_lock

def test_alimentation_bloc_general () :
    arg_kernel = {  
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
              "_ID_reference_base" : "000000000000000000000000000000",


                    }




    # test ligne sur un ID min max
    arg = {}
    nom_environnement = 'test'
    pathFile_evenements = '/dico_evenements_2.json'
    pathFile_systeme = '/dico_systeme_2.json'


    arg_entree_sortie_lock = {} 
    arg_entree_sortie_lock ['nom_environnement'] = nom_environnement
    arg_entree_sortie_lock['pathFile'] = pathFile_evenements
    Entree_sortie_evenements = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_evenements, etat = Entree_sortie_evenements.lire()

    arg_entree_sortie_lock = {} 
    arg_entree_sortie_lock ['nom_environnement'] = nom_environnement
    arg_entree_sortie_lock['pathFile'] = pathFile_systeme
    Entree_sortie_evenements = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_systeme, etat = Entree_sortie_evenements.lire()


    arg ['pathDico_systeme'] = dico_systeme
    arg['pathDico_evenements'] = dico_evenements
    arg['isTrace'] = False

    #  variable pour alimentation bloc


    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = None
    arg ['isReference'] = False

    arg ['isVariable'] =  True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00'
    arg ['variable_max'] = '2021-02-08 00:00:00'
    arg ['variable_sort'] = 'asc'

    arg ['isID'] = False
    arg ['ID_min'] = "couple_cadre_0"
    arg ['ID_max']  = "couple_cadre_0"
    arg ['ID_sort']  = None

    A = Alimentation_bloc (arg)

    for enreg in A.get_ligne (' ') :
        l = [v for v in enreg.keys()]
        assert len(l) ==  9 
        continue

    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = None
    arg ['isReference'] = False

    arg ['isVariable'] =  False
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00'
    arg ['variable_max'] = '2021-02-08 00:00:00'
    arg ['variable_sort'] = None

    arg ['isID'] = True
    arg ['ID_min'] = "couple_cadre_0"
    arg ['ID_max']  = "couple_cadre_0"
    arg ['ID_sort']  = 'asc'

    A = Alimentation_bloc (arg)


    nombre_1 = 0   
    for variable in A.get_ligne (' ') :
        assert variable['ID'] == "couple_cadre_0" 
        nombre_1 += 1
        continue

    assert nombre_1 == 12 


    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 1000000000
    arg ['ID_reference_sort'] = None
    arg ['isReference'] = False

    arg ['isVariable'] =  True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00'
    arg ['variable_max'] = '2021-02-09 11:08:40'
    arg ['variable_sort'] = 'asc'

    arg ['isID'] = True
    arg ['ID_min'] = "couple_cadre_0"
    arg ['ID_max']  = "homme_ouvrier_1"
    arg ['ID_sort']  = None

    arg ['isTrace'] = False

    A = Alimentation_bloc (arg)

    voulu = ['ID', 'date_evenement', 'description', 'nomenclature_1', 'nomenclature_2',
             'nomenclature_3', 'nomenclature_4', 'prix', 'prix_panier']
    nombre_1 = 0
    for ligne in A.get_ligne (' ') :
        nombre_1 += 1
        l = [v for v in ligne.keys()]
        assert l == voulu 
        date_lu = ligne ['date_evenement']
        assert not date_lu >= '2021-02-09 11:08:40' 
            








    assert nombre_1 == 192 , '#################### erreur nombre de ligne n =' + str( nombre_1)
        


if __name__ == '__main__' :
    t = time.time()
    test_alimentation_bloc_general ()
    print ('fin test_alimentation_bloc_general en ', time.time () - t)  
