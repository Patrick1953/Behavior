# coding: utf-8
from datetime import datetime
from Ferie import Ferie
from Entree_sortie_lock import Entree_sortie_lock

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

def test_ferie () :
    
    
    
    

    arg_entree_sortie_lock = {} 
    pathFile = '../data/test/parametres/dico_systeme_2.json'
    arg_entree_sortie_lock ['pathFile'] = pathFile
    Entree_sortie_systeme = Entree_sortie_lock (arg_entree_sortie_lock)
    
    dico_systeme = Entree_sortie_systeme.lire_with_lock()
    Entree_sortie_systeme.unlock_lire()
    
    
    format_date_standard = dico_systeme ['calcul'] ['format_date_standard']
    
    
    F = Ferie ()
    date_string = "2021-04-27 19:45:00.000000"
    date = datetime.strptime(date_string, format_date_standard)
    
    
    resultat = F.get_jour_ferie ( date)
    
    assert resultat == 'non_ferie'
    
    date_string = "2030-12-25 19:45:00.000000"
    date = datetime.strptime(date_string, format_date_standard)
    resultat = F.get_jour_ferie ( date)
       
    assert resultat == 'jour_de_noël'
    
    date_string = "2030-11-11 19:45:00.000000"
    date = datetime.strptime(date_string, format_date_standard)
    resultat = F.get_jour_ferie ( date)
      
    assert resultat == '11_novembre'
    
    
    
if __name__ == '__main__' :
    test_ferie ()
    print ('test_ferie OK') 
