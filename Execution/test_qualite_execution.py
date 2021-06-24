# coding: utf-8
# on test la qualité

import json, time, sys
import luigi

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Execution import Execution_ID

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
from detruirePath import detruirePath


path = "../Calcul"
if path not in sys.path : 
    sys.path.append (path)
from Embedding import Gestion_vecteur

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

E = Gestion_vecteur (arg)

pathFile = '../Calcul/test_embedding.json'
fin = open (pathFile,'r')
        
dico = {}
for ligne_json in fin:
    dico_ligne = json.loads (ligne_json)
    dico.update(dico_ligne)
    
liste_ID = [ID for ID in dico.keys()]
liste_ID.sort()


ID_1 = liste_ID [0]
paragraphe_1 = dico [ID_1]
vecteur_calcule_1 = E.infer_vecteur_embedding (paragraphe_1)



ID_2 = liste_ID [len(liste_ID) - 1]
paragraphe_2 = dico [ID_2]
vecteur_calcule_2 = E.infer_vecteur_embedding (paragraphe_2)

similarite1_1 = E.similarite_par_vecteur (vecteur_calcule_1, vecteur_calcule_2)
print ('similarite entre deux paragraphes calculés differents =', similarite1_1 )
distance_1_1 = E.calcul_distance (vecteur_calcule_1 ,vecteur_calcule_2)
print ('distance entre deux paragraphes calculés differents =', distance_1_1)
print ()


print ('conclusion : OK pour passer à l inference ')
