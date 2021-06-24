# coding: utf-8
import pandas as pd
import numpy as np
import json
from Alimentation_bloc import Alimentation_bloc

# pour calcul separateurs pour une variable
# manque la lecture des valeurs par Alimentation_bloc
# puis l'ecriture du dio_quantile dans /data/quantile/nom_variable +".json"
##


class Quantile ():
    """
    creation des dictionnaires pour chaque quantile demandé par une zone
    
    def __init__ (self, arg = 
            - arg_alimentation =
                  index_data, # mis dans doc_evenements 
                  nom_variable, # arg_kernel
                  ID_reference_min, # arg_alimentation
                  ID_reference_max, # arg_alimentation
                  taille_bloc # size pour search par bloc de kernel 
                  arg_kernel, # arg_kernel pour alimentation 
                  isValeur , # arg_alimentation
                  isID , # arg_alimentation
                  isTrace = False, # arg_alimentation
                  ID_reference_base = "000000000000000000000000000000", # arg_alimentation
                  
            pathDicoEvenements = "../data/dico_evenements.txt", # pour obtenir info data, task et system
            
            ce qui donne en simplifiant (voir arg_alimentation)
            
            arg = { 'arg_alimentation' : dico pour alimentation ,
                    'pathDicoEvenements' : "../data/dico_evenements.txt",
                    }
                  
                 ) :
        """
    def __init__(self, arg) :
        # initialisation des données pour calcul
        self.dataframe =  pd.DataFrame()
        
        # initialisation nom du quantile => liste des pas (pour calcul)
        self.dico = {}
        self.nombreSeparation = [4, 5 ,10, 20, 50, 100]
        self.nameSeparation = ['quartile', 'quintile', 'decile', 'vingtile', 'cinquantile', 'centile' ]
        
        for counter, valeur in enumerate  (self.nombreSeparation) :
            pas = 1.0/valeur
            r = np.array([i*pas for i in range(1, valeur)])
            nom = self.nameSeparation [counter]
            self.dico [nom] = r
            continue
            
        # lecture du dico evenements
        pathDicoEvenements = arg ['pathDicoEvenements']
        f = open (pathDicoEvenements, 'r')
        data = f.read()
        f.close()
        dico_evenements = json.loads (data)
        
        # initialisation de l'alimentation 
        arg_alimentation = arg # on a les variable d execution
                
        # parametres supplementaires et necessaire pour le contexte
        
        index_data = dico_evenements ['_index_data']
        arg_alimentation ['index_data'] = index_data
        
        taille_bloc = dico_evenements ['_taille_bloc']
        arg_alimentation ['taille_bloc'] = taille_bloc
        
        arg_alimentation ['isValeur'] = True
        arg_alimentation ['isID'] = False
        self.isTrace = arg ['isTrace']
        arg_alimentation ['isTrace'] = self.isTrace
        
        self.Alimentation = Alimentation_bloc (arg_alimentation)
        
        
        
        
        # on recupere dans dico_evenements les parametres pour cette variable
        
        nom_variable = arg_alimentation  ['nom_variable']
        creation_dictionnaire = dico_evenements ['creation_dictionnaire']
        travail = creation_dictionnaire [nom_variable]
        
        # verification
        if travail ['travail'] != 'quantile' :
            raise ValueError
        
        liste_calculs = travail ['parametres']
        self.listNom = []
        self.dicoNomManuel = {}
        for dico in liste_calculs :
            typeCalcul = dico ['type']
            
            if typeCalcul == 'manuel' :
                nom_manuel = dico ['nom_manuel']
                separateurs = dico ['separateurs']
                
                self.dicoNomManuel [nom_manuel] = separateurs
                
                self.listNom.append(nom_manuel)
                continue
            self.listNom.append(typeCalcul)
            continue
               
        return
    
    
    def bulk (self, ) :
        """
        recuperation de l'ensemble des donnes (generalisation du nom bulk pour appel generique)
        puis calcul et envoie des résultats
               
        """
        
        for taille, liste_valeurs in self.Alimentation.alimentation_bloc (" ") :
            liste_valeurs_float = [float(d) for d in liste_valeurs]
            self.put_data (liste_valeurs_float)
            continue
        
        
        
        return self.get_dico_quantile (listNom  = self.listNom , dicoNomManuel = self.dicoNomManuel)
            
        
        
    

     
            
    def put_data (self, liste) :
        # on recupere de facon incrementale les valeurs de data d'une zone pour calcul des separateurs
        self.dataframe = self.dataframe.append(liste, ignore_index = True)
        return
    
    def get_quantile (self, nomQuantile ) :
        # ressort une de valeurs croissantes qui sont les separateurs entre quantiles
        
        array = self.dico [nomQuantile]
        
            
        resultat = self.dataframe.quantile (array)
        
        array  = resultat.to_numpy()
        
        longueur = array.shape [0]
        
        return array.reshape (1,longueur).tolist()[0]
    
    def get_dico_quantile (self, listNom = None , dicoNomManuel = {}) :
        # nom manuel => liste separateur (parametres)
        
               
        resultat = {}
        for nom in listNom :
            if nom in dicoNomManuel :
                r = dicoNomManuel [nom]
            else :
                r = self.get_quantile (nom)
            resultat [nom] = r
            continue
        return resultat # => mis dans un fichier pour futur regroupement dans parametres travail pour cette zone
    

# pour calcul sous vecteur    
    
class CalculQuantile () :
    def __init__ (self, 
                      index_data,
                      nom_variable,
                      ID_reference_min,
                      ID_reference_max,
                      taille_bloc,
                      arg_kernel,
                      isValeur,
                      isID,
                      pathDicoSeparateurs = "../data/quantile/",
                      isPurge_existing_index = False,
                      isTrace = False,
                  
                        ) :
        
        """
        objectif :
        par Zone, par ID en utilisant la valeur de la zone 
           on emet autant de sous vecteur que de élément dans la liste (different vecteur dans le bulk)
                     
        structure sous vecteurs = {ID , 
                                   IDreferenceMin,
                                   IDreferenceMax ,
                                    nom_variable,
                                    type_sous_vecteur,
                                    sous_vecteur}
                                    
        type du sous vecteur = type du quantile ex quartile, centile ....pour cette variable
        
        warning : nom_sousvecteur permet de creer le vecteur globale : ensemble sous vecteur dans le bon ordre  
            
        """
        # on lit le dico_separateurs de la variable
        f = open (pathDicoSeparateurs + nom_variable +".json", "r")
        d = f.read ()
        self.dicoValeursSeparation = json.loads (d)
        
        # initialisation kernel
        self.kernel = Kernel (arg_kernel)
        
        # initialisation de l'alimentation
        isValeur = True
        isID = True
        isTrace = isTrace
        self.Alimentation = Alimentation_bloc (index_data,
                                                nom_variable,
                                                ID_reference_min,
                                                ID_reference_max,
                                                taille_bloc,
                                                arg_kernel,
                                                isValeur = isValeur,
                                                isID = isID,
                                                isTrace = isTrace,
                                                ID_reference_base = "000000000000000000000000000000")
        
        
        # dicoValeursSeparation dans data/quantile/nom_variable.json 
        self.listID = listeID
        self.nomVariable = nomVariable
        self.index_sous_vecteur = index_sous_vecteur
        self.isPurge_existing_index = isPurge_existing_index 
        
        
        
    def get_sous_vecteurs (self, ID) :
        
        resultat_all_quantile = {}
        for taille_lu, hists in self.alimentation.alimentation_bloc (ID) :
            
            for valeur in hists :
                
                for nom_quantile, separateurs in self.dicoValeursSeparation.values() :
                    sous_vecteur_unitaire = self._calcul_sous_vecteur (valeur, separateurs)
                    try :
                        sous_vecteur = resultat_all_quantile [nom_quantile]
                    except:
                        resultat_all_quantile [nom_quantile] = sous_vecteur_unitaire
                        continue
                    resultat_all_quantile [nom_quantile] = sous_vecteur_unitaire + sous_vecteur
                    continue
                continue
            continue
        return resultat_all_quantile
    
    def _calcul_sous_vecteur (self, valeur, separateurs) :
               
        #print ("valeur =", valeur)
        taille = len(separateurs) # taille separateur
        
        #print ("separateur =", separateur)
        comparateur = np.zeros(taille) + valeur
        #print ("comparateur =", comparateur)
        comparaison = np.invert(comparateur < separateurs)
        #print ("comparaison =",comparaison)
        position = comparaison.sum()
        #print ("position =", position)
        sous_vecteur = np.zeros (taille+1)
        sous_vecteur [position] = 1
        #print ("sous_vecteur =", sous_vecteur )
        return sous_vecteur
    
    
    
    def iterateur_sous_vecteurs_par_ID (self,) :
        """
        -on lit les blocs de valeurs sur cette ID et cette variable
        -si pas de valeurs , on ne fait rien
                sinon par valeur (attention init)
        on somme les sous vecteurs pour chaque quantile
        
        puis retourne l 'ensemble des dicos du sous vecteur de chaque quantile pour cet ID
        # on obtiend cette liste des quartiles dans le resultat de get_sous_vecteurs 
        """
        
        for ID in self.listeID :
            # pour chaque ID on yield chque dico representant un sous_vecteur
            resultat_all_quantile = self.get_sous_vecteurs (ID)
            for nom_quantile, sous_vecteur in resultat_all_quantile.values() :
                dico = {'ID' : ID ,
                        'IDreferenceMin' : self.ID_reference_min,
                        'IDreferenceMax' : self.ID_reference_max ,
                        'nom_variable' : self.nom_variable,
                         'type_sous_vecteur' : nom_quantile,
                         'sous_vecteur' : sous_vecteur.tolist(),
                       }
                yield dico
            continue
        return
        
    
    def bulk (self,) :
        
        self.kernel.bulk ( self.iterateur_sous_vecteurs_par_ID () ,
                          self.index_sous_vecteur,
                          isPurge_existing_index = self.isPurge_existing_index,
                          chunk_size = 2000,
                          )
        return
    
            
    
            
            
            
        
    
    

        


    


        
