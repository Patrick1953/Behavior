# coding: utf-8
import json, time, sys
import luigi

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Calcul_bloc_ID import Calcul_bloc_ID, get_liste_bloc

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
from detruirePath import detruirePath

arg = {}


#  variable pour alimentation bloc_date

arg ['ID_reference_min'] = 0
arg ['ID_reference_max'] = 100000000
arg ['ID_reference_sort'] = None
arg ['isReference'] = False






arg ['isVariable'] =  True
arg ['nom_variableQuery'] = "date_evenement"
arg ['variable_min'] = '2021-02-01 00:00:00.000'
arg ['variable_max'] = '2021-02-08 00:00:00.000'
arg ['variable_sort'] = None

arg ['isID'] = False
arg ['ID_min'] = ""# avec
arg ['ID_max']  = ""
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

arg_json = json.dumps (arg)

t = time.time()
if __name__ == '__main__':
    luigi.build([Calcul_bloc_ID (arg_travail = arg_json)],
                 workers= 1, local_scheduler = True)
    
    
    voulu = [['couple_cadre_0', 'couple_cadre_1'], ['couple_cadre_sup_0', 'couple_cadre_sup_1'],
              ['couple_enfant_cadre_0', 'couple_enfant_cadre_1'],
              ['couple_enfant_cadre_sup_0', 'couple_enfant_cadre_sup_1'],
              ['couple_enfant_ouvrier_0', 'couple_enfant_ouvrier_1'],
              ['couple_ouvrier_0', 'couple_ouvrier_1'], ['femme_cadre_0', 'femme_cadre_1'],
              ['femme_cadre_sup_0', 'femme_cadre_sup_1'], ['femme_ouvrier_0', 'femme_ouvrier_1'],
              ['homme_cadre_0', 'homme_cadre_1'], ['homme_cadre_sup_0', 'homme_cadre_sup_1'],
              ['homme_ouvrier_0', 'homme_ouvrier_1']]
    resultat, nombre_ID = get_liste_bloc (arg)
    assert resultat == voulu
    assert nombre_ID == 24
    dir_path = arg ['pathLuigi_file']
    detruirePath (dir_path)
    #print (dir_path, ' supprimé')
    
    
    
    
   

print ('fin test Execution en ',time.time() - t)
