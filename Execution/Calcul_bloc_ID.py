# coding: utf-8
import sys, os, json
import luigi

from Generic import Generic_simulation, Generic
from Alimentation_ID_bloc import Alimentation_ID_bloc

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from validationPath import validationPath


def get_liste_bloc (arg) :
    dir_path = arg ['pathLuigi_file']
    pathFile = dir_path + 'Calcul_bloc_ID.json' 
    if os.path.exists (pathFile) :
        f = open (pathFile, 'r')
        data = f.read ()
        resultat = json.loads (data)
        nombre_ID = resultat.pop()
        resultat = resultat [0]
        return resultat, nombre_ID
    else:
        raise ValueError
    




class Calcul_bloc_ID  (Generic) :
    """
    recoit dans arg 
    les paths (systeme et evenements)
  
    les parametres d'encadrement de la lecture dans l'index data
    
    renvoie la liste de blocs qui encadre le calcul des paragraphes
    
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
        self.nom_tache_luigi = 'Calcul_bloc_ID'     
        self.path = self.arg_travail_data ['pathLuigi_file']
        validationPath (self.path)
        l = [
             self.nom_tache_luigi,
             
            ]
             
        self.nom_file = self.path +  ('_'.join(l)) +'.json'
        
        return luigi.LocalTarget(self.nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        
        self.get_travail()
        
        A = Alimentation_ID_bloc (self.arg_travail_data)
        resultat = A.get_liste_bornes_ID ()
              
         
        with self.output().open ('w') as fout :
            data = json.dumps (resultat)
            fout.write (data)
        
        return
    
    
    
        
        
            
            
        
            
            
            
