# coding: utf-8
import json, sys
from nltk.tokenize import word_tokenize



from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Parametres import Parametres

class Paragraphe_string () :
    
    def __init__ (self, arg) :
        
        
        
        self.arg = arg
        self.dicoEvenements = Parametres ( arg ['pathDico_evenements'], [])
            
        
        
        self.dictionnaire = self.dicoEvenements ['dictionnaire']
        
    
    
    def calcul_sous_vecteur_mot (self,
                                 nom_variable,
                                 ligne,
                                 
                                
                                ) :
               
        texte = ligne [nom_variable]
        
        parametres_variable = self.dictionnaire [nom_variable] ['parametres']
        resultat = []      
        for dico_type_mot in parametres_variable :
            
            nom_type_calcul = dico_type_mot ['type']
            if nom_type_calcul == 'standard' :
                liste_mot = self.paragraphe_standard (texte)
                
            else:
                raise Value_error ('pas existant')
            resultat.extend(liste_mot)
            continue
               
        return resultat
                
            
    def paragraphe_standard (self, texte, 
                            ):
        liste_mot = self.lemmatizer (texte,)
        
        return liste_mot
    
    def lemmatizer (self, texte, ponctuation = {"." : None,
                                            "'" : None,
                                            '?' : None,
                                            '-' : None,
                                            ";" : None,
                                            '(' : None,
                                            ')' : None,
                                            '#' : None,
                                            '=' : None,
                                            '!' : None,
                                            '&' : None,
                                            '*' : None,
                                            '@' : None,
                                            '%' : None,
                                            '"' : None,
                                            '+' : None,
                                            "/" : None,
                                            "\\": None,
                                            "^" : None,
                                            "<" : None,
                                            ">" : None,
                                            '0' : None,
                                            '1' : None,
                                            '2' : None,
                                            '3' : None,
                                            '4' : None,
                                            '5' : None,
                                            '6' : None,
                                            '7' : None,
                                            '8' : None,
                                            '9' : None,                                              

                                           },
                    ) :
        
        
        """
        ###################### amelioration possible #################
        
        prendre le mot comme une phrase que l on peut transformer en vecteur 
        ce model doit dependre de la variable (mis dans la directory model avec son nom-variable)
        le vecteur calcule devient un mot de l'embedding global
              
        """
        texte = texte.lower ()
        for caractere in ponctuation.keys() :
            texte = texte.replace (caractere, ' ')
        resultat = texte.split()
                      
        return resultat
        
