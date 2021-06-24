# coding: utf-8
import random, json
from pathlib import Path
from Embedding import Embedding

class Apprentissage_par_corpus(Embedding) :
    
    def __init__ (self, arg) :
        
        # init embedding
        super().__init__ (arg)
        
        # echantillonnage
        nombre_ID = arg ['nombre_ID']
        nombre_ID_pour_apprentissage = arg ['pathDico_systeme'] ['calcul'] ['nombre_ID_pour_apprentissage']
        
        if nombre_ID < nombre_ID_pour_apprentissage :
            self.pourcentage_echantillon = 101. # toojours vrai
        else:
            self.pourcentage_echantillon = float (nombre_ID) / float (nombre_ID_pour_apprentissage)
        
        
        # path corpus 
        self.path_corpus = arg ['Path_corpus']
        
        
    def init_corpus (self, ) :
        self.f_corpus = open (self.path_corpus, 'w')
        self.total_words = 0
        self.total_examples = 0
        return
            
            
    def ecrire_luigi_file_random(self, fin) :
        pourcentage_echantillon = self.pourcentage_echantillon      
        for ligne_json in fin:
            x = random.uniform (0., 100.)
            if  x < pourcentage_echantillon :
                self.total_examples += 1
                dico_ligne = json.loads (ligne_json)
                liste_mot = [v for v in dico_ligne.values()] [0]
                self.total_words += len(liste_mot)
                liste_mot.append('\n')
                ligne =  ' '.join (liste_mot)
                self.f_corpus.write(ligne )
                continue
            fin.close()
            continue
        
        return
        
    def Apprentissage_par_corpus(self,) :
        self.f_corpus.close()
        if Path(self.path_corpus).stat().st_size != 0 :
            self.apprentissage  (self.path_corpus,
                                 total_examples = self.total_examples,
                                 total_words =  self.total_words,
                                 isDocument = False)
            
        return
    
    
        
        
        
        
    

        
        
        
