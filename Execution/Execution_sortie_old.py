# coding: utf-8
import sys, os, json

import luigi



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

from Sortie import Sortie
from Reunion import Reunion_paragraphe
    
    
class Execution_sortie  (Generic) :
    """
    recoit dans arg 
    les dicos (systeme, evenements et embedding
    les parametres d'encadrement de la lecture dans les evenements
    
    sortie : fichier externe des resultats.
       
    warning l apprentissage sur data (execution_ID) doit etre réalisé
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
        self.nom_tache_luigi = 'Sortie'
        self.path = self.arg_travail_data ['pathLuigi_file']
        validationPath (self.path)
        self.nom_file = self.path + self.nom_tache_luigi  +'.json'
        validationPath (self.path)
        return luigi.LocalTarget(self.nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        self.get_travail()
        
        S = Sortie (self.arg_travail_data)
        S.init_ecriture ()

        for i in range (0, self.nombre_appels) :
            with self.input() [i].open() as fin :
                S.ecrire_resultat (fin)
        
        S.close()
         
        with self.output().open ('w') as fout :
            fout.write ('OK_sortie')
                 
        
        return
    
                
        

    
    
    
    
       
        
        
    
