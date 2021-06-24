# coding: utf-8
class Entree_fichier () :
    
    def __init__(self, arg) :
        path = arg ['path_fichier']
        nom_fichier = arg ['nom_fichier']
        self.pathFile = path + nom_fichier
        
        self.sep = arg ['separateur'] 
        
        
    def init_lecture (self,) :
        self.f = open (self.pathFile, "r", newline='\r\n')
        #self.f = open(self.pathFile, 'r')
        
    def readIterator (self,) :
        sep = self.sep
        while (True) :
            li = self.f.readline ()
            if li == "" :
                return
            liste = li[:-1].split (sep)
            yield  liste
    def close (self,) :
        self.f.close()
    
    
