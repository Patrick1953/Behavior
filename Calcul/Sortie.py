# coding: utf-8
import json, sys

from Embedding import Embedding

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Sortie_fichier import Sortie_fichier

class Sortie (Sortie_fichier) :
    
    def __init__ (self, arg) :
        
        super().__init__ (arg)
        
        self.embedding = Embedding (arg)
        
        
        
    def ecrire_resultat (self, fin) :
        
        for data in fin :
            dico = json.loads (data)
            ID = [cle for cle in dico.keys()] [0]
            paragraphe = dico [ID]
            vecteur = self.embedding.infer_vecteur_embedding (paragraphe)
            dico_out = {}
            dico_out ['words'] = paragraphe
            dico_out  ['vector'] = vecteur.tolist()
            dico [ID] = dico_out
            self.ecrire (json.dumps (dico))
        fin.close()
        return
