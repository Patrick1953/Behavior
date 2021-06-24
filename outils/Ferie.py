# coding: utf-8
from datetime import datetime
from jours_feries_france import JoursFeries
from Parametres import Parametres
from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

class Ferie ()  :
    # Obtenir les jours fériés pour une année, pour la métropole
    #res = JoursFeries.for_year(2018)
    # res est un dictionnaire
    # {
    #     '1er janvier': datetime.date(2018, 1, 1),
    #     'Lundi de Pâques': datetime.date(2018, 4, 2),
    #     '1er mai': datetime.date(2018, 5, 1),
    #     '8 mai': datetime.date(2018, 5, 8),
    #     'Ascension': datetime.date(2018, 5, 10),
    #     'Lundi de Pentecôte': datetime.date(2018, 5, 21),
    #     '14 juillet': datetime.date(2018, 7, 14),
    #     'Assomption': datetime.date(2018, 8, 15),
    #     'Toussaint': datetime.date(2018, 11, 1),
    #     '11 novembre': datetime.date(2018, 11, 11),
    #     'Jour de Noël': datetime.date(2018, 12, 25)
    # }

    # Vous pouvez aussi obtenir certains jours fériés en tant que datetime.date
    #print (JoursFeries.lundi_paques(2018))
    #print (JoursFeries.ascension(2018))
    #print (JoursFeries.lundi_pentecote(2018))

    # Obtenir les jours fériés pour une zone spécifique
    #res = JoursFeries.for_year(2018, zone="Alsace-Moselle")

    # Quelques fonctions d'aide
    #JoursFeries.is_bank_holiday(datetime.date(2019, 12, 25), zone="Métropole")
    # -> True
    #JoursFeries.next_bank_holiday(datetime.date(2019, 12, 24), zone="Métropole")
    # -> ('Noël', datetime.date(2019, 12, 25))

    def __init__ (self,) :
        
        self.memoire = {}
        
        
    
        
    def get_jour_ferie (self, date ) :
        
        
        annee = date.year
        date_cherche = str(date.date())
        
        dico = self.get_info  (annee)
        
        if date_cherche in dico :
            return dico[date_cherche]
        else :
            return 'non_ferie'
        
    
    
    def get_info (self, annee) :
        annee_string = str(annee)
        if annee_string in self.memoire :
            res = self.memoire [annee_string]
            #print (annee_string)
        else :
            res_data = JoursFeries.for_year(annee)
            res = self.inverse (res_data)
            self.memoire [annee_string] = res
            
        return res
    
    def inverse (self, dico ) :
        r = {}
        for jour_ferie, date in dico.items() :
            r [str(date)] = '_'.join([mot.lower () for mot in jour_ferie.split()])
        return r
    
    
    
            
        
        
        
        
        
        
        
