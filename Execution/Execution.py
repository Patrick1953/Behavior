# coding: utf-8
import json, time, sys
from datetime import datetime

import luigi

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Calcul_bloc_ID import Calcul_bloc_ID, get_liste_bloc
from Execution_ID import Execution_ID
from Execution_sortie import  Execution_sortie

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
from detruirePath import detruirePath

class Execution () :
    
    def __init__ (self, arg) :
        
        self.arg = arg
        
    def run (self,) :
        
        E = Execution_calcul (self.arg)
        resultat = E.run()
        
        M = Mise_a_jour_execution (self.arg)
        M.run (resultat)
        
        dir_path = resultat ['sortie']
        detruirePath (dir_path)
        
        return
    
    


class Execution_calcul () :
    
    def __init__ (self, arg_parametres) :
        
        self.arg_parametres = arg_parametres
        self.nom_tache_execution = arg_parametres ['nom_tache_execution']
        
    def run (self,) :
        
        
        arg = {}


        #  variable pour alimentation bloc_date

        arg ['ID_reference_min'] = 0
        arg ['ID_reference_max'] = 1000000000
        arg ['ID_reference_sort'] = None
        arg ['isReference'] = False






        arg ['isVariable'] =  True
        arg ['nom_variableQuery'] = "date_evenement"
        
        self.variable_min = self.arg_parametres ['date_min'] #'2021-02-01 00:00:00.000'
        arg ['variable_min'] = self.variable_min
        
        self.variable_max = self.arg_parametres ['date_max'] #'2021-02-01 00:00:00.000'
        arg ['variable_max'] = self.variable_max
        
        arg ['variable_sort'] = None

        arg ['isID'] = False
        arg ['ID_min'] = ""# avec
        arg ['ID_max']  = ""
        arg ['ID_sort']  = 'asc'

        arg ['isTrace'] = False


        

        nom_environnement = self.arg_parametres ['nom_environnement']
        arg ['nom_environnement'] = nom_environnement 


        pathFile_evenements = 'dico_evenements_2.json'
        pathFile_systeme = 'dico_systeme_2.json'
        path = '../data/' + nom_environnement + '/parametres/'
        
        arg_entree_sortie_lock = {} 
        arg_entree_sortie_lock['pathFile'] = path + pathFile_evenements
        Entree_sortie_evenements = Entree_sortie_lock (arg_entree_sortie_lock)
        
        
        self.dico_evenements = Entree_sortie_evenements.lire_with_lock ()
        Entree_sortie_evenements.unlock_lire()
        arg ['pathDico_evenements'] = self.dico_evenements
        
        arg_entree_sortie_lock = {}
        arg_entree_sortie_lock ['pathFile'] = path + pathFile_systeme
        Entree_sortie_systeme = Entree_sortie_lock (arg_entree_sortie_lock)
        dico_systeme = Entree_sortie_systeme.lire_with_lock ()
        Entree_sortie_systeme.unlock_lire ()
        arg ['pathDico_systeme'] = dico_systeme

        self.pas = self.arg_parametres ['pas']
               
        pas_date = self.variable_max.replace (':', '.').replace (' ', '_')
        
        directory_de_travail = '../data/' + nom_environnement + '/data/' + self.pas + '/' + pas_date + '/'
        arg ['pathLuigi_file'] = directory_de_travail

        arg['pathModele'] = '../data/test/data/'+ self.pas + '/' +'Modele_test2.model'

        arg ['Path_corpus']  = directory_de_travail + 'mon_corpus.txt'
        
        arg_json = json.dumps(arg)
              
        
        luigi.build([Calcul_bloc_ID (arg_travail = arg_json)],
                 workers= 1, local_scheduler = True)
        
        
        
        liste_blocs_ID, nombre_ID = get_liste_bloc (arg)
        
             
        
        arg ['nombre_ID'] = nombre_ID
        arg ['liste_blocs_ID'] = liste_blocs_ID
        
        workers = self.arg_parametres ['workers']
        local_scheduler = self.arg_parametres ['local_scheduler']
        
        arg_json = json.dumps (arg)
    
        
        luigi.build([Execution_ID (arg_travail = arg_json)],
                 workers= workers, local_scheduler = local_scheduler)
        
        
        parametres = self.dico_evenements ['environnement']  ['parametres_ecriture']
        arg ['parametres'] = parametres
        path_data = self.pas + '/' + pas_date + '/'
        arg ['nom_data'] = path_data  + 'vecteurs' # nom reel construit par bloc d 'ID'
        
        arg_json = json.dumps (arg)
        
        luigi.build([Execution_sortie (arg_travail = arg_json)],
                 workers= workers, local_scheduler = local_scheduler)
        
        
        
        resultat = {}
        resultat ['pas'] = self.pas
        resultat ['date_min'] = self.variable_min
        resultat ['date_max'] = self.variable_max
        resultat ['sortie'] = arg ['pathLuigi_file']
        resultat ['nom_tache_execution'] = self.nom_tache_execution
        
        return resultat
        

    
class Mise_a_jour_execution (Entree_sortie_lock) :
    
    def __init__ (self, arg) :
        
        nom_environnement = arg ['nom_environnement']
        l = nom_environnement.split('|')
        nom_environnement_local = l [0]
        pathFile_evenements = 'dico_evenements_2.json'
        pathFile = '../data/'+ nom_environnement_local + '/parametres/' + pathFile_evenements
        arg_Entree_sortie_lock = {}
        arg_Entree_sortie_lock ['pathFile'] = pathFile
        super().__init__(arg_Entree_sortie_lock)
        
        
    def run (self, resultat):
        
        self.pas = resultat ['pas']
        self.date_min = resultat ['date_min'] 
        self.date_max = resultat ['date_max'] 
        self.sortie = resultat ['sortie']
        self.nom_tache_execution = resultat ['nom_tache_execution']
        self.dico_evenements = self.lire_with_lock ()
        self.insertion_info ()
        self.ecrire_with_unlock (self.dico_evenements)
        
    def creation_info(self,) :
        dico = {}
        dico ['date_min'] = self.date_min
        dico ['date_max'] = self.date_max
        dico ['date_creation'] = str(datetime.now())
        dico ['sortie'] = self.sortie
        dico ['nom_tache_execution'] = self.nom_tache_execution
        return dico
    
    def insertion_info (self,) :
        

        try:
            x = self.dico_evenements ['pas']  [self.pas] 
        except:
            self.dico_evenements ['pas'][self.pas] = {'liste_execution' : []}
        
        try:
            liste_execution = self.dico_evenements ['pas']  [self.pas] ['liste_execution']
        except:
            self.dico_evenements ['pas'][self.pas] = {'liste_execution' : []}
            liste_execution = []
            
        
        isNew = True
        liste_execution_new = []
        for dico_info in liste_execution :
            if dico_info ['date_min'] == self.date_min and dico_info ['date_max'] == self.date_max :
                dico_info ['date_creation'] = str(datetime.now())
                isNew = False
                liste_execution_new.append(dico_info)
                continue
            liste_execution_new.append(dico_info)
            continue
        
        if isNew :
            new_info = self.creation_info()
            liste_execution_new.append(new_info)
        
        self.dico_evenements ['pas']  [self.pas] ['liste_execution'] =  liste_execution_new
        
        return
        
        
        
        
        
        
        
