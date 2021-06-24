# coding: utf-8
import json, time, sys
import luigi

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


from Execution import Execution_ID
from Execution_sortie import Execution_sortie

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
from detruirePath import detruirePath

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
arg ['path_fichier_sortie'] = './test_Sortie_fichier.txt'

arg_json = json.dumps (arg)

luigi.build([Execution_ID (arg_travail = arg_json)],
                 workers= 1, local_scheduler = True)


t = time.time()
if __name__ == '__main__':
    luigi.build([Execution_sortie (arg_travail = arg_json)],
                 workers= 1, local_scheduler = True)
    
    dir_path = arg ['pathLuigi_file']
    
    detruirePath (dir_path)
    
   

print ('fin test Execution en ',time.time() - t)
