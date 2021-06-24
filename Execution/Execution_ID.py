# coding: utf-8
import sys, os, json

import luigi

from Reunion import Reunion_paragraphe

path = "../Calcul"
if path not in sys.path : 
    sys.path.append (path)
from Generic import Generic
    
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from validationPath import validationPath




from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Apprentissage_par_corpus import Apprentissage_par_corpus

    
    
class Execution_ID  (Generic) :
    """
    recoit dans arg 
    les dicos (systeme, evenements et embedding
    les parametres d'encadrement de la lecture dans les evenements
    
    sortie : fichier externe.
    ecrit sur une sortie externe la liste des ID concernés
    
    warning creation quantile est supposée réalisée
    
    """
    arg_travail = luigi.Parameter(default = "")
    
    
    def get_execution (self) :
        self.appels = {'appel' : Reunion_paragraphe,
                      'type_repetition' : 'ID',
                       }
        return 
        
    def output(self):
        # calcul le nom de l'output
        # et on realise le path si neccessaire
        self.get_travail()
        self.nom_tache_luigi = 'Execution'
        self.path = self.arg_travail_data ['pathLuigi_file']
        validationPath (self.path)
        self.nom_file = self.path + self.nom_tache_luigi  +'.json'
        validationPath (self.path)
        return luigi.LocalTarget(self.nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        self.get_travail()
        
        A = Apprentissage_par_corpus (self.arg_travail_data)
        A.init_corpus()

        for i in range (0, self.nombre_appels) :
            with self.input() [i].open() as fin :
                A.ecrire_luigi_file_random (fin)
        
        A.Apprentissage_par_corpus ()
        A.save_model ()
         
        with self.output().open ('w') as fout :
            fout.write ('OK')
                 
        
        return
    
                
        

    
    
    
    
       
        
        
    
