# coding: utf-8
from datetime import datetime, timedelta
import calendar
import random
from copy import copy

class gestionDate () :
    def __init__ (self, typeGen = 0, liste_typeGen = ['demi_jour', 'jour','semaine', 'mois'],
                 dateDebut = [2021,1,1,0,0,0,0],
                 formatDate = "%Y-%m-%d %M:%S:%f",
                 ) :
        
        """
        typeGen int de 0,3 fournit l 'acces au type d'increment donnée par liste_typeGen
        liste_typeGen = ['demi_jour', 'jour','semaine', 'mois']
        dateDebut = [2021,1,1,0,0,0,0] si dateDebut alors on applique formatDate 
        formatDate = "%Y-%m-%d %M:%S:%f"
        modif à faire https://pypi.org/project/jours-feries-france/0.5.1/
        """
        self.formatDate = formatDate
        self.liste_typeGen = liste_typeGen
        
        
        if isinstance (dateDebut, type (' ')) :
            self.dateCourante = datetime.strptime(dateDebut, formatDate)
        else :
            y, m, d, h, mi, s, ms = dateDebut
            self.dateCourante = datetime(y, m, d, h, mi, s, ms)
            
        self.dateDebut = copy(self.dateCourante)
        self.dateDebut_string = str(self.dateDebut)
        
        self.typeGen = liste_typeGen [typeGen]
        
        self.jour = ("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche")
        self.mois = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout' , 'septembre',
                    'octobre', 'novembre', 'decembre']
        
        if self.typeGen == 'demi_jour' :
            t1 = timedelta( hours = 0,)
            t2 = timedelta(hours = 12, )
        if self.typeGen == 'jour' :
            t1 = timedelta( days = 1,)
            t2 = timedelta(days = 2, )
        if self.typeGen == 'semaine' :
            t1 = timedelta( weeks = 1,)
            t2 = timedelta(weeks = 2,)
            
        if self.typeGen == 'mois' :
            return
           
        self.delta = (t2 - t1).total_seconds()
        return
    
    
    
    def getListeDate (self,) :
        l = [self.dateCourante.year,
             self.dateCourante.month,
             self.dateCourante.day,
             self.dateCourante.hour,
             self.dateCourante.minute,
             self.dateCourante.second,
             self.dateCourante.microsecond,
            ]
        return l
        
    
    def getDate (self,) :
        return str(self.dateCourante)
    
    def isMatin (self,) :
        heure = self.dateCourante.hour
        if heure < 12 :
            return True
        else :
            return False
        
    def getJour (self,) :
        i = self.dateCourante.weekday()
        return self.jour [i]
    
    def getMois (self,):
        i = self.dateCourante.month
        return self.mois [i-1]
    
    def getAnnee (self,):
        return self.dateCourante.year

    def increment (self,) :
        if self.typeGen == 'mois' :
            days_in_month = calendar.monthrange(self.dateCourante.year, self.dateCourante.month)[1]
            t2 = timedelta(days = days_in_month )
            self.delta = t2.total_seconds()
        timestamp  = datetime.timestamp(self.dateCourante)
        newTimestamp = timestamp + self.delta
        self.dateCourante = datetime.fromtimestamp(newTimestamp)
        return str(self.dateCourante)
    
    def aleaDate (self, ) :
        # on avance de facon aleatoire l 'heure courante pour fournir une heure dispersé'
        if self.typeGen == 'mois' :
            days_in_month = calendar.monthrange(self.dateCourante.year, self.dateCourante.month)[1]
            t2 = timedelta(days = days_in_month )
            self.delta = t2.total_seconds()
        
          
        delta = (random.random() * self.delta)
        timestamp  = datetime.timestamp(self.dateCourante)
        newTimestamp = timestamp + delta
        return str(datetime.fromtimestamp(newTimestamp))
    
    
    
    def recherche_plage (self, date, ) :
        """
        date en format standart string
        nous allons parcourir les plages suivant le pas
        et renvoyer en format string dateDebut de la plage et dateFin de la plage
        en format string
        """
            
        if not isinstance ( date, type (' ')) or date < self.dateDebut_string :
            raise ValueError
                
        date =  datetime.strptime(date, self.formatDate )
        
        dateDebut_courante = self.dateDebut
        dateFin_courante = self._increment_date (dateDebut_courante )
        
        while (not ( (date >= dateDebut_courante) and (date < dateFin_courante) ) ) :
            dateDebut_courante = self._increment_date (dateDebut_courante )
            dateFin_courante = self._increment_date (dateDebut_courante )
            continue
            
        return str(dateDebut_courante), str(dateFin_courante)
    
      
    
    def _increment_date (self, date ) :
                
        if self.typeGen == 'mois' :
            days_in_month = calendar.monthrange(date.year, date.month)[1]
            t2 = timedelta(days = days_in_month )
            self.delta = t2.total_seconds()
        timestamp  = datetime.timestamp(date)
        newTimestamp = timestamp + self.delta
        return datetime.fromtimestamp(newTimestamp)
    
    def convertir (self, date, formatDate = None) :
        if formatDate == self.formatDate :
            return date
        date = datetime.strptime(date, formatDate) 
        return str (date)
            
            
        
    
        
        
        
        
        
        
        
        
        
    
    
            
        




        
    
        
