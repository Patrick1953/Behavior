# coding: utf-8
import sys, os, json
import luigi

from Generic import Generic_simulation, Generic


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)

from validationPath import validationPath




from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Creation import Creation_paragraphe


    
    
class Reunion_paragraphe  (Generic) :
    """
    recoit dans arg 
    les paths (systeme et evenements)
    
    les parametres d'encadrement de la lecture dans l'index data
    
    renvoie un dico {'ID : ' } (calcul réalisé dans la classe calcul)
    
    warning creation quantile est supposée réalisé
    
    """
    arg_travail = luigi.Parameter(default = "")
    
    
    def get_execution (self) :
        self.appels = {'appel' : Creation_paragraphe,
                      'type_repetition' : 'date_evenement',
                       }
        return 
        
    def output(self):
        # calcul le nom de l'output
        # et on realise le path si neccessaire
        self.get_travail()
        self.nom_tache_luigi = 'Reunion'
        self.path = self.arg_travail_data ['pathLuigi_file']
        validationPath (self.path)
        l = [
             self.arg_travail_data ['ID_min'],
             self.arg_travail_data ['ID_max'],
        ]
            
             
        self.nom_file = self.path +  ('_'.join(l)) +'.json'
        
        return luigi.LocalTarget(self.nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        self.get_travail()
        message = "OK"
        dico_out = {}
        
        for i in range (0, self.nombre_appels) :
            
            with self.input() [i].open() as fin :
                dico = self.lire_luigi_file(fin)
                try:
                    dico_out = reunion_dico (dico, r_entree = dico_out)
                except Exception as e:
                    message = str(e)

            continue
            
        
        
        
        with self.output().open ('w') as fout :
            self.ecrire_luigi_file (fout, dico_out)
            
        
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
    
    
    
    
       
        
        
    
