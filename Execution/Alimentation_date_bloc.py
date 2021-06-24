# coding: utf-8
import  os, sys, json, luigi, time, copy
from datetime import datetime

path = "../Calcul"
if path not in sys.path : 
    sys.path.append (path)

class Alimentation_date_bloc () :
    
    def __init__ (self, arg ):
        
        self.arg_travail_data = arg
        self.dico_systeme = arg ['pathDico_systeme']
        self.format_date_standard= self.dico_systeme ['calcul']['format_date_standard']
        #print (self.format_date_standard)
        
    def get_liste_date_bloc (self,) :
        
        date_debut = self.arg_travail_data ['variable_min']
        date_fin = self.arg_travail_data ['variable_max']
        
        
        date_debut_timestamp = self.timestamp (date_debut)
        date_fin_timestamp = self.timestamp (date_fin)
        
        nombre_bloc_date = self.dico_systeme ['calcul'] ['nombre_bloc_date']
        
        timedelta = (date_fin_timestamp - date_debut_timestamp) / nombre_bloc_date
        
        resultat = []
        time_debut = date_debut_timestamp
        time_fin = date_debut_timestamp + timedelta
        
        while (True) :
            if time_fin >= date_fin_timestamp :
                d1  = self.fromtimestamp(time_debut) 
                d2 =  self.fromtimestamp(time_fin) 
                resultat.append ([d1, d2])
                break
            d1  = self.fromtimestamp(time_debut) 
            d2 =  self.fromtimestamp(time_fin)
            resultat.append ([d1, d2])
            
            time_debut = time_fin
            time_fin = time_fin + timedelta
            continue
        return resultat
    
    def timestamp (self, date) :
        d = datetime.strptime(date, self.format_date_standard)
        return datetime.timestamp(d)
    
    def fromtimestamp (self, timestamp) :
        d = datetime.fromtimestamp(timestamp)
        return datetime.strftime(d, self.format_date_standard)
        
        
