# coding: utf-8
import sys, os, json
path = "../Calcul"
if path not in sys.path : 
    sys.path.append (path)
    
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)

from validationPath import validationPath
from Calcul import Calcul
from Generic_simulation import Generic_simulation, Generic
import luigi

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

class Creation_paragraphe_simulation  (Generic_simulation) :
    """
    recoit dans arg 
    les paths (systeme et evenements)
    
    les parametres d'encadrement de la lecture dans l'index data
    
    renvoie un dico {'ID : ' } (calcul réalisé dans la classe calcul)
    
    warning creation quantile est supposée réalisé
    
    """
    #arg_travail = luigi.Parameter(default = "")
    
    
    def get_execution (self) :
        self.appels = {'appel' : None,
                      'type_repetition' : 'rien',
                       }
        return 
        
    def output(self):
        # calcul le nom de l'output
        # et on realise le path si neccessaire
        self.get_travail()
        self.nom_tache_luigi = 'Creation'
        etape = self.arg_travail_data ['etape']
        self.path = '../data/temp/' + etape + '/' + self.nom_tache_luigi + '/'
        
        validationPath (self.path)
        l = [
             self.arg_travail_data ['ID_min'],
             self.arg_travail_data ['ID_max'],
             self.arg_travail_data ['variable_min'],
             self.arg_travail_data ['variable_max'],
            ]
        
        
        nom_file = self.path +  ('|'.join(l)) +'.json'
        
        return nom_file  #luigi.LocalTarget("task.txt")
    
    
        
        
        
    def run_tache (self, ) :
        self.get_travail()
        
        C = Calcul (self.arg_travail_data)
        r = C.calcul_paragraphe()
        r = json.dumps (r)
        
        nom_file = self.output ()
        f = open (nom_file, 'w')
        f.write(r)
        f.close ()
            
        
        """remplacer par 
        with self.output().open('w') as f:
            f.write(r)
        """
    
    
class Creation_paragraphe  (Generic) :
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
        # et on realise le path si neccessaire
        self.get_travail()
        self.nom_tache_luigi = 'Creation'
        etape = self.arg_travail_data ['etape']
        self.path = '../data/temp/' + etape + '/' + self.nom_tache_luigi + '/'
        validationPath (self.path)
        l = [
             self.arg_travail_data ['ID_min'],
             self.arg_travail_data ['ID_max'],
             self.arg_travail_data ['variable_min'],
             self.arg_travail_data ['variable_max'],
            ]
             
        nom_file = self.path +  ('|'.join(l)) +'.json'
        
        return luigi.LocalTarget(nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        self.get_travail()
        
        C = Calcul (self.arg_travail_data)
        r = C.calcul_paragraphe()
        r = json.dumps (r)
        
        
        with self.output().open('w') as f:
            f.write(r)
            
        
            
        
        
    
    
        
        
        
    
