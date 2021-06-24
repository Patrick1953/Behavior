# coding: utf-8
import sys

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Ferie import Ferie
from gestionDate import gestionDate

class Calcul_date (gestionDate ) :
    
    def __init__ (self, ) :
        
        super ().__init__ ()
        self.F = Ferie()
        self.calcul_dates = {

                            'demi_jour' :self.Demi_jour,
                            'jour' : self.Jour,
                            'semaine' : self.Semaine,
                            'mois' : self.Mois,
                            'annee' : self.Annee,
                            'ferie' : self.get_jour_ferie, 
                        }
        
        self.liste_operations = [op for op in self.calcul_dates.keys()]
        
        return
    
    def get_calcul_dates  (self,) :
        return self.calcul_dates
    
    def get_liste_travail_date (self,)  :
        return self.liste_operations
    
    def Demi_jour (self,date) :
        
        self.dateCourante = date
        resultat = self.isMatin ()
        if resultat :
            return 'bpm'
        else:
            return 'apm'
    def Jour (self, date) :
        self.dateCourante = date
        return self.getJour ()
    
    def Semaine (self,date) :
        self.dateCourante = date
        return str(date.isocalendar()[1])
    
    def Mois (self, date) :
        self.dateCourante = date
        return self.getMois ()
    
    def Annee (self,date) :
        self.dateCourante = date
        return str(self.getAnnee() )
    
    def get_jour_ferie (self, date) :
        return self.F.get_jour_ferie ( date)
    
    
        
        
        
    
    
