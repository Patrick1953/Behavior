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

from Sortie_vecteur import Sortie_vecteur
    
    
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
        self.appels = {'appel' : Sortie_vecteur,
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
        
        return luigi.LocalTarget(self.nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        self.get_travail()
        
        
        resultat = []
        for i in range (0, self.nombre_appels) :
            with self.input() [i].open() as fin :
                message = self.lire_luigi_file (fin)
                resultat.append (message)
                
         
        with self.output().open ('w') as fout :
            resultat_json = json.dumps (resultat)
            fout.write (resultat_json)
                      
        
        return
    
                
        

    
    
    
    
       
        
        
    
