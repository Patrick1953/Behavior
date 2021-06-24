# coding: utf-8
import sys
from datetime import datetime
from Indexation_evenements import Indexation_evenements 
from Kernel_entree import Kernel_entree

path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock

class Alimentation () :
    def __init__ (self, arg ) :
        
        self.arg = arg
        
    def run  (self, ) :
        
        A = Alimentation_calcul (self.arg)
        arg_resultat = A.run()
        
        M = Mise_a_jour = Mise_a_jour_alimentation (self.arg)
        M.run (arg_resultat)
        #print ('alimentation OK')
        return
    




class Alimentation_calcul (Indexation_evenements) :
    
    def __init__ (self, arg) :
        
        
        self.nom_environnement = arg ['nom_environnement']
        #print (self.nom_environnement)
        pathFile_evenements = '/dico_evenements_2.json'
        pathFile_systeme = '/dico_systeme_2.json'
        
        arg_entree_sortie_lock = {} 
        pathFile = '../data/'+ self.nom_environnement + '/parametres/' + pathFile_evenements
        arg_entree_sortie_lock['pathFile'] = pathFile
        Entree_sortie = Entree_sortie_lock (arg_entree_sortie_lock)
        dico_evenements = Entree_sortie.lire_with_lock ()
        Entree_sortie.unlock_lire ()
        arg ['dico_evenements'] = dico_evenements
        
        #x = dico_evenements ['environnement']
        
        pathFile = '../data/'+ self.nom_environnement + '/parametres/' + pathFile_systeme
        arg_entree_sortie_lock ['pathFile'] = pathFile
        Entree_sortie = Entree_sortie_lock (arg_entree_sortie_lock)
        dico_systeme  = Entree_sortie.lire_with_lock()
        Entree_sortie.unlock_lire ()
        arg ['dico_systeme'] = dico_systeme
        
        
        arg_entree = dico_evenements ['environnement'] ['parametres_lecture']
        nom_fichier = arg ['nom_fichier']
        arg_entree ['nom_fichier'] = nom_fichier
        
        K = Kernel_entree (arg_entree)
        K.init_lecture()
        iterateur = K.readIterator
        
        
        super ().__init__( arg, iterateur)
        

    def run (self,) :
        
        arg_resultat = self.indexation ()
        return arg_resultat
    
class Mise_a_jour_alimentation (Entree_sortie_lock) :
    
    def __init__ (self, arg) :
        
        nom_environnement = arg ['nom_environnement']
        l = nom_environnement.split('%')
        nom_environnement_local = l [0]
        pathFile_evenements = '/dico_evenements_2.json'
        pathFile = '../data/'+ nom_environnement_local + '/parametres/' + pathFile_evenements
        arg_Entree_sortie_lock = {}
        arg_Entree_sortie_lock ['pathFile'] = pathFile
        super().__init__(arg_Entree_sortie_lock) 
        
        
    def run (self, arg) :
               
        nom_alimentation = arg ['nom_tache_alimentation']
        nombre_ligne = arg ['nombre_ligne']
        date_min = arg ['date_min']
        date_max = arg ['date_max']
        nombre_erreur = arg ['nombre_erreur']
        isPurge_existing_index = arg['isPurge_existing_index']
                       
        dico_evenements = self.lire_with_lock ()
        
        try:
            dico_alimentation = dico_evenements ['alimentation'] ['execution' ]
            dico_ajout = dico_alimentation  ['dico_ajout']
            ID_reference_depart, ID_reference_fin = dico_alimentation ["taille_globale"]

            if len(dico_ajout) == 0 :
                numero = 0
            else:
                liste_ajout = [nom_ajout for nom_ajout in dico_ajout.keys()]
                liste_ajout.sort()
                dernier_ajout = liste_ajout [len(liste_ajout) - 1]

                _ , numero = dernier_ajout.split ('_')
                numero = int(numero) + 1


            numero_string = ("0000000000000000000"+str(numero) ) [-10:] 
            name_ajout = "ajout_" + numero_string

            nombre_debut = ID_reference_fin
            nombre_fin = ID_reference_fin + nombre_ligne
            new_ajout = {}
            new_ajout ['numero_ligne_debut'] = nombre_debut
            new_ajout ['numero_ligne_fin'] = nombre_fin
            new_ajout ['date_execution'] = str(datetime.now())
            new_ajout ['date_min'] = date_min 
            new_ajout ['date_max'] = date_max
            new_ajout ['nombre_ligne'] = nombre_ligne
            new_ajout ['nombre_erreur'] = nombre_erreur
            new_ajout ['purge de la base'] = isPurge_existing_index
            new_ajout ['nom_alimentation'] = nom_alimentation

            dico_ajout [name_ajout] = new_ajout

            ID_reference_fin += nombre_ligne
            taille_globale = [ID_reference_depart, ID_reference_fin]

            dico_evenements ['alimentation'] ['execution' ] ['dico_ajout'] = dico_ajout
            dico_evenements ['alimentation'] ['execution' ] ['taille_globale'] = taille_globale
        except:
            raise
            pass
        
        self.ecrire_with_unlock (dico_evenements)
        
        return
        
        
