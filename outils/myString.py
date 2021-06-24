# coding: utf-8
from datetime import datetime

import sys
path = "../outils"
if path not in sys.path :
    sys.path.append (path)

from Parametres import Parametres




class myString () :
    def __init__ (self, dico_systeme ) :
        
        dico = Parametres (dico_systeme, listeData = ['calcul'])
                      
        self.formatStandard = dico ['format_string_standard']
                
        return
    
    def test_string (self, val, formatEntree) :
        if formatEntree == 'standard' :
            if isinstance (val, type(' ')) :
                return True
            
            return False
        
        return True
    
        
        return
    
    def convert_string (self,val , formatEntree  ) :
        if formatEntree == 'standard' :
            return val
        
        return  val
    
    
    
        
        
       
        
