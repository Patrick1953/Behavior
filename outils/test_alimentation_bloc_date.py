# coding: utf-8
#### import json, time
import numpy as np
from datetime import datetime

from Kernel_BE import Kernel


def test_alimentation_bloc_date ():
    
    
    
    #  variable pour alimentation bloc_date
    
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
    
    index = 'data_fake'

    ID_reference_min = 0
    ID_reference_max = 100000000
    ID_reference_sort = 'asc'
    isReference = False






    isVariable =  True
    nom_variableQuery = "date_evenement"
    variable_min = '2021-02-01 00:00:00.000'
    variable_max = '2021-03-10 00:00:00.000'
    variable_sort = 'asc'

    isID = False
    ID_min = "couple_cadre_1"
    ID_max = "couple_cadre_sup_1"
    ID_sort = 'asc'
    
    isTrace = False
    size = 192*7
    
    taille, hits = k.search_par_bloc (index,

                                     'ID',                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = None,
                                     isReference = False,

                                     isID = False,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = None,

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = variable_min,
                                     variable_max = variable_max,
                                     variable_sort  = 'asc',

                                     size = size ,

                                     )
    
    assert taille == size, "erreur lecture globale sur date"
    
    #print ("dans lecture avec size =", size, " on a len(hist) =",len(hits), " et taille =", taille)
    taille_totale_lu = len(hits)
    memoire = {}
    date_max = ""
    isFirst = True
    for hit in hits :
        enreg = hit ['_source']
        date_evenement = enreg ['date_evenement']
        if date_evenement > date_max :
            date_max = date_evenement
        
        if isFirst :
            taille_evenement = len(date_evenement)
            isFirst = False
        
        if taille_evenement != len(date_evenement) :
            print('### erreur possible pour date_evenement =',date_evenement) 
            raise ValueError
        try :
            memoire [date_evenement] += 1
        except :
            memoire [date_evenement] = 1
        continue
    
    
        
    #print ('apres analyse de la premiere lecture, on a taille_evenement =',taille_evenement)
    #print ('apres analyse de la premiere lecture, on a len (memoire) =',len(memoire))
    #print ('apres analyse de la premiere lecture, on a date_max =',date_max)
    #print ()
                
    
    size = 700
    
    
    taille, hits = k.search_par_bloc (index,

                                     'ID',                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = None,
                                     isReference = False,

                                     isID = False,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = None,

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = variable_min,
                                     variable_max = variable_max,
                                     variable_sort  = 'asc',

                                     size = size ,

                                     )
    
    #print ("dans lecture avec size =", size, " on a len(hist) =",len(hits), " et taille =", taille)
    #print ()
    taille_deja_lu = len(hits)
    
    memoire = {}
    date_max = ""
    for hit in hits :
        enreg = hit ['_source']
        date_evenement = enreg ['date_evenement']
        if date_evenement > date_max :
            date_max = date_evenement
            
        try :
            memoire [date_evenement] += 1
        except :
            memoire [date_evenement] = 1
        continue
    
    #print ('apres analyse de la deuxieme lecture, on a len (memoire) =',len(memoire))
    #print ('apres analyse de la deuxieme lecture, on a date_max (la plus grande) =',date_max)
    #print ()
    hit = hits [len(hits)- 1]
    enreg = hit ['_source']
    date_evenement_min = enreg ['date_evenement']
    
    
    format_standard = '%Y-%m-%d %H:%M:%S.%f'
    dateCourante = datetime.strptime(date_evenement_min, format_standard)
    timestamp = datetime.timestamp(dateCourante)
    timestamp += 1
    date_evenement_min = str(datetime.fromtimestamp(timestamp))
    
    
    #print ('preparation deuxieme lecture')
    #print ('variable min calculée dans alimentation_bloc =',date_evenement_min)
    #print ( 'et variable_max =' , variable_max)
    
    variable_min = date_evenement_min
    
    taille, hits = k.search_par_bloc (index,

                                     'ID',                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = None,
                                     isReference = False,

                                     isID = False,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = None,

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = variable_min,
                                     variable_max = variable_max,
                                     variable_sort  = 'asc',

                                     size = size ,

                                     )
    #print ("dans lecture bloc final  avec size =", size, " on a len(hist) =",len(hits), " et taille =", taille)
    #print ('bloc final len(hits) =', len(hits))
    hit = hits [len(hits)- 1]
    enreg = hit ['_source']
    date_evenement_min = enreg ['date_evenement']
    #print ('date_evenement finale apres la dernier lecture =', date_evenement_min)
    
    assert len(hits) + taille_deja_lu == taille_totale_lu, 'erreur de, lecture sur date'
    
if __name__ == '__main__' :
    test_alimentation_bloc_date ()
    print ('fin test_alimentation_bloc_date')    

    
