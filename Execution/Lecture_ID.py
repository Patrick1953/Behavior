# coding: utf-8
import sys, os, json
import luigi

from Generic import Generic_simulation, Generic
from Alimentation_ID_bloc import Alimentation_ID_bloc

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from validationPath import validationPath




class Lecture_ID  (Generic) :
    """
    recoit dans arg 
    les paths (systeme et evenements)
    y
    les parametres d'encadrement de la lecture dans l'index data
    
    renvoie un dico {'ID : ' } (calcul réalisé dans la classe calcul)
    
    warning creation quantile est supposée réalisé
    
    """
    arg_travail = luigi.Parameter(default = "")
    
    
    def get_execution (self) :
        self.appels = {'appel' : None,
                      'type_repetition' : 'rien',
                       }
        return
    
        
    def output(self):
        # calcul le nom de l'output
        
        self.get_travail()
        self.nom_tache_luigi = 'Lecture_ID'     
        self.path = self.arg_travail_data ['pathLuigi_file']
        validationPath (self.path)
        l = [
             self.nom_tache_luigi,
             self.arg_travail_data ['variable_min'].replace (':', '.').replace (' ', '_'),
             self.arg_travail_data ['variable_max'].replace (':', '.').replace (' ', '_'),
            ]
             
        self.nom_file = self.path +  ('_'.join(l)) +'.json'
        
        return luigi.LocalTarget(self.nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        
        self.get_travail()
        A = Alimentation_ID_bloc (self.arg_travail_data)
        resultat = A.get_liste_bornes_ID ()
               
        with self.output().open('w') as fout:
            data = json.dumps(resultat)
            fout.write(data)
        
            
        return
