# coding: utf-8
import sys, os, json
import luigi

from Generic import  Generic

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)

from validationPath import validationPath

path = "../Calcul"
if path not in sys.path : 
    sys.path.append (path)
    
from Sortie import Sortie



from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)




    
    
class Sortie_vecteur  (Generic) :
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
    
    ### warning equivallent à reunion_paragraphe à normaliser
    def output_fait_par_paragraphe(self):
        # calcul le nom de l'output de reunion_paragraphe pour ce bloc
        # et on realise le path si neccessaire
        self.get_travail()
        
        self.path = self.arg_travail_data ['pathLuigi_file']
        validationPath (self.path)
        l = [
             self.arg_travail_data ['ID_min'],
             self.arg_travail_data ['ID_max'],
        ]
            
             
        self.nom_file = self.path +  ('_'.join(l)) +'.json'
        
        return self.nom_file
    
    def output (self):
        # calcul le nom de l'output
        # et on realise le path si neccessaire
        self.get_travail()
        self.nom_tache_luigi = 'Sortie_vecteur'
        self.path = self.arg_travail_data ['pathLuigi_file']
        validationPath (self.path)
        l = [ self.nom_tache_luigi ,
             self.arg_travail_data ['ID_min'],
             self.arg_travail_data ['ID_max'],
        ]
            
            
        self.nom_file = self.path +  ('_'.join(l)) +'.json'
        
        return luigi.LocalTarget(self.nom_file)
    
    
        
        
        
    def run_tache (self, ) :
        self.get_travail()
        
         
        
        
            
        # dans self.nom_file on a le resultat de reunion_paragraphe sur ID_min, ID_max
        # lecture et ecriture des vecteurs en devrivant le bloc d'ID
        # on update le nom de sortie du resultat de reunion paragrapge
        nom_data = self.arg_travail_data  ['nom_data']
        l = [nom_data,
             self.arg_travail_data ['ID_min'],
             self.arg_travail_data ['ID_max'],
            ]
        nom_file = '_'.join (l) + '.json'
        self.arg_travail_data  ['nom_data'] = nom_file # modif ecriture sortie vecteur
        
        S = Sortie (self.arg_travail_data)
        S.init_ecriture ()
        # on prend l'output de reunion_paragraphe (format ligne json)
        fichier_paragraphe = self.output_fait_par_paragraphe()
        fin = open (fichier_paragraphe, 'r')
        S.ecrire_resultat (fin)
        S.close()
        
        with self.output().open ('w') as fout :
            fout.write ('OK pour:'+ self.nom_file)
            
        
        return message
    
                
        

    
    
    
    
       
        
        
    
