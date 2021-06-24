# coding: utf-8
import time, sys
from Execution import Execution, Mise_a_jour_execution, Execution_calcul
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from detruirePath import detruirePath

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

def test_execution () :
    nom_environnement = '#test'
    arg = {}
    arg ['date_min'] = '2021-02-01 00:00:00.000000'
    arg ['date_max'] = '2021-02-09 00:00:00.000000'
    arg ['pas'] = 'semaine'
    arg ['nom_environnement'] = nom_environnement
    arg ['nom_tache_execution'] = nom_environnement
    
    arg ['workers'] = 6
    arg ['local_scheduler'] = True
    t = time.time()
    resultat = Execution_calcul (arg).run()
    
    arg = {}
    arg ['nom_environnement'] = nom_environnement
    M = Mise_a_jour_execution (arg)
    M.run(resultat)
    
    pas = resultat ['pas']
    dico_evenements = M.dico_evenements
    
    liste_execution_new = dico_evenements ['pas']  ['semaine'] ['liste_execution']
    new_info = liste_execution_new.pop()
    del new_info ['date_creation']
    
    voulu = {   'date_max': '2021-02-09 00:00:00.000000',
    'date_min': '2021-02-01 00:00:00.000000',
    'nom_tache_execution': '#test',
    'sortie': '../data/#test/data/semaine/2021-02-09_00.00.00.000000/'}
    
    
    assert new_info == voulu
    
    
    dir_path = resultat ['sortie']
    detruirePath (dir_path)
    
    t = time.time ()
    arg = {}
    arg ['date_min'] = '2021-02-01 00:00:00.000000'
    arg ['date_max'] = '2021-02-09 00:00:00.000000'
    arg ['pas'] = 'semaine'
    arg ['nom_environnement'] = nom_environnement
    arg ['nom_tache_execution'] = nom_environnement
    
    arg ['workers'] = 6
    arg ['local_scheduler'] = True
    t = time.time()
    Execution (arg).run()
    
    print ('total calcul plus mise à jour', time.time () - t )
    
    
        
    
if __name__ == '__main__':
    
    test_execution ()
