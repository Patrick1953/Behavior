# coding: utf-8
import sys

path = "../outils"
if path not in sys.path :
    sys.path.append (path)
    
from Entree_fichier import Entree_fichier

class Kernel_entree () :
    """
    fournit le lecteur d'entree
    """
    
    def __init__ (self, arg) :
        
        """
        arg : 
        {'parametres_lecture' : {'path_fichier' : '../data/alimentation/evenements.txt',
                                                    'separateur' : "|", },
        'parametres_execution' : {'type_lecteur' : 'fichier',},
                                },
        
        """
        
        
        
        
        class_lecteurs = {'fichier' : Entree_fichier ,}
        
        
        parametres_execution = arg  ['parametres_execution']
        type_lecteur = parametres_execution ['type_lecteur']
                
        class_lecteur = class_lecteurs  [type_lecteur]
        
        self.lecteur = class_lecteur (arg)
        
    def init_lecture (self,) :
        self.lecteur.init_lecture ()
        
    def readIterator (self,) :
        return self.lecteur.readIterator ()
        
    def close (self,) :
        self.lecteur.close()
        

        
        
        
        
        
        
        
        
        
