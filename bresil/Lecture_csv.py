# coding: utf-8
import csv

class Lecture_csv ():
    
    def __init__ (self, path, nameFile ):
        
        self.pathFile = path + nameFile
        
    def read (self,) :
        liste = []
        with open(self.pathFile, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                liste.append (row)
                
        return liste
    
    def read_iterator (self,) :
        with open(self.pathFile, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield row
        

    
    
