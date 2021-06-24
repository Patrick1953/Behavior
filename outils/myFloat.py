# coding: utf-8
import locale
import sys
path = "../outils"
if path not in sys.path :
    sys.path.append (path)

from Parametres import Parametres

class myFloat () :
    def __init__ (self, dico_systeme):
        
        
        dico = Parametres (dico_systeme, listeData = ['calcul'])
        self.formatStandard = dico ['format_float_standard']
        return
    
    def convert_float (self, val, formatEntree) :
        """
        Parse a string to a floating point number. Uses locale.atof(),
        in future with ICU present will use icu.NumberFormat.parse().
        """
        try:
            return locale.atof(val)
        except ValueError:
            point = locale.localeconv()['decimal_point']
            sep = locale.localeconv()['thousands_sep']

            if point == ',':
                return locale.atof(val.replace(' ', sep).replace('.', sep))
            elif point == '.':
                return locale.atof(val.replace(' ', sep).replace(',', sep))
            else:
                raise ValueError
        
        return
    
    
    def test_float(self, val, formatEntree):
        try:
            self.convert_float ( val, formatEntree)
            return True
        except:
            return False
        
            
        
            
                
