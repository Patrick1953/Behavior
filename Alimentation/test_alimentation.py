# coding: utf-8
import json, sys, time

from datetime import datetime

from pprint import PrettyPrinter 
def PP (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from PARAMETRAGES_2_2 import ecriture    
from Alimentation import Alimentation, Mise_a_jour_alimentation, Alimentation_calcul 




def test_alimentation () :
    
    ecriture ()
       
    nom_environnement = '#test'
       
    arg = {}
    arg ['nom_environnement'] = nom_environnement
    arg ['isPurge_existing_index'] = True
    arg ['nom_fichier'] =  'evenements.txt'
    arg ['nom_tache_alimentation'] = 'test'
    
    A = Alimentation_calcul (arg)
    
    arg_resultat = A.run()
    
    def lire_file (pathFile) :
        f = open (pathFile, 'r')
        data = f.read()
        return json.loads (data)
    
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
    
    
       
    arg = {}
    arg ['nom_environnement'] = nom_environnement
    arg ['isPurge_existing_index'] = True
    arg ['nom_fichier'] =  'evenements.txt'
    arg ['nom_tache_alimentation'] = 'test'
    A = Alimentation (arg)
    A.run()
    
    ecriture ()
    
    
    
    
if __name__ == '__main__' :
    t = time.time()
    test_alimentation ()
    print ('fin test_alimentation en ', time.time () - t)      
