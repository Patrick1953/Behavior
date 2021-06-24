# coding: utf-8
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


def apprentissage (liste, namefilePickle, max_features) :
    vectorizer = TfidfVectorizer(
                                analyzer='word', 
                                sublinear_tf=True,
                                strip_accents='unicode',
                                token_pattern=r'\w{1,}',
                                ngram_range=(1, 1),
                                max_features=max_features)
    # on sauve
    tfidf = vectorizer.fit(liste)
    pickle.dump(tfidf, open(namefilePickle, "wb"))
    return



class vectorisationStrings():
    def __init__ (self,namefilePickle) :
        self.new_tfidf = pickle.load  (open("tfidf.pickle", "rb"))
        
    def vectorisationListStrings (self, liste) :
        resultat_xparseArray = self.new_tfidf.transform(liste)
        return resultat_xparseArray.toarray().tolist()
        
        
    def vectorisationString (self , ligne ) :
        liste = [ligne]
        resultat_xparseArray = self.new_tfidf.transform(liste)
        return resultat_xparseArray.toarray().tolist() [0]
    
    def getFeatures (self,) :
        return self.new_tfidf.get_feature_names()


    
