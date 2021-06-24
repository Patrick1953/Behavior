# coding: utf-8
from datetime import datetime
import sys
path = "../outils"
if path not in sys.path :
    sys.path.append (path)

from Parametres import Parametres




class myDate () :
    def __init__ (self,dico_systeme ) :
        
        dico = Parametres (dico_systeme, listeData = ['calcul'])
        self.formatStandard = dico ['format_date_standard']
        
        return
    
    def test_date (self, val, formatEntree) :
        if formatEntree == 'standard' :
            formatEntree = self.formatStandard
        
        try:
            datetime.strptime (val, formatEntree)
            return True
        except:
            return False
        
        return
    
    def convert_date (self,val , formatEntree  ) :
        if formatEntree == 'standard' :
            return val
        val = datetime.strptime (val, formatEntree)
        r = datetime.strftime (val, self.formatStandard )
        return  r
    
    
    
        
        
        
        
    
        
