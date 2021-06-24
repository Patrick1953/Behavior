# coding: utf-8
import locale
from locale import atof

class Convert():
    def __init__ (self,abbr = ''):
        locale.setlocale(locale.LC_ALL, abbr)
        self.info = locale.localeconv()
        return
    
    def float(self, val):
        """
        Parse a string to a floating point number. Uses locale.atof(),
        in future with ICU present will use icu.NumberFormat.parse().
        renvoie None if error
        """
        try:
            return locale.atof(val)
        except ValueError:
            point = locale.localeconv()['decimal_point']
            sep = locale.localeconv()['thousands_sep']
            try:
                if point == ',':
                    return locale.atof(val.replace(' ', sep).replace('.', sep))
                elif point == '.':
                    return locale.atof(val.replace(' ', sep).replace(',', sep))
                else:
                    return None
            except ValueError:
                return None
            
            
