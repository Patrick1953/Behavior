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
from Generic_simulation import Generic
import luigi

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Reunion import Reunion_paragraphe


    
    
class Execution_ID  (Generic) :
    """
    recoit dans arg 
    les paths (systeme et evenements)
    
    les parametres d'encadrement de la lecture dans l'index data
    
    renvoie un dico {'ID : ' } (calcul réalisé dans la classe calcul)
    
    warning creation quantile est supposée réalisé
    
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
        self.nom_tache_luigi = 'Execution_ID'
        etape = self.arg_travail_data ['etape']
        self.path = '../data/temp/' + etape + '/' + self.nom_tache_luigi + '/'
        validationPath (self.path)
        l = ['resultat_paragraphe', ]
             
        nom_file = self.path +  ('_'.join(l)) +'.json'
        
        return luigi.LocalTarget(nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        self.get_travail()
        message = "OK"
        dico_out = {}
        
        for i in range (0, self.nombre_appels) :
            
            with self.input() [i].open() as fin :
                data = fin.read()
                dico = json.loads (data)
                try:
                    dico_out = reunion_dico (dico, r_entree = dico_out)
                except Exception as e:
                    message = str(e)

            continue
            
        
        data = json.dumps ( dico_out)
        
        with self.output().open ('w') as fout :
            fout.write (data)
        
        return message
    
                
        
def reunion_dico (r, r_entree = {}) :
    for cle, liste in r.items () :
        try :
            liste_entree = r_entree [cle]
        except:
            liste_entree = []
        liste_entree.extend(liste)
        r_entree [cle] = liste_entree
        continue
    
    return r_entree
    
    
    
    
       
        
        
    
