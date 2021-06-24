# coding: utf-8
import pandas as pd
import numpy as np
import json
from Alimentation_bloc import Alimentation_bloc
from nltk.tokenize import word_tokenize


from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

import sys
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Kernel_BE import Kernel
from Parametres import Parametres

from Paragraphe_string import Paragraphe_string
from Paragraphe_quantile import Paragraphe_quantile
from Paragraphe_date import Paragraphe_date
    





class Calcul () :
    """
    en entree
    
    arg = {}
    arg ['index_data'] = "data_fake"
    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 392
    arg ['ID_reference_sort'] = 'asc'

    arg ['taille_bloc'] = 10
    arg ['isID'] = False
    arg ['ID_min'] = ""
    arg ['ID_max']  = ""
    arg ['ID_sort']  = "asc"
    arg ['isVariable'] =  False
    arg ['nom_variableQuery'] = "date_evenements"
    arg ['variable_min'] = ""
    arg ['variable_max'] = ""
    arg ['variable_sort'] = "asc"
    arg['isTrace'] = True
    arg['arg_kernel'] = arg_kernel




    #  variable pour alimentation bloc
    
    arg['pathDico_evenements'] = "../data/dico_evenements_2.txt" #  dico direct
    
        
    """
    def __init__ (self, arg) :
        
        
        self.arg = arg
        dico_systeme = Parametres (arg ['pathDico_systeme'], [])
                
        self.arg_kernel = dico_systeme ['elasticsearch']
        self.kernel = Kernel (self.arg_kernel)
                
        self.dicoEvenements = Parametres ( arg ['pathDico_evenements'], [])
        
            
        # parametres necessaire pour creation sous vecteur Quantile
        
        self.creation_dictionnaire = self.dicoEvenements ['creation_dictionnaire']
        self.dictionnaire = self.dicoEvenements ['dictionnaire']
        #P(self.dictionnaire )
        
        
        # creation liste variables numerique (quantile)
        self.liste_nom_variable_quantile = []
        for  nom_variable  in self.creation_dictionnaire.keys() :
            travail = self.creation_dictionnaire [nom_variable] ['travail']
            if travail != 'quantile' :
                continue
            self.liste_nom_variable_quantile.append(nom_variable)
            continue
            
        
        # initialisation nom du quantile => liste des pas (pour calcul)
        dico = {}
        nombreSeparation = [4, 5 ,10, 20, 50, 100]
        nameSeparation = ['quartile', 'quintile', 'decile', 'vingtile', 'cinquantile', 'centile' ]
        
        for counter, valeur in enumerate  (nombreSeparation) :
            pas = 1.0/valeur
            r = np.array([i*pas for i in range(1, valeur)])
            nom = nameSeparation [counter]
            dico [nom] = r
            continue
        
        self.dico_parametres_creation_quantile = dico   
        self.isTrace = arg ['isTrace']
        
        self.ID = "" # dans cette structure de calcul, on regroupe les lignes = > paragraphe
                
        # on recupere dans self.dico_parametres_variable les parametres du calcul pour les variables
    
        self.dico_parametres_variable = {}
        for nom_variable in self.liste_nom_variable_quantile :
            
            travail = self.creation_dictionnaire [nom_variable]
            liste_calculs = travail ['parametres']
            listNom = []
            dicoNomManuel = {}
            for dico in liste_calculs :
                
                typeCalcul = dico ['type']
                if typeCalcul == 'manuel' :
                    nom_manuel = dico ['nom_manuel']
                    separateurs = dico ['separateurs']

                    dicoNomManuel [nom_manuel] = separateurs
                    listNom.append(nom_manuel)
                    continue
                listNom.append(typeCalcul)
                continue
            listNom_trie = sorted (listNom)
            
            self.dico_parametres_variable [nom_variable] = [listNom_trie, dicoNomManuel ]
            continue
        
        # pour alimenter le calcul d un vecteur
        
        self.liste_nom_variable = [nom_variable for nom_variable in self.dicoEvenements ['position'].keys() ]
        
        # pour calcul des sous vecteurs (sous paragraphe)
        self.Paragraphe_string = Paragraphe_string (arg)
        self.Paragraphe_quantile = Paragraphe_quantile (arg)
        self.Paragraphe_date = Paragraphe_date (arg)
        
        
        return
    
    def lecture_ligne (self,) :
        A = Alimentation_bloc (self.arg)
        for ligne in A.get_ligne(self.ID) :
            ID = ligne ['ID']
            yield ligne
            
    def calcul_paragraphe(self,) :
        """
        calcul d'un paragraphe pour un ID qui est donné par l'appel du main
                    -soit pour apprentissage du modele 
                    -soit pour calcul du vecteur de comportement de l'ID sur le pas
                                        (parametres à passer dans arg pour l'ID et pour le pas)
                                        
                
        
        
        
        calcul du paragraphe par ID sur ID_reference_min , ID_reference_max
        Warning l apprentissage calcul aussi sur tranche de temps pour obtenir
                des paragraphes compatibles avec l'inférence
        """
        
        paragraphe_ID = {}
              
        for ligne in self.lecture_ligne():
            
            ID = ligne ['ID']
            vecteur = self.calcul_vecteur (ligne)
            
            try :
                paragraphe = paragraphe_ID [ID]
            except:
                paragraphe = []
                
            paragraphe.extend (vecteur)
            paragraphe_ID [ID] = paragraphe
            
            
            continue
        
        return paragraphe_ID
    
    def calcul_vecteur (self, ligne ) :
        
        vecteur = []
        for nom_variable in self.liste_nom_variable :
            
            if nom_variable == 'ID' :
                continue
                        
            travail =  self.creation_dictionnaire [nom_variable] ['travail']
            if travail == 'quantile' :
                sous_vecteur = self.Paragraphe_quantile.calcul_sous_vecteur_quantile (nom_variable, ligne) # fait
            elif travail == 'analyse_mot' :
                sous_vecteur = self.Paragraphe_string.calcul_sous_vecteur_mot (nom_variable,ligne) #fait
            elif travail == 'date' :
                sous_vecteur = self.Paragraphe_date.calcul_sous_vecteur_date (nom_variable,ligne)
            else :
                createur = self.arg_kernel ['createur']
                etape =  "calcul_vecteur"
                message = "le travail pour la variable " + nom_variable + "est faux"
                self.kernel.log_error(createur, etape, message)
                sous_vecteur = ''
            
            vecteur.extend (sous_vecteur) 
            continue
             
        return vecteur
    
    
    
            
        
    
    
        
    
    
   

    
    
