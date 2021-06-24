# coding: utf-8
import sys
from datetime import datetime

from Calcul_quantile import Calcul_quantile

path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

class Apprentissage () :
    
    def __init__ (self, arg) :
        
        self.arg = arg
        
    def run (self,) :
        
        A = Apprentissage_calcul (self.arg )
        resultat = A.run()
        
        
        
        M = Mise_a_jour_apprentissage (self.arg)
        M.run (resultat)
        


class Apprentissage_calcul () :
    
    def __init__ (self, arg_entree) :
        
        
        self.nom_tache_apprentissage = arg_entree ['nom_tache_apprentissage']
        
        arg = {}
        arg ['isTrace'] = arg_entree['isTrace']
        nom_environnement = arg_entree ['nom_environnement']
        
        
        pathFile_evenements = 'dico_evenements_2.json'
        pathFile_systeme = 'dico_systeme_2.json'
        
        self.path = '../data/' + nom_environnement +'/parametres/'
        
        arg_entree_sortie_lock = {} 
        
        arg_entree_sortie_lock['pathFile'] = self.path + pathFile_evenements
        self.Entree_sortie_evenements = Entree_sortie_lock (arg_entree_sortie_lock)
        
        self.dico_evenements = self.Entree_sortie_evenements.lire_with_lock()
        self.Entree_sortie_evenements.unlock_lire()
        arg ['pathDico_evenements'] = self.dico_evenements
        
        
        arg_entree_sortie_lock ['pathFile'] = self.path + pathFile_systeme
        Entree_sortie_systeme = Entree_sortie_lock (arg_entree_sortie_lock)
        dico_systeme = Entree_sortie_systeme.lire_with_lock()
        Entree_sortie_systeme.unlock_lire()
        arg ['pathDico_systeme'] = dico_systeme
             
             
        

        #  variable pour alimentation bloc dans calcul quantile

        arg ['ID_reference_min'] = 0
        arg ['ID_reference_max'] = 100000000
        arg ['ID_reference_sort'] = 'asc'
        arg ['isReference'] = False

        arg ['isVariable'] =  True
        arg ['nom_variableQuery'] = "date_evenement"
        arg ['variable_min'] = arg_entree ['date_min'] # '2021-02-01 00:00:00'
        self.variable_min = arg_entree ['date_min']
        arg ['variable_max'] = arg_entree ['date_max'] # '2021-03-30 00:00:00'
        self.variable_max = arg_entree ['date_max']
        arg ['variable_sort'] = 'asc' # pour l'instant inused

        arg ['isID'] = False
        arg ['ID_min'] = ""
        arg ['ID_max']  = ""
        arg ['ID_sort']  = None
        self.C =  Calcul_quantile (arg)    
             
    def run (self,) :
        resultat = self.C.creation_quantile ()
        resultat ['date_min'] = self.variable_min
        resultat ['date_max'] = self.variable_max
        resultat ['nom_tache_apprentissage'] = self.nom_tache_apprentissage
        return resultat
        
        
    
class Mise_a_jour_apprentissage (Entree_sortie_lock) :
    
    def __init__ (self, arg) :
        
        nom_environnement = arg ['nom_environnement']
        l = nom_environnement.split('|')
        nom_environnement_local = l [0]
        pathFile_evenements = 'dico_evenements_2.json'
        pathFile = '../data/'+ nom_environnement_local + '/parametres/' + pathFile_evenements
        arg_Entree_sortie_lock = {}
        arg_Entree_sortie_lock ['pathFile'] = pathFile
        
        super().__init__(arg_Entree_sortie_lock) 
        
        
    def run (self, resultat) :
        
        self.date_min = resultat ['date_min']
        self.date_max =  resultat ['date_max']
        self.nom_tache_apprentissage = resultat ['nom_tache_apprentissage']
        self.dico_evenements = self.lire_with_lock()
        
        
        dictionnaire = self.dico_evenements ['dictionnaire']
        for nom_variable, valeur_quantile in resultat.items() :
            dictionnaire [nom_variable] = valeur_quantile
               
        self.dico_evenements ['dictionnaire'] = dictionnaire
        self.insertion_info ()
            
        self.ecrire_with_unlock (self.dico_evenements)
        
        return
    
    def creation_info(self,) :
        dico = {}
        dico ['date_min'] = self.date_min
        dico ['date_max'] = self.date_max
        dico ['date_creation'] = str(datetime.now())
        dico ['nom_tache_apprentissage'] = self.nom_tache_apprentissage
        return dico
    
    def insertion_info (self,) :

        try:
            liste_execution = self.dico_evenements ['apprentissage'] ['liste_execution']
        except:
            self.dico_evenements ['apprentissage'] = {'liste_execution' : []}
            liste_execution = []
            
        
        isNew = True
        liste_execution_new = []
        for dico_info in liste_execution :
            date_creation = str(datetime.now())
            if dico_info ['date_min'] == self.date_min and dico_info ['date_max'] == self.date_max :
                dico_info ['date_creation'] = date_creation
                dico_info ['nom_tache_apprentissage'] = self.nom_tache_apprentissage
                isNew = False
                liste_execution_new.append(dico_info)
                continue
            liste_execution_new.append(dico_info)
            continue
        
        if isNew :
            new_info = self.creation_info()
            liste_execution_new.append(new_info)
        
        self.dico_evenements ['apprentissage'] ['liste_execution'] =  liste_execution_new
        
        return
            
            
        
    
    
        
