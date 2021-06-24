# coding: utf-8
from datetime import datetime
import sys

from Calcul_date import Calcul_date

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

def test_calcul_date () :
    

    arg_entree_sortie_lock = {} 
    
    
    arg_entree_sortie_lock ['pathFile'] = '../data/test/parametres/dico_systeme_2.json'
    Entree_sortie_systeme = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_systeme = Entree_sortie_systeme.lire_with_lock()
    Entree_sortie_systeme.unlock_lire ()
    
    #P(dico_systeme)
    
    format_date_standard = dico_systeme ['calcul'] ['format_date_standard']
    date_string = "2021-04-27 19:45:00.000000"
    date = datetime.strptime(date_string, format_date_standard)
    
    C = Calcul_date ()
    
    
    dico = {
        
        'demi_jour' :C.Demi_jour,
        'jour' : C.Jour,
        'semaine' : C.Semaine,
        'mois' : C.Mois,
        'annee' : C.Annee,
    }
    
    voulu = {
        
        'demi_jour' :'apm',
        'jour' : 'mardi',
        'semaine' : '17',
        'mois' : 'avril',
        'annee' : '2021',
        
        }
    
    for type_calcul in dico.keys () :
        r = dico [type_calcul] (date)
        v = voulu [type_calcul]
        assert r == v
        continue
        
    date_string = "2021-04-27 19:45:00.000000"
    date = datetime.strptime(date_string, format_date_standard)
    
    
    resultat = C.get_jour_ferie ( date)
    
    assert resultat == 'non_ferie'
    
    date_string = "2030-12-25 19:45:00.000000"
    date = datetime.strptime(date_string, format_date_standard)
    resultat = C.get_jour_ferie ( date)
       
    assert resultat == 'jour_de_noël'
    
    date_string = "2030-11-11 19:45:00.000000"
    date = datetime.strptime(date_string, format_date_standard)
    resultat = C.get_jour_ferie ( date)
      
    assert resultat == '11_novembre'
    
    resultat = C.get_calcul_dates ()
    liste = [op for op in resultat.keys()]
    voulu = C.get_liste_travail_date ()
    assert voulu == liste
        
if __name__ == '__main__' :
    test_calcul_date ()
    print ('test_calcul_date OK')   
