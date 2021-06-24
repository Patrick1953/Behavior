# coding: utf-8
#Import all the dependencies

from gensim.models.doc2vec import Doc2Vec, TaggedDocument, TaggedLineDocument
from gensim.test.utils import get_tmpfile
from nltk.tokenize import word_tokenize
import nltk
import pandas as pd
import numpy as np
import os, json ,sys, time
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
import multiprocessing


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from validationPath import validationPath    
from Kernel_BE import Kernel





class Embedding () :
    def __init__ (self,arg) :
        

        
        self.dico_systeme = arg ['pathDico_systeme']
        
        # lecture des parametres de l embedding (dans dico _embedding)
        self.vector_size = self.dico_systeme ['embedding'] ['vector_size']
        self.alpha = self.dico_systeme ['embedding'] ['alpha']
        self.min_alpha = self.dico_systeme ['embedding']['min_alpha']   #0.00025,
        self.min_count = self.dico_systeme ['embedding']['min_count']          # 1, # on peut retirer les mots qui se repete peu
        self.dm = self.dico_systeme ['embedding']['dm']                #1 no BoW 
        self.max_epoch = self.dico_systeme['embedding'] ['max_epoch']   # nombre d iteration pour apprentissage du RN                              
        self.decrease_alpha = self.dico_systeme ['embedding'] ['decrease_alpha'] # decroissance du pas de retro propagation
        self.isOublie = self.dico_systeme ['embedding'] ['isOublie']
        
        self.cores = multiprocessing.cpu_count()
        
        self.pathFile_model = arg ['pathModele']
        
        validationPath (self.pathFile_model)
        # lecture du model si necessaire (premier apprentissage)
        if not os.path.exists(self.pathFile_model) :
            self.init_model ()
        else :
            
            abs_path = os.path.abspath(self.pathFile_model)
            self.model = Doc2Vec.load(abs_path)
            
        return
    
           
    def init_model (self,) :
        
        
        
        self.model = Doc2Vec(vector_size= self.vector_size,
                                alpha=self.alpha, 
                                min_alpha= self.min_alpha, #0.00025,
                                min_count= self.min_count,     # on peur retirer les mots qui se repete peu
                                dm =self.dm,
                                 workers = self.cores,
                            
                            ) # 1 no BoW
        
        
        self.debug_model()
        return
    
    
    
    def apprentissage (self, data,
                       isDocument = True,
                       total_examples = 24,
                       total_words =  3792,
                      ) :
        
        # apprend par bloc recu et on sauve le modele (pour inference si la phase de train est fini )
        # le format d entree data = { ID_pas : ['mots,' ] 
        # ou ID_pas est l ID qui permet de recuperer le vecteur embedding (à recalculer ?)
        # le calcul est en non supervise
        
        
        if isDocument :
            
            tagged_data = [TaggedDocument(words = _d  ,
                                          tags=[str(ID_pas)]) for ID_pas, _d in data.items()]






            liste_mot  = self.get_vocabulaire()
            if len(liste_mot) == 0 :
                self.model.build_vocab(tagged_data,) # à voir si on perd des mots ? 
            else:
                pass


            
            self.model.train(corpus_iterable = tagged_data, 
                                    total_examples = self.model.corpus_count,
                                    epochs = self.max_epoch,
                                 
                                )

                
            

            return
        
        else:
            
            self.model.train(corpus_file = data,
                             epochs = self.max_epoch,
                            total_examples = total_examples,
                            total_words =  total_words,
                           )

            return
             
    
    def save_model (self,) :
        # on sauve un modele qui peut continuer à apprendre 
        fname = os.path.abspath(self.pathFile_model)
        self.model.save(fname)
        self.model = Doc2Vec.load(fname)
        return

    
    def infer_vecteur_embedding (self, data) :
        # data = vecteur de mots (en lower # pas une phrase
        return self.model.infer_vector(data)
        
    def get_vocabulaire (self,) :
        
        r =[mot for mot in self.model.wv.key_to_index.keys()]
        return r
    
    def debug_model (self, ) :
        # bug Gensim
        # on fait un premier apprentissage  pour eviter la bug ()
        # 
        
        dico = {'_init' : ['patrick', 'laffitte']}
        
        self.apprentissage (dico)
        return
        
        dico = {'_init' : ['patrick', 'laffitte']}
        
        tagged_data = [TaggedDocument(words = _d  ,
                                          tags=[str(ID_pas)]) for ID_pas, _d in dico.items()]
        
        self.model.build_vocab(tagged_data,) # à voir si on perd des mots ? 
        return
    

        
    
    

class Gestion_vecteur(Embedding) :
    
    'permet de réaliser les fonctions necessaires sur les vecteurs'
    'comme la normalisation'
    'Warning calcul par inference paragraphe => vecteur'
    
    def __init__ (self, arg) :
        
        super().__init__ (arg)
        
        
    def get_vecteur_array (self,dico_paragraphes) :
        
        resultat = []
        liste_ID = [ID for ID in dico_paragraphes.keys()]
        for ID in liste_ID :
            data = dico_paragraphes [ID]
            vecteur = self.infer_vecteur_embedding (data)
            resultat.append (vecteur)
            continue
        return np.array (resultat), liste_ID
    
    def get_vecteur_normalized (self, dico_paragraphe) :
        tableau, liste_ID = self.get_vecteur_array (dico_paragraphe) 
        normalized_array = sklearn.preprocessing.normalize(tableau, norm="l2")
        return normalized_array, liste_ID
    
    
        
    def similarite_par_vecteur (self, vecteur_1, vecteur_2 ):
        similarities = cosine_similarity([vecteur_1], [vecteur_2] , )
        return similarities [0] [0]
    
    def calcul_distance (self, vecteur_embedding_0 ,vecteur_embedding_1) :
        # on normalize avant le calcul de distance
        v0 = np.array (vecteur_embedding_0)
        v0_0 = v0/np.linalg.norm(v0)
        
        v1 = np.array (vecteur_embedding_1)
        v1_1 = v1/np.linalg.norm(v1)

        dist =  np.linalg.norm (v0_0 - v1_1)
        return dist  
    

        
        
class Embedding_vecteur (Embedding)  :
    def __init__ (self, index_bulk, dico_out, arg) :
        '''tagged_data
        on delegue à Embedding tous le boulot
        y compris et surtout le loading du modele (parametre dans arg)
        
        initialisation du kernel (pour bulk_vecteur)
        
        dans _iterateur 
        boucle sur IDs du dico_out :
            pour chaque ID , recuperer le vecteur et bulk du vecteur et du paragraphe associé
            
        
            
        
        '''
        
        super().__init__( arg)
        
        kernel_data = self.dico_systeme ['elasticsearch']
        self.kernel = Kernel(kernel_data)
        
        self.index_bulk = index_bulk
        
        
    def _iterateur (self, ) :
        
        for ID, paragraphe in self.dico_out.items():
            
            vecteur = self.infer_vecteur_embedding ( paragraphe)
            doc = {'ID' : ID ,
                  'vecteur' : vecteur,
                   'paragraphe' : paragraphe,
                  }
            yield doc
        
        
    def bulk_vecteur (self, dico_out) :
        
        self.dico_out = dico_out
        
        self.kernel.bulk_vecteur (self._iterateur(),
                                  index = self.index_bulk,
                                  isPurge_existing_index = False,
                                  chunk_size = 2000,
                                 )
        return
    
    
    
    
                           
        
        
        
        
        
        
        

    
    
    
          
        
        
