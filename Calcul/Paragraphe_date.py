# coding: utf-8
import pandas as pd
import numpy as np
import json, sys
from datetime import datetime

from Calcul_date import Calcul_date

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Parametres import Parametres


class Paragraphe_date ()  :
    
    def __init__ (self, arg) :
        
        
        
        
        self.arg = arg
        self.dicoEvenements = Parametres ( arg ['pathDico_evenements'], [])
            
        # parametres necessaire pour creation sous vecteur Quantile
        self.dictionnaire = self.dicoEvenements ['dictionnaire']
        
        C = Calcul_date ()
        self.calcul_dates = C.get_calcul_dates ()
        
        dico_systeme = Parametres ( arg ['pathDico_systeme'], [])
        self.format_date_standard = dico_systeme ['calcul'] ['format_date_standard']
        
    def calcul_sous_vecteur_date (self, nom_variable, ligne) :
        
        date_string = ligne [nom_variable]
        date = datetime.strptime(date_string, self.format_date_standard)
        
        parametres_variable = self.dictionnaire [nom_variable] ['parametres']
        resultat = []
        for dico_type_date in parametres_variable :
                      
            try :
                nom_type_calcul = dico_type_date ['type']
                
                calcul_date = self.calcul_dates [nom_type_calcul]
            except :
                raise ValueError ('pas existant')
            
            mot = calcul_date (date)
             
                        
            resultat.append(nom_variable + '_' + mot)
            continue
               
        return resultat
