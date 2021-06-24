# coding: utf-8
from datetime import datetime
import sys

from Paragraphe_date import Paragraphe_date

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock

def test_paragraphe_date () :
    arg = {}
    nom_environnement = 'test'
    arg ['nom_environnement'] =  'nom_environnement'


    arg_entree_sortie_lock = {} 
    arg_entree_sortie_lock ['pathFile'] = '../data/test/parametres/dico_evenements_2.json'
    Entree_sortie = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_evenements  = Entree_sortie.lire_with_lock()
    Entree_sortie.unlock_lire ()
    arg ['pathDico_evenements'] = dico_evenements
    
    #P(dico_evenements)
    arg_entree_sortie_lock ['pathFile'] = '../data/test/parametres/dico_systeme_2.json'
    Entree_sortie = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_systeme  = Entree_sortie.lire_with_lock()
    Entree_sortie.unlock_lire ()
    arg ['pathDico_systeme'] = dico_systeme
    
        
    date_string = "2021-04-27 19:45:00.000000"
    
    
    C = Paragraphe_date (arg)
    
    nom_variable = 'date_evenement'
    enreg = {nom_variable : date_string} 
    
    resultat = C.calcul_sous_vecteur_date (nom_variable, enreg)
    #P(resultat)
    voulu = [   'date_evenement_apm',
                'date_evenement_mardi',
                'date_evenement_17',
                'date_evenement_avril',
                'date_evenement_2021',
                'date_evenement_non_ferie']
    
    #P(resultat)
    
    assert resultat == voulu
    
    date_string = "2021-11-11 19:45:00.000000"
    
    
    C = Paragraphe_date (arg)
    
    nom_variable = 'date_evenement'
    enreg = {nom_variable : date_string} 
    
    resultat = C.calcul_sous_vecteur_date (nom_variable, enreg)
    #P(resultat)
    voulu = [   'date_evenement_apm',
                'date_evenement_jeudi',
                'date_evenement_45',
                'date_evenement_novembre',
                'date_evenement_2021',
                'date_evenement_11_novembre']
    
    assert resultat == voulu
    
    
    
if __name__ == '__main__' :
    test_paragraphe_date ()
    print ('test_paragraphe_date OK')       
    
    
