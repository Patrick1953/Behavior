# coding: utf-8
import sys, os, json
import luigi

from Generic import Generic_simulation, Generic

path = "../Calcul"
if path not in sys.path : 
    sys.path.append (path)
from Calcul import Calcul
    
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from validationPath import validationPath




from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


    
    
class Creation_paragraphe  (Generic) :
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
        self.nom_tache_luigi = 'Creation'     
        self.path = self.arg_travail_data ['pathLuigi_file']
        validationPath (self.path)
        l = [
             self.arg_travail_data ['ID_min'],
             self.arg_travail_data ['ID_max'],
             self.arg_travail_data ['variable_min'].replace (':', '.').replace (' ', '_'),
             self.arg_travail_data ['variable_max'].replace (':', '.').replace (' ', '_'),
            ]
             
        self.nom_file = self.path +  ('_'.join(l)) +'.json'
        
        return luigi.LocalTarget(self.nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        self.get_travail()
        
        C = Calcul (self.arg_travail_data)
        r = C.calcul_paragraphe()
        
        
        
        with self.output().open('w') as f:
            self.ecrire_luigi_file (f, r)
            
        return '  OK  '
            
        
            
class Creation_paragraphe_simulation  (Generic_simulation) :
    """
    recoit dans arg 
    les paths (systeme et evenements)
    
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
        self.nom_tache_luigi = 'Creation'     
        self.path = self.arg_travail_data ['pathLuigi_file']
        validationPath (self.path)
        l = [
             self.arg_travail_data ['ID_min'],
             self.arg_travail_data ['ID_max'],
             self.arg_travail_data ['variable_min'].replace (':', '.').replace (' ', '_'),
             self.arg_travail_data ['variable_max'].replace (':', '.').replace (' ', '_'),
            ]
             
        self.nom_file = self.path +  ('_'.join(l)) +'.json'
        
        return luigi.LocalTarget(self.nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        self.get_travail()
        
        C = Calcul (self.arg_travail_data)
        r = C.calcul_paragraphe()
        
        
        
        with self.output().open('w') as f:
            self.ecrire_luigi_file (f, r)
            
        return 'OK'
        
     
    
        
        
        
    
