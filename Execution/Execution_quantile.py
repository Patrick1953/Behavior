# coding: utf-8
from datetime import datetime
import json

import sys
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Kernel_BE import Kernel

path = "../Calcul"
if path not in sys.path : 
    sys.path.append (path)
from Parametres import Parametres
from Calcul_quantile import Calcul_quantile

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

class Execution_quantile ():
    def __init__ (self,arg):
        """
        deroulement :
        initialisation de dictionnaire ( copie de creation_dictionnaire dans dictionnaire )
        initialisation des parametres necessaire au calcul quantile ie profondeur(parametres)
        
        permet en utilisant Calcul:
            de recuperer les valeurs des variables numeriques
            de calculer les quantiles (en suivant les parametres dans dico_evenements (creation_dictionnaire)
            de mettre à jour ou creer les parametres de calcul (separateurs) dans dictionnaire
        
        Remarque :
        ce calcul se realise sur une profondeur donnée par ID_reference_min , ID_reference_max
        il se realise en une seule passe sur l'ensembles des lignes mais par bloc pour laisser respirer
            elasticsearch
        Pas de methode pour mieux paralleliser (principe mathematique du quantile)
        
        """
        try :
            self.arg = arg
            self.dico_syteme = arg ['pathDico_systeme']
            self.arg_kernel = self.dico_syteme ['elasticsearch']
            self.kernel = Kernel (self.arg_kernel)
            
            self.dico_evenements = arg ['pathDico_evenements']
            
        except Exception as e:
            try:
                
                createur = self.arg_kernel ['createur']
                etape =  "Init Learning task"
                message = "Bad parameters "
                message += str(datatime.now()) + ": " + str(e)
                self.kernel.log_error(createur, etape, message)
            except Exception as e:
                message = "ERROR kernel.log_error FAILED in "
                raise  ValueError (message)
        
                
        
            
                
            
        
        
    def run (self,) :
        
        try :
            # copie 'creation_dictionnaire' => 'dictionnaire' pour preparation du calcul
            # on recoit les dico evenements et sysyteme
            
            creation_dictionnaire  = self.dico_evenements ['creation_dictionnaire']
            self.dico_evenements ['dictionnaire'] = creation_dictionnaire
            
            self.arg ['pathDico_evenements'] = self.dico_evenements 
            
            #  variable pour alimentation bloc dans calcul Quantile 
            # 1000 milliard de lignes dans le temps si necessaire (precaution)
            self.arg ['isTrace'] = False
                      
            self.arg ['variable_sort'] = 'asc' # pour l'instant inused
            
            self.arg ['ID_reference_min'] = 0
            self.arg ['ID_reference_max'] = 100000000
            self.arg ['ID_reference_sort'] = 'asc'
            self.arg ['isReference'] = False
            
            self.arg ['isID'] = False
            self.arg ['ID_min'] = "couple_cadre_0"
            self.arg ['ID_max']  = "couple_cadre_1"
            self.arg ['ID_sort']  = None
            
            self.arg ['isVariable'] =  True
            self.arg ['nom_variableQuery'] = "date_evenement"
            #arg ['variable_min'] = '2021-02-01 00:00:00' #fourni par l'appellant
            #arg ['variable_max'] = '2021-03-30 00:00:00' 
            self.arg ['variable_sort'] = 'asc' # pour l'instant inused
                   
            
            C = Calcul_quantile (self.arg)
            new_dictionnaire = C.creation_quantile ()
            
            self.dico_evenements ['dictionnaire'] = new_dictionnaire
            
            # on renvoie le parametres de la reception
            return self.dico_evenements
            
            
        
        except Exception as e:
            raise
            try:
                
                createur = self.arg_kernel ['createur']
                etape =  "Init Learning task"
                message = "Bad parameters "
                message += str(datatime.now()) + ": " + str(e)
                self.kernel.log_error(createur, etape, message)
            except Exception as e:
                message = "ERROR kernel.log_error FAILED"
                raise  ValueError (message)
            
        
        return None
    

        
        
        
