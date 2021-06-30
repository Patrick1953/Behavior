# coding: utf-8
import json, sys, time

from datetime import datetime

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Kernel_entree import Kernel_entree

path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from PARAMETRAGES import Update_create__environnement    
from Alimentation import Alimentation, Mise_a_jour_alimentation, Alimentation_calcul 

def lire_file (pathFile) :
    f = open (pathFile, 'r')
    data = f.read()
    return json.loads (data)


def test_alimentation () :
    
    
    
    Update_create__environnement ('test')
    
    pathEvenements = '../data/#test/parametres/dico_evenements_2.json'
    dico_systeme = lire_file (pathEvenements)
           
    arg_kernel_fichier = dico_systeme  ['environnement']['parametres_lecture']
    arg_kernel_fichier ['nom_fichier'] = 'evenements.csv'
    dico_systeme  ['environnement']['parametres_lecture'] = arg_kernel_fichier
    
    E = Kernel_entree (arg_kernel_fichier)
    
    E.init_lecture ()
    
    numero = 0
    for data in E.readIterator () :
        numero += 1
        continue
    E.close ()   
    assert numero == 192
    
    pathFile = '../data/#test/parametres/dico_evenements_2.json'
    dico_evenements = lire_file (pathFile)
    voulu = {   'parametres_ecriture': {   'parametres_execution': {   'type_lecteur': 'fichier'},
                               'path_sortie': '../data/data_sortie/test/'},
    'parametres_lecture': {   'parametres_execution': {   'type_lecteur': 'fichier'},
                              'path_fichier': '../data/#test/data_alimentation/',
                              'separateur': '|'}}
    
    assert voulu == dico_evenements ['environnement']
    
    
      
    arg = {}
    arg ['nom_environnement'] = '#test'
    arg ['isPurge_existing_index'] = True
    arg ['nom_fichier'] =  'evenements.csv'
    arg ['nom_tache_alimentation'] = 'test'
    
    A = Alimentation_calcul (arg)
    
    voulu = {   'dico_evenements': {   'alimentation': {   'execution': {   'date_debut_alimentation': '2021-02-01 '
                                                                                           '00:00:00',
                                                                'dico_ajout': {   },
                                                                'index_data': 'data_fake',
                                                                'nombre_erreur_max': 0,
                                                                'taille_globale': [   0,
                                                                                      0]}},
                           'apprentissage': {'liste_execution': []},
                           'creation_dictionnaire': {   'ID': {   'parametres': [   ],
                                                                  'travail': None},
                                                        'date_evenement': {   'parametres': [   ],
                                                                              'travail': 'date'},
                                                        'description': {   'parametres': [   {   'format': 'standard'}],
                                                                           'travail': 'analyse_mot'},
                                                        'nomenclature_1': {   'parametres': [   {   'format': 'standard'}],
                                                                              'travail': 'analyse_mot'},
                                                        'nomenclature_2': {   'parametres': [   {   'format': 'standard'}],
                                                                              'travail': 'analyse_mot'},
                                                        'nomenclature_3': {   'parametres': [   {   'format': 'standard'}],
                                                                              'travail': 'analyse_mot'},
                                                        'nomenclature_4': {   'parametres': [   {   'format': 'standard'}],
                                                                              'travail': 'analyse_mot'},
                                                        'prix': {   'parametres': [   {   'type': 'quartile'},
                                                                                      {   'type': 'decile'},
                                                                                      {   'nom_manuel': 'manuel1',
                                                                                          'separateurs': [   10.0,
                                                                                                             20.0,
                                                                                                             100.0],
                                                                                          'type': 'manuel'}],
                                                                    'travail': 'quantile'},
                                                        'prix_panier': {   'parametres': [   {   'type': 'quartile'}],
                                                                           'travail': 'quantile'}},
                           'dictionnaire': {   'ID': {   'parametres': [],
                                                         'travail': None},
                                               'date_evenement': {   'parametres': [   {   'type': 'demi_jour'},
                                                                                       {   'type': 'jour'},
                                                                                       {   'type': 'semaine'},
                                                                                       {   'type': 'mois'},
                                                                                       {   'type': 'annee'},
                                                                                       {   'type': 'ferie'}],
                                                                     'travail': 'date'},
                                               'description': {   'parametres': [   {   'type': 'standard'}],
                                                                  'travail': 'analyse_mot'},
                                               'nomenclature_1': {   'parametres': [   {   'type': 'standard'}],
                                                                     'travail': 'analyse_mot'},
                                               'nomenclature_2': {   'parametres': [   {   'type': 'standard'}],
                                                                     'travail': 'analyse_mot'},
                                               'nomenclature_3': {   'parametres': [   {   'type': 'standard'}],
                                                                     'travail': 'analyse_mot'},
                                               'nomenclature_4': {   'parametres': [   {   'type': 'standard'}],
                                                                     'travail': 'analyse_mot'},
                                               'prix': {   'parametres': [   {   'type': 'quartile'},
                                                                             {   'type': 'decile'},
                                                                             {   'nom_manuel': 'manuel1',
                                                                                 'separateurs': [   10.0,
                                                                                                    20.0,
                                                                                                    10.0],
                                                                                 'type': 'manuel'}],
                                                           'travail': 'quantile'},
                                               'prix_panier': {   'en_tete': 'commande_',
                                                                  'parametres': [   {   'type': 'quartile'}],
                                                                  'pathFile': '../data/test/commandes.json',
                                                                  'travail': 'quantile'}},
                           'environnement': {   'parametres_ecriture': {   'parametres_execution': {   'type_lecteur': 'fichier'},
                                                                           'path_sortie': '../data/data_sortie/test/'},
                                                'parametres_lecture': {   'nom_fichier': 'evenements.csv',
                                                                          'parametres_execution': {   'type_lecteur': 'fichier'},
                                                                          'path_fichier': '../data/#test/data_alimentation/',
                                                                          'separateur': '|'}},
                           'pas': {'demi_jour': {'liste_execution': []}},
                           'position': {   'ID': 0,
                                           'date_evenement': 1,
                                           'description': 7,
                                           'nomenclature_1': 3,
                                           'nomenclature_2': 4,
                                           'nomenclature_3': 5,
                                           'nomenclature_4': 6,
                                           'prix': 8,
                                           'prix_panier': 2},
                           'type': {   'ID': {   'format': 'standard',
                                                 'type': 'string'},
                                       'date_evenement': {   'format': 'standard',
                                                             'type': 'date'},
                                       'description': {   'format': 'standard',
                                                          'type': 'string'},
                                       'nomenclature_1': {   'format': 'standard',
                                                             'type': 'string'},
                                       'nomenclature_2': {   'format': 'standard',
                                                             'type': 'string'},
                                       'nomenclature_3': {   'format': 'standard',
                                                             'type': 'string'},
                                       'nomenclature_4': {   'format': 'standard',
                                                             'type': 'string'},
                                       'prix': {   'format': 'standard',
                                                   'type': 'numeric'},
                                       'prix_panier': {   'format': 'standard',
                                                          'type': 'numeric'}}},
    'dico_systeme': {   'calcul': {   'format_date_standard': '%Y-%m-%d '
                                                              '%H:%M:%S.%f',
                                      'format_float_standard': 1.0,
                                      'format_string_standard': '',
                                      'nombre_ID_par_bloc': 2,
                                      'nombre_ID_pour_apprentissage': 50000,
                                      'nombre_bloc_date': 3,
                                      'pourcentage_echantillon': 100.0,
                                      'taille_bloc': 100},
                        'elasticsearch': {   'ID_reference_base': '000000000000000000000000000000',
                                             'createur': 'generic',
                                             'date_emetteur': '2021-06-30 '
                                                              '17:23:05.693820',
                                             'extra_elasticsearch_args': None,
                                             'host': 'localhost',
                                             'http_auth': None,
                                             'index_log_error': 'trace1',
                                             'index_log_trace': 'trace3',
                                             'index_log_warning': 'trace2',
                                             'index_system': 'systeme',
                                             'isPurge_existing_index_log': False,
                                             'port': 9200,
                                             'timeout': 10,
                                             'trace': False,
                                             'zipChoisi': 'bz2'},
                        'embedding': {   'alpha': 0.025,
                                         'decrease_alpha': 0.0002,
                                         'dm': 1,
                                         'isOublie': False,
                                         'max_epoch': 10,
                                         'min_alpha': 0.00025,
                                         'min_count': 1,
                                         'vector_size': 100}},
    'isPurge_existing_index': True,
    'nom_environnement': '#test',
    'nom_tache_alimentation': 'test',
            }
    
    
    
    assert voulu ['dico_evenements'] == A.arg ['dico_evenements'] 
    
    assert voulu ['nom_environnement'] == A.arg ['nom_environnement']
    assert voulu ['isPurge_existing_index'] == A.arg ['isPurge_existing_index']
    assert voulu ['nom_tache_alimentation'] == A.arg ['nom_tache_alimentation']
    
    
    iterateur = A.iterateur ()
    nombre = 0
    for li in iterateur :
        nombre += 1
    
    assert numero == 192
    
    
    A = Alimentation_calcul (arg) 
    arg_resultat = A.run()
    voulu = {   'date_max': '2021-02-08 11:41:19.754879',
    'date_min': '2021-02-01 00:57:06.244944',
    'etat': 'OK',
    'isPurge_existing_index': True,
    'nom_tache_alimentation': 'test',
    'nombre_erreur': 0,
    'nombre_ligne': 192}
    
    
    

    assert voulu == arg_resultat
        
    nom_environnement = '#test'
    arg = {}
    arg ['nom_environnement'] = nom_environnement
    
    mise_a_jour = Mise_a_jour_alimentation (arg)
    mise_a_jour.run (arg_resultat)
    pathEvenements = '../data/'+nom_environnement+ '/parametres/dico_evenements_2.json'    
    dico_evenements = lire_file (pathEvenements)
    dico_alimentation = dico_evenements ['alimentation'] ['execution' ]
     
    dico_ajoute = dico_alimentation ['dico_ajout'] ['ajout_0000000000']
    
    del dico_ajoute ['date_execution']
    voulu = {   
            'date_max': '2021-02-08 11:41:19.754879',
            'date_min': '2021-02-01 00:57:06.244944',
            'nom_alimentation': 'test',
            'nombre_erreur': 0,
            'nombre_ligne': 192,
            'numero_ligne_debut': 0,
            'numero_ligne_fin': 192,
            'purge de la base': True}
    
    
    assert dico_ajoute == voulu
       
    taille_globale = dico_alimentation ['taille_globale']
    
    # verification de l 'ensemble
    
    
    nom_environnement = '#test'   
    arg = {}
    arg ['nom_environnement'] = nom_environnement
    arg ['isPurge_existing_index'] = True
    arg ['nom_fichier'] =  'evenements.csv'
    arg ['nom_tache_alimentation'] = 'test'
    A = Alimentation (arg)
    A.run()
    pathEvenements = '../data/'+nom_environnement+ '/parametres/dico_evenements_2.json'    
    dico_evenements = lire_file (pathEvenements)
    dico_alimentation = dico_evenements ['alimentation'] ['execution' ]
     
    dico_ajoute = dico_alimentation ['dico_ajout'] ['ajout_0000000000']
    del dico_ajoute ['date_execution']
    
    voulu = {   
            'date_max': '2021-02-08 11:41:19.754879',
            'date_min': '2021-02-01 00:57:06.244944',
            'nom_alimentation': 'test',
            'nombre_erreur': 0,
            'nombre_ligne': 192,
            'numero_ligne_debut': 0,
            'numero_ligne_fin': 192,
            'purge de la base': True}
    
    
    assert dico_ajoute == voulu
    
    
    
    Update_create__environnement ('test')
    
    pathFile = '../data/#bresil/parametres/dico_evenements_2.json'
    dico_evenements = lire_file (pathFile)
    voulu = {   'parametres_ecriture': {   'parametres_execution': {   'type_lecteur': 'fichier'},
                               'path_sortie': '../data/data_sortie/test/'},
    'parametres_lecture': {   'parametres_execution': {   'type_lecteur': 'fichier'},
                              'path_fichier': '../data/#bresil/data_alimentation/',
                              'separateur': '|'}}
    
    assert voulu == dico_evenements ['environnement']
    
def test_alimentation_bresil () :
    pathFile = '../data/#bresil/parametres/dico_evenements_2.json'
    dico_evenements_debut = lire_file (pathFile)
    
    arg = {}
    arg ['nom_environnement'] = '#bresil'
    arg ['isPurge_existing_index'] = True
    arg ['nom_fichier'] =  'mois_1.csv'
    arg ['nom_tache_alimentation'] = 'bresil'
    
    A = Alimentation (arg)
    A.run()
    
    pathFile = '../data/#bresil/parametres/dico_evenements_2.json'
    dico_evenements = lire_file (pathFile)
    dico_alimentation = dico_evenements ['alimentation'] ['execution' ]
    
    #P(dico_alimentation)
    
    dico_ajoute = dico_alimentation ['dico_ajout'] ['ajout_0000000000']
    
    del dico_ajoute ['date_execution']
    
    
    
    voulu = {   'date_max': '2018-01-31 23:58:22.000000',
    'date_min': '2017-01-05 11:56:06.000000',
    'nom_alimentation': 'bresil',
    'nombre_erreur': 0,
    'nombre_ligne': 8055,
    'numero_ligne_debut': 0,
    'numero_ligne_fin': 8055,
    'purge de la base': True}
    
    assert dico_ajoute ==  voulu
    
    
    # restauration
    data =json.dumps(dico_evenements_debut)
    pathFile = '../data/#bresil/parametres/dico_evenements_2.json'
    f = open (pathFile, 'w')
    f.write (data)
    
    
    
    
    
    
    
if __name__ == '__main__' :
    t = time.time()
    test_alimentation ()
    test_alimentation_bresil ()
    print ('fin test_alimentation en ', time.time () - t)      
