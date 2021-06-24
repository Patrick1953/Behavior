# coding: utf-8
import json, sys, os, time
import numpy as np

from gensim.utils import save_as_line_sentence
from gensim.parsing.preprocessing import preprocess_string

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
    
from Kernel_BE import Kernel

from Embedding import Gestion_vecteur, Embedding
from Apprentissage_par_corpus import Apprentissage_par_corpus



arg = {}

nom_environnement = 'test'
arg ['nom_environnement'] =  nom_environnement


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

arg ['pathLuigi_file'] = './'

arg['pathModele'] = '../data/test/data/'+ pas + '/' +'Modele_test2.model'
arg ['Path_corpus'] = 'mon_corpus.txt'


arg ['Path_corpus']  = 'mon_corpus.txt'


pathFile = './test_embedding.json'
fin = open (pathFile,'r')

dico = {}
for ligne_json in fin:
    dico_ligne = json.loads (ligne_json)
    dico.update(dico_ligne)
    
liste_ID = [ID for ID in dico.keys()]
liste_ID.sort()
arg ['nombre_ID'] = len(liste_ID)


A = Apprentissage_par_corpus(arg)


pathFile = './test_embedding.json'
fin = open (pathFile,'r')

t = time.time()
A.init_corpus ()
A.ecrire_luigi_file_random (fin)
A.Apprentissage_par_corpus ()
A.save_model ()
delaie = time.time() - t

print ("apprentissage modele par corpus en temps =", delaie)
print ()



# on repete 
repetition = 200

A = Apprentissage_par_corpus(arg)


pathFile = './test_embedding.json'
fin = open (pathFile,'r')

t = time.time()
A.init_corpus ()
A.ecrire_luigi_file_random (fin)
for _ in range (0, repetition) :
    A.Apprentissage_par_corpus ()
A.save_model ()
delaie = time.time() - t

print ("apprentissage modele par corpus avec repetition ", repetition, ' et un temps =', delaie)
print ()

# on test la qualité
E = Gestion_vecteur (arg)

pathFile = './test_embedding.json'
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


print ('conclusion : OK pour l inference ')

normalized_array, liste_ID = E.get_vecteur_normalized (dico)

ID_0 = liste_ID [0]
paragraphe = dico [ID_0]

v0 = E.infer_vecteur_embedding (paragraphe)
v0_0 = v0/np.linalg.norm(v0)

assert (np.sum(normalized_array [0, :] - v0_0) < 10.e-7)

print ('end of job')
