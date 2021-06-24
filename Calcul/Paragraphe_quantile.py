# coding: utf-8
import pandas as pd
import numpy as np
import json, sys



from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Parametres import Parametres


class Paragraphe_quantile ()  :
    
    def __init__ (self, arg) :
        
        
        
        self.arg = arg
        
        self.dicoEvenements = Parametres ( arg ['pathDico_evenements'], [])
            
        # parametres necessaire pour creation sous vecteur Quantile
         
        self.dictionnaire = self.dicoEvenements ['dictionnaire']
        
        
    def calcul_sous_vecteur_quantile (self,nom_variable, ligne ) :
        
        """
        calcul des sous vecteur (on connait la dispertion)
        la variable est en mode quantile
        le format des dictionnaies pour une variable numerique (quantile)
        { nom_variable : {'type_quantile' : [separateurs ...],
                                'autre_type_quanrtile': [separateurs...]...,
                                }}
                                
        le format du mot par type de quantile = nom_variable_type_quantile_valeurNumeriqueResultat
        
        la phrase est l'ensemble de ces mots separés par un blanc
        """
        valeur = ligne [nom_variable]
        #print (self.dictionnaire, nom_variable )
        #print (self.dictionnaire [nom_variable], nom_variable )
        #modif (parametres)
        #print ("nom_variable:", nom_variable)
        #P (self.dictionnaire )
        #P (self.dictionnaire [nom_variable])
        parametres_variable = self.dictionnaire [nom_variable]
        
        liste_mot = []
        #print ('nom_variable:', nom_variable)
        #print ()
        #print ('self.dictionnaire:',self.dictionnaire)
        #print ()
        #print ('parametres_variable',parametres_variable)
        #print ()
        for dico_type_quantile in parametres_variable :
            #print ('dico_type_quantile',dico_type_quantile)
            
            nom_quantile = dico_type_quantile ['nom']
            try :
                separateurs = dico_type_quantile  ['separateurs']
            except :
                separateurs = []
                
            
            resultat = self._calcul_sous_vecteur (valeur, separateurs)
            mot = nom_variable + '_' + nom_quantile+'_'+ resultat
            liste_mot.append (mot)
            continue
        
        return liste_mot
    
    def _calcul_sous_vecteur (self,  valeur, separateurs) :
               
        #print ("valeur =", valeur)
        taille = len(separateurs) # taille separateur
        
        #print ("separateur =", separateur)
        comparateur = np.zeros(taille) + float(valeur)
        #print ("comparateur =", comparateur)
        comparaison = np.invert(comparateur < separateurs)
        #print ("comparaison =",comparaison)
        position = comparaison.sum()
        
        return str(int(position + 1))  # on evite le zero
    
    
