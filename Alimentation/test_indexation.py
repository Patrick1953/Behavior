# coding: utf-8
import json, sys, time
from datetime import datetime

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)
from Alimentation import  Mise_a_jour_alimentation
from Indexation_evenements import Indexation_evenements
path = "../outils"
if path not in sys.path :
    sys.path.append (path)
    
from Kernel_entree import Kernel_entree
from PARAMETRAGES import  Update_create__environnement

def lire_file (pathFile) :
    f = open (pathFile, 'r')
    data = f.read()
    return json.loads (data)


def test_Indexation_evenements () :
    
    
    
    
    #init #test
    Update_create__environnement ('test')
    
    
    pathEvenements = '../data/#test/parametres/dico_evenements_2.json'
    pathSysteme = '../data/#test/parametres/dico_systeme_2.json'
    nom_environnement = '#test'
    
    dico_evenements = lire_file (pathEvenements)
    dico_systeme = lire_file (pathSysteme)
    
    
    
    arg = {}
    arg ['dico_evenements'] = dico_evenements
    arg ['dico_systeme'] = dico_systeme
    arg ['nom_environnement'] = nom_environnement
    arg ['isPurge_existing_index'] = True
    arg ['nom_tache_alimentation'] = 'test'
        
    arg_kernel_fichier = dico_evenements  ['environnement'] ['parametres_lecture']
    arg_kernel_fichier ['nom_fichier'] = 'evenements.csv'
    
    K = Kernel_entree (arg_kernel_fichier)
    K.init_lecture()
    iterateur = K.readIterator
    
    #P(arg)
    
    I = Indexation_evenements (arg, iterateur)
    
    
    date_now = str(datetime.now())
    I.memorisation_date_min_max (date_now)
    assert I.date_min == date_now
    assert I.date_max == date_now
    
    
    
    I = Indexation_evenements (arg, iterateur)
    
    
    s = 'test'
    assert I.convertir (s, 'ID') == s
    assert I.convertir (date_now, 'date_evenement') == date_now
    assert I.test_val(s, 'ID')
    assert I.test_val(date_now, 'date_evenement')
       
    arg_resultat = I.indexation ()
    voulu = {   'date_max': '2021-02-08 11:41:19.754879',
    'date_min': '2021-02-01 00:57:06.244944',
    'etat': 'OK',
    'isPurge_existing_index': True,
    'nom_tache_alimentation': 'test',
    'nombre_erreur': 0,
    'nombre_ligne': 192}
    
    assert voulu == arg_resultat
    #P(arg_resultat)
    '''
    arg = {}
    arg ['nom_environnement'] = '#test'
    mise_a_jour = Mise_a_jour_alimentation (arg)
    
    mise_a_jour.run (arg_resultat)
        
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
    #print (taille_globale)
    assert taille_globale == [0, 192]
    '''
    Update_create__environnement ('test')
    
def test_indexation_bresil () :
    
    pathEvenements = '../data/#bresil/parametres/dico_evenements_2.json'
    pathSysteme = '../data/#bresil/parametres/dico_systeme_2.json'
    nom_environnement = '#bresil'
    
    dico_evenements = lire_file (pathEvenements)
    dico_systeme = lire_file (pathSysteme)
    
    
    nom_environnement = '#bresil'
    arg = {}
    arg ['dico_evenements'] = dico_evenements
    arg ['dico_systeme'] = dico_systeme
    arg ['nom_environnement'] = nom_environnement
    arg ['isPurge_existing_index'] = True
    arg ['nom_tache_alimentation'] = 'bresil'
        
    arg_kernel_fichier = dico_evenements  ['environnement'] ['parametres_lecture']
    arg_kernel_fichier ['nom_fichier'] = 'mois_1.csv'
    
    K = Kernel_entree (arg_kernel_fichier)
    K.init_lecture()
    iterateur = K.readIterator
    
    #P(arg)
    
    I = Indexation_evenements (arg, iterateur)
    
    arg_resultat = I.indexation ()
    #P( arg_resultat)
    
    voulu = {   'date_max': '2018-01-31 23:58:22.000000',
    'date_min': '2017-01-05 11:56:06.000000',
    'etat': 'OK',
    'isPurge_existing_index': True,
    'nom_tache_alimentation': 'bresil',
    'nombre_erreur': 0,
    'nombre_ligne': 8055}
    
    assert voulu == arg_resultat
    
    
    
    
    
if __name__ == '__main__' :
    t = time.time ()
    test_Indexation_evenements ()
    test_indexation_bresil ()
    print ('fin test_Indexation_evenements en ', time.time() - t, ' secondes')  
