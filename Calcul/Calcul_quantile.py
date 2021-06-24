# coding: utf-8
import pandas as pd
import json, copy
import pandas as pd
import numpy as np


from Alimentation_bloc import Alimentation_bloc

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

import sys
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Parametres import Parametres


class Description_travail_quantile () :
    
    def __init__ (self,) :
        
        
        dico = {}
        nombreSeparation = [4, 5 ,10, 20, 50, 100]
        nameSeparation = ['quartile', 'quintile', 'decile', 'vingtile', 'cinquantile', 'centile' ]
        self.nameSeparation = copy.copy (nameSeparation) # effet de bord
        self.nameSeparation.append('manuel')
        
        for counter, valeur in enumerate  (nombreSeparation) :
            pas = 1.0/valeur
            r = np.array([i*pas for i in range(1, valeur)])
            nom = nameSeparation [counter]
            dico [nom] = r
            continue
        self.dico_parametres_creation_quantile = dico
        
    def get_liste_travail_quantile (self,) :
        return self.nameSeparation
        
        


class Calcul_quantile (Description_travail_quantile) :
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
        
        
        
        super ().__init__  ()       
        
        self.arg = arg
        self.dicoEvenements = Parametres ( arg ['pathDico_evenements'], [])
        self.creation_dictionnaire = self.dicoEvenements ['creation_dictionnaire']
        
        # creation liste variables numerique (quantile)
        self.liste_nom_variable_quantile = []
        for  nom_variable  in self.creation_dictionnaire.keys() :
            travail = self.creation_dictionnaire [nom_variable] ['travail']
            if travail != 'quantile' :
                continue
            self.liste_nom_variable_quantile.append(nom_variable)
            continue
            
        
        
        
        
        
        """ Init réalisé par calcul ... suffisant
        self.arg = arg
        dico_systeme = Parametres (arg ['pathDico_systeme'], [])
             
        
        self.arg_kernel = dico_systeme ['elasticsearch']
        self.kernel = Kernel (self.arg_kernel)
        
        
        
        self.dicoEvenements = Parametres ( arg ['pathDico_evenements'], [])
        #P (arg ['pathDico_evenements'])
        #print ('apres Parametres')
        #P(self.dicoEvenements.dicoComplet)
        #print()
            
        # parametres necessaire pour creation Quantile et calcul Quantile
        
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
            #print (self.creation_dictionnaire)
            travail = self.creation_dictionnaire [nom_variable]
            liste_calculs = travail ['parametres']
            listNom = []
            dicoNomManuel = {}
            for dico in liste_calculs :
                #print (dico)
                typeCalcul = dico ['type']
                if typeCalcul == 'manuel' :
                    nom_manuel = dico ['nom_manuel']
                    separateurs = dico ['separateurs']

                    dicoNomManuel [nom_manuel] = separateurs
                    listNom.append(nom_manuel)
                    continue
                listNom.append(typeCalcul)
                continue
            #print (listNom)
            listNom_trie = sorted (listNom)
            #print (listNom_trie)
            self.dico_parametres_variable [nom_variable] = [listNom_trie, dicoNomManuel ]
            continue
            
        # pour alimenter le calcul d un vecteur
        
        self.liste_nom_variable = [nom_variable for nom_variable in self.dicoEvenements ['position'].keys() ]
        """
        
        return
    
    def lecture_ligne (self,) :
        A = Alimentation_bloc (self.arg)
        for ligne in A.get_ligne(None) :
            yield ligne
    
              
            
            
    def creation_dataframe (self,) :
        """
        
        en utilisant liste_variable quantile, 
        boucle sur les lignes de min max sur l'ensemble de la profondeur
                prendre les valeurs des variables numeriques mis dans dictionnaires
                en creant un bloc de valeurs mettre dans le df
                continue
        
                
        
        
        """
         
        
        
        
        dico_alimentation = {}  
        for ligne in self.lecture_ligne():
            for nom_variable in self.liste_nom_variable_quantile :
                try :
                    liste = dico_alimentation [nom_variable]
                except:
                    liste = []
                valeur = ligne [nom_variable]
                valeur = float(ligne [nom_variable])
                liste.append (valeur)
                dico_alimentation [nom_variable] = liste
                continue
        
        
        self.dataframe = pd.DataFrame(dico_alimentation)
            
        return
    
    
    
    
    def creation_quantile (self, ) :
        
        # pour chaque type de quantile dans creation_dictionnaire
        # calculer les parametres et mettre le resultat dans dicoEvenements 
        #
        self.creation_dataframe ()
        dico_quantile = {}
        for nom_variable in self.liste_nom_variable_quantile :
            parametres_creation_quantile = self.creation_dictionnaire [nom_variable]
            liste_calcul_demande = parametres_creation_quantile ['parametres']
            liste_resultat_variable = []
            for type_calcul in liste_calcul_demande :
                nom_calcul = type_calcul ['type']
                if nom_calcul == 'manuel' :
                    nom = type_calcul ['nom_manuel']
                    separateurs = type_calcul ['separateurs']
                else :
                    separateurs =  self.get_quantile ( nom_calcul, nom_variable)
                    nom = nom_calcul
                liste_resultat_variable.append ({'nom': nom, 'separateurs' : separateurs})
                continue
            dico_quantile [nom_variable] = liste_resultat_variable
            continue
            
        # on enregistre dans dicoEvenements_general deprecated
        """
        self.dicoEvenements ['dictionnaire'] = dico_quantile
        # on sauve ne fait rien
        
        self.dicoEvenements.save ( )
        """
        
        return dico_quantile
    
    def get_quantile (self, nomQuantile, nom_variable) :
        # ressort une de valeurs croissantes qui sont les separateurs entre quantiles
        # ppouyr cette variable et ce quantile
        array = self.dico_parametres_creation_quantile [nomQuantile]
        resultat = self.dataframe[nom_variable].quantile (array)
        array  = resultat.to_numpy()
        longueur = array.shape [0]
        return array.reshape (1,longueur).tolist()[0]
    
