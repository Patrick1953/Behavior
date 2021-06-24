# coding: utf-8
from random import randint
from datetime import datetime
from Kernel_BE import Kernel

def iterator (nombre) :
    vecteurG = [1.]*300
    paragrapheG = ['essai']*1000
    for i in range(0, nombre ):
        doc = {'ID' : i ,
               'vecteur' : vecteurG,
               'ID_random' : randint (1, 1000000),
               'paragraphe' : paragrapheG }
        #print (doc ['ID'])
        yield doc
        
def test_vecteur () :
    
    systeme = {  
    "createur" : "generic", 
    "date_emetteur" : str(datetime.now()),
    "http_auth" : None,
    "timeout" : 10,
    "host" : "localhost", 
    "port" : 9200 ,
    "zipChoisi" : 'bz2',
    "index_log_error" : "trace1",
    "index_log_warning" : "trace2",
    "index_log_trace" : "trace3",
    "index_system" : "systeme",
    "isPurge_existing_index_log" : True,
    "extra_elasticsearch_args" : None,
    "trace" : False,
    "ID_reference_base" : "000000000000000000000000000000",


        }

    k = Kernel (systeme)
    nombre_vecteur = 11
    docs = iterator (nombre_vecteur)
    index = 'test'
    isPurge_existing_index = True
    resultat = k.bulk_vecteur (docs,
                                   index = index,
                                  isPurge_existing_index = isPurge_existing_index,
                                  chunk_size = 2000,
                                 )
    
    assert (resultat == True)

    index = 'test'
    
    #print ("premiere lecture")
    #print ('index =', index)
    nombre, vrai_hits = k.search_par_bloc_vecteur(
                                                     index,
                                                     isRandom = False,

                                                     isID = False,
                                                     ID_min = "0",
                                                     ID_max  = str(nombre_vecteur),
                                                     ID_sort  = 'asc',
                                                     size = 1000 ,
                                                )
    
    
    #print ("recu premiere lecture = \n",len(vrai_hits) )
    #print ("recu premiere lecture = \n", vrai_hits [0])
    assert ( nombre == nombre_vecteur ), 'erreur nombre de bulk'

    #print ()
    #print ("seconde lecture")
    #print ('index =', index)
    nombre, vrai_hits = k.search_par_bloc_vecteur(
                                                     index,
                                                     isRandom = False,
                                                     isID = True,
                                                     ID_min = 0,
                                                     ID_max  = 9,
                                                     ID_sort  = 'asc',
                                                     size = 1000 ,

                                                    )
    
    #print ("recu seconde lecture = \n",len(vrai_hits) )
    #print ("recu seconde lecture = \n", vrai_hits [0])
    assert nombre == 10  , ' erreur sur search vecteur :' + str(nombre)

if __name__ == '__main__' :
    test_vecteur ()
    print ('vecteur OK')
