# coding: utf-8
import os, sys, json
from datetime import datetime, timedelta
import calendar

path = "../Calcul"
if path not in sys.path :
    sys.path.append (path)
from Calcul_date import Calcul_date

class Calcul_date_pas () :
    
    def __init__ (self, type_pas ) :
        
        self.type_pas = type_pas
                
        self.Description_travail_date = Calcul_date ()
        self.formatDate = "%Y-%m-%d %M:%S:%f"
        
        self.jour = ("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche")
        self.mois = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout' , 'septembre',
                    'octobre', 'novembre', 'decembre']
        
        if self.type_pas == 'demi_jour' :
            t1 = timedelta( hours = 0,)
            t2 = timedelta(hours = 12, )
        if self.type_pas == 'jour' :
            t1 = timedelta( days = 1,)
            t2 = timedelta(days = 2, )
        if self.type_pas == 'semaine' :
            t1 = timedelta( weeks = 1,)
            t2 = timedelta(weeks = 2,)
            
        if self.type_pas == 'mois' or self.type_pas == 'trimestre' :
            return
           
        self.delta = (t2 - t1).total_seconds()
        return
    
    
           
    def _liste_pas ( self,):
        
        liste1 = self.Description_travail_date.get_liste_travail_date ()
        try:
            liste1.remove ('ferie')
        except:
            pass
        liste1.append('trimestre')
        
        return liste1
    
    def _calcul_delta_mois (self, date_debut) :
        
        days_in_month = calendar.monthrange(date_debut.year, date_debut.month)[1]
        t2 = timedelta(days = days_in_month )
        delta = t2.total_seconds()
        timestamp  = datetime.timestamp(date_debut)
        newTimestamp = timestamp + delta
        date_fin = datetime.fromtimestamp(newTimestamp)
        return date_fin
        
    
    def _calcul_delta_trimestre (self, date_debut) :
        
        date_courante = date_debut
        for _ in range( 0, 3) :
            date_courante = self._calcul_delta_mois (date_courante)
        return date_courante
                 
        
    
    def calcul_date_fin (self, date_debut) :
        
        date =  datetime.strptime(date_debut, self.formatDate )
        
        if self.type_pas == 'mois' :
            date_fin = self._calcul_delta_mois (date)
        elif self.type_pas == 'trimestre' :
            date_fin = self._calcul_delta_trimestre (date)
        else:
            timestamp  = datetime.timestamp(date)
            newTimestamp = timestamp + self.delta
            date_fin = datetime.fromtimestamp(newTimestamp)
        
        return datetime.strftime (date_fin, self.formatDate)
        
        
        
        
        
    
    
