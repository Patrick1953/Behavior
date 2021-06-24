# coding: utf-8
import json
from datetime import datetime

from myDate import myDate

def test_myDate ():
    def lire_file (pathFile) :
        f = open (pathFile, 'r')
        data = f.read()
        return json.loads (data)
    
    pathSysteme = '../data/test/parametres/dico_systeme_2.json'
    dico_systeme = lire_file (pathSysteme)
    
    D = myDate (dico_systeme)
    now = str(datetime.now())
    
    assert D.test_date(now, 'standard' )
    
    resultat = D.convert_date (now,  'standard')
    assert (resultat == now)
    
    d = '2021-02-07 11:12:49.743165'
    assert D.test_date (d, 'standard' )
    d = '2021-02-03 05:08:46.297688'
    assert D.test_date (d, 'standard' )
    assert D.convert_date (d,  'standard') == d
    
    
    format_entree = '%Y-%m-%d %H:%M:%S'
    d = '2021-02-07 11:12:49'
    assert D.test_date (d, format_entree )
    d = '2021-02-03 05:08:46'
    assert D.test_date (d, format_entree )
    assert D.convert_date (d,  format_entree) == '2021-02-03 05:08:46.000000'
    
    return
    
    
if __name__ == '__main__' :
    test_myDate ()
    print ('fin test date')    
 
