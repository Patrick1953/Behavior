# coding: utf-8
import time

from Lecture_csv import Lecture_csv

def test_lecture_csv () :
    
    path = '../bresil/'
    namefile =  'olist_customers_dataset.csv'

    L = Lecture_csv (path, namefile)

    resultat = L.read() [0]
    
    voulu = {'customer_id': '06b8999e2fba1a1fbc88172c00ba8bc7',
 'customer_unique_id': '861eff4711a542e4b93843c6dd7febb0',
 'customer_zip_code_prefix': '14409',
 'customer_city': 'franca',
 'customer_state': 'SP'}
    
    assert voulu == resultat
    
    nombre = 0
    for d in L.read_iterator () :
        nombre += 1
    assert nombre == 99441
    
    
if __name__ == '__main__' :
    t = time.time()
    test_lecture_csv ()
    print ('fin test_alimentation en ', time.time () - t)    
