# coding: utf-8
import json, time
import numpy as np
from datetime import datetime

from Kernel_BE import Kernel



        
        
def  test_kernel_general () :

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

    ID_reference_base = systeme ["ID_reference_base"]
    k = Kernel(systeme)
    index = "test"
    k.create_index (index)
    k.delete_index (index)




    array = np.array ([i for i in range(0, 10)])
    data = k.array2liste (array,)
    arrayF = k.liste2array( data,dtype = np.int32)

    assert array.any()  == arrayF.any() , 'array <=> faux'

    array = np.array ([float(i)*0.1 for i in range(0, 10)])
    data = k.array2liste (array,)
    arrayF = k.liste2array( data,dtype = np.float64)

    assert array.any()  == arrayF.any(), 'array <=> faux'
    #print (array)
    #print (arrayF)
    ID_reference_base = systeme ["ID_reference_base"]
    taille = len(ID_reference_base)
    def iterateur (kernel, nombre = 1000) :

        for i in range(0, nombre) :
            for j in range(0,10) :
                dico = {
                      "ID" : ("0000"+ str(i)) [-4:] ,
                      "date_evenement" : (ID_reference_base + str(i))[-taille:],

                      "ID_reference" : (ID_reference_base  +str(i))[-taille:],

                       "nom_variable" : "variable_"+ str(j),
                       "valeur" : 1000000000000,
                }
                yield dico

    nombre = 10000    
    docs = iterateur (k, nombre = nombre)
    index = "test"

    t = time.time()
    k.bulk ( docs, index, isPurge_existing_index = True,)
    #print ("bulk =",k.count (index) == nombre*10, " en temps =", time.time () - t)



    # on test les logs

    #auteur, etape,  message

    auteur = "test1"
    etape = "etape1"
    message = "message1"

    k.log_error (auteur, etape,  message)
    k.log_error (auteur, etape,  message)

    k.log_warning (auteur, etape,  message)
    k.log_warning (auteur, etape,  message)

    k.log_trace (auteur, etape,  message)
    k.log_trace (auteur, etape,  message)
    
    voulu = {'origine': 'error', 'auteur': 'test1', 'etape': 'etape1',
             'message': 'message1'}
    
    result = k.get_logs_error() 
    assert len (result) == 2, "log error"
    voulu ['origine'] = 'error'
    r = result [0]
    del r ['date']
    assert voulu == r, str(result [0])
    
    result = k.get_logs_warning()
    assert len (result) == 2, "log warning"
    voulu ['origine'] = 'warning'
    r = result [0]
    del r ['date']
    assert voulu == r, "log warning"
    
    result = k.get_logs_trace()
    assert len (result) == 2, "log trace"
    voulu ['origine'] = 'trace'
    r = result [0]
    del r ['date']
    assert voulu == r, "log trace"
    
    

    
    # test search bloc ######################

    j = 5

    i = 0
    pas = 1000 # donne 1000 ligne

    ID_reference_min = i
    ID_reference_max = i + pas
    ID = str(i+2)
    index = "test"
    # test avec un size ################


    time.time()
    taille, hits = k.search_par_bloc (index,
                             ID,                     # inused Mais compatibilite oblige
                             ID_reference_min,
                             ID_reference_max ,
                             ID_reference_sort = None,

                             isID = False,
                             ID_min = "",
                             ID_max  = "",
                             ID_sort  = 'asc',

                             isVariable = False,
                             nom_variableQuery = None,
                             variable_min = "",
                             variable_max = "",
                             variable_sort = None,

                             size = pas*10 ,
                                     )

    assert taille != 0  , 'erreur de lecture'
        


    







    assert taille == len(hits)  and taille == pas * 10 , 'erreur taille dans lecture de 10000 éléments'
        



    t = time.time()


    taille, hits = k.search_par_bloc (index,
                             ID,                     # inused Mais compatibilite oblige
                             ID_reference_min,
                             ID_reference_max ,
                             ID_reference_sort = None,

                             isID = False,
                             ID_min = "",
                             ID_max  = "",
                             ID_sort  = None,

                             isVariable = False,
                             nom_variableQuery = None,
                             variable_min = "",
                             variable_max = "",
                             variable_sort = None,

                             size = pas*10 ,
                                     )

    
    assert taille == len(hits)  and taille == 10000 , 'erreur taille dans lecture de 10000 éléments'
    



    r = hits [0]['_source'] ['ID_reference']

    taille_1 = len(ID_reference_base)
    voulu = (ID_reference_base  +str (ID_reference_min))[-taille_1:]

    assert r == voulu , 'erreur dans le contenu du premier hit'
        



    r = hits [taille - 1]['_source'] ['ID_reference']

    taille_1 = len(ID_reference_base)             
    voulu = (ID_reference_base  + str(ID_reference_max-1))[-taille_1:] # on calcul le ID_reference
    assert r == voulu , 'erreur dans le contenu du dernier hit'
    


    # avec ID voulu
    j = 5 # ID
    ID_min = ("0000"+ str(j)) [-4:] # il apparait une fois par ligne donc il a 10 variables
    ID_max = ("0000"+ str(j+1)) [-4:]


    i = 0
    pas = 100 # nombre de ligne


    ID_reference_min = i 
    ID_reference_max = i + pas
    index = "test"
    t = time.time()
    taille, hits = k.search_par_bloc (index,
                                     ID,                     # inused Mais compatibilite oblige

                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                      isReference = True,

                                     isID = True,
                                     ID_min = ID_min ,
                                     ID_max  = ID_max ,
                                     ID_sort  = 'asc',

                                     isVariable = False,
                                     nom_variableQuery = None,
                                     variable_min = "",
                                     variable_max = "",
                                     variable_sort = None,
                                      size = pas*10 ,
                                     )

    



    assert taille == len(hits) and taille == 20 , 'nombre d evenements pour 1 ID'
        





    ID_voulu =  ("0000"+ str(j)) [-4:]    # ID_min 
    taille_variable = 10
    liste_variable =  []
    for i in range(0, taille_variable ) :
        nom_variable = hits [i] ['_source'] ['nom_variable']
        assert hits [i] ['_source'] ['ID'] == ID_min
        
        liste_variable.append (nom_variable)
        continue

    voulu = ['variable_0', 'variable_1', 'variable_2', 'variable_3', 'variable_4', 'variable_5',
             'variable_6', 'variable_7', 'variable_8', 'variable_9']

    assert liste_variable == voulu , 'variable non trie par ID_reference'
        


    # on verifie que ID_reference est trie

    ID_reference_courant = ""
    for i in range(0, 10) :
        ID_reference = hits[i] ['_source'] ['ID_reference']
        assert ID_reference >= ID_reference_courant
        
        ID_reference_courant = ID_reference
        continue

    # avec ID voulu mais non ID dans ID_reference
    j = 5 # ID
    ID_min = ("0000"+ str(j)) [-4:] # il apparait une fois par ligne donc il a 10 variables
    ID_max = ("0000"+ str(j+1)) [-4:]


    i = 0
    pas = 5


    ID_reference_min = i 
    ID_reference_max = i + pas
    index = "test"
    t = time.time()
    taille, hits = k.search_par_bloc (index,
                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = True,

                                     isID = True,
                                     ID_min = ID_min ,
                                     ID_max  = ID_max ,
                                     ID_sort  = 'asc',

                                     isVariable = False,
                                     nom_variableQuery = None,
                                     variable_min = "",
                                     variable_max = "",
                                     variable_sort = None,

                                     size = pas*10 ,)


    assert  taille == 0 , 'on  load un ID sur une plage ou il n est pas'
        

    # on croise date et ID_ref

    j = 5 # ID
    ID_min = ("0000"+ str(j)) [-4:] # il apparait une fois par ligne donc il a 10 variables
    ID_max = ("0000"+ str(j+1)) [-4:]


    i = 0
    pas = 5


    ID_reference_min = i 
    ID_reference_max = i + pas

    variable_min = 0
    variable_max = 2

    taille = len(ID_reference_base)
    variable_min_string = (ID_reference_base + str(variable_min))[-taille:]
    variable_max_string = (ID_reference_base + str(variable_max))[-taille:]

    index = "test"
    t = time.time()
    taille, hits = k.search_par_bloc (index,
                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = True,

                                     isID = True,
                                     ID_min = ID_min ,
                                     ID_max  = ID_max ,
                                     ID_sort  = 'asc',

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = variable_min_string,
                                     variable_max = variable_max_string,
                                     variable_sort = 'asc',

                                     size = pas*10 ,)


    assert taille == 0 , 'reference 0, 5 et ID 5, 6 et date_evenement 0, 2 taille ?'
        



    j = 5 # ID
    ID_min = ("0000"+ str(j)) [-4:] # il apparait une fois par ligne donc il a 10 variables
    ID_max = ("0000"+ str(j+1)) [-4:]




    i = 0
    pas = 5

    ID_reference_min = i 
    ID_reference_max = i + pas

    variable_min = 0
    variable_max = 2

    taille = len(ID_reference_base)
    variable_min_string = (ID_reference_base + str(variable_min))[-taille:]
    variable_max_string = (ID_reference_base + str(variable_max))[-taille:]

    index = "test"
    t = time.time()
    taille, hits = k.search_par_bloc (index,
                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'desc',
                                     isReference = True,

                                     isID = False,
                                     ID_min = ID_min ,
                                     ID_max  = ID_max ,
                                     ID_sort  = 'asc',

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = variable_min_string,
                                     variable_max = variable_max_string,
                                     variable_sort = 'desc',

                                     size = pas*10 ,)


    assert taille == 20 , 'ID_reference et date_evenement ne correspondent pas taille'
        
    liste_date_evenement = []
    liste_ID_reference = []

    for hit in hits :
        enreg = hit ['_source']
        ID_reference = enreg ['ID_reference']
        liste_ID_reference.append(ID_reference)

        date_evenement = enreg ['date_evenement']
        liste_date_evenement.append(date_evenement) 

        continue
    isFirst = True    
    for date, ID_reference in zip (liste_date_evenement, liste_ID_reference ) :
        if isFirst :
            date_courant, ID_reference_courant = date, ID_reference
            isFirst = False
        assert date  <= date_courant and ID_reference <= ID_reference_courant
        
        continue


    path  = '../data/generation/evenements1.txt'

    k.initRead(path)
    i = 0
    for liste in k.readIterator (sep = '|') :
        if len(liste) == 0 :
            break
        i += 1
        continue

    

    # test de search par date

    index = "test"
    t = time.time()

    variable_min = 1
    variable_max = 21

    taille = len(ID_reference_base)
    variable_min_string = (ID_reference_base + str(variable_min))[-taille:]
    variable_max_string = (ID_reference_base + str(variable_max))[-taille:]

    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = False,

                                     isID = False,
                                     ID_min = "",
                                     ID_max  = "",
                                     ID_sort  = 'asc',

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = variable_min_string,
                                     variable_max = variable_max_string,
                                     variable_sort = 'asc',

                                     size = pas*10 ,)


    assert taille == 200 , 'erreur dans search sur variable date_evenement'
    

    isFirst = True    
    for hit in hits :
        enreg = hit ['_source']
        date = enreg ['date_evenement']
        if isFirst :
            assert date == '000000000000000000000000000001'
            
            date_courante = date
            isFirst = False
            continue
        assert date >= date_courante , 'erreur de sens non asc'
        
        date_courante = date
        continue


    # test search par bloc temps X ID
    taille = len(ID_reference_base)
    # min
    i = 0
    ID_min = ("0000"+ str(i)) [-4:] 
    date_evenement_min = (ID_reference_base + str(i))[-taille:]

    ID_reference_min = (ID_reference_base  +str(i))[-taille:],

    #max
    i = 10
    ID_max = ("0000"+ str(i)) [-4:] 
    date_evenement_max = (ID_reference_base + str(i))[-taille:]

    ID_reference_max = (ID_reference_base  +str(i))[-taille:]






    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = False,

                                     isID = True,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = 'asc',

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = date_evenement_min,
                                     variable_max = date_evenement_max,
                                     variable_sort = 'asc',

                                     size = pas*10 ,)




    assert taille == 100 , 'erreur de taille dans la lecture par bloc date X ID'
    
    ID_reference_base = systeme ["ID_reference_base"]
    taille = len(ID_reference_base)
    isFirst = True
    numero_ligne = 0
    for hit in hits :
        doc = hit ['_source']
        i = int(numero_ligne/10)
        j = numero_ligne % 10
        dico = {
                      "ID" : ("0000"+ str(i)) [-4:] ,
                      "date_evenement" : (ID_reference_base + str(i))[-taille:],

                      "ID_reference" : (ID_reference_base  +str(i))[-taille:],

                       "nom_variable" : "variable_"+ str(j),
                       "valeur" : 1000000000000,
                }
        assert dico == doc , 'erreur de contenu dans le search bloc date x ID'
            
        numero_ligne += 1
        continue

    
    # test search par bloc ID_reference X ID
    taille = len(ID_reference_base)
    # min
    i = 0
    ID_min = ("0000"+ str(i)) [-4:] 
    date_evenement_min = (ID_reference_base + str(i))[-taille:]

    ID_reference_min = (ID_reference_base  +str(i))[-taille:],

    #max
    i = 10
    ID_max = ("0000"+ str(i)) [-4:] 
    date_evenement_max = (ID_reference_base + str(i))[-taille:]

    ID_reference_max = (ID_reference_base  +str(i))[-taille:]






    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = True,

                                     isID = True,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = 'asc',

                                     isVariable = False,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = date_evenement_min,
                                     variable_max = date_evenement_max,
                                     variable_sort = 'asc',

                                     size = pas*10 ,)





    assert taille == 100 , 'erreur de taille dans la lecture par bloc date X ID'
        

    ID_reference_base = systeme ["ID_reference_base"]
    taille = len(ID_reference_base)
    isFirst = True
    numero_ligne = 0
    for hit in hits :
        doc = hit ['_source']
        i = int(numero_ligne/10)
        j = numero_ligne % 10
        dico = {
                      "ID" : ("0000"+ str(i)) [-4:] ,
                      "date_evenement" : (ID_reference_base + str(i))[-taille:],

                      "ID_reference" : (ID_reference_base  +str(i))[-taille:],

                       "nom_variable" : "variable_"+ str(j),
                       "valeur" : 1000000000000,
                }
        assert  dico == doc , 'erreur de contenu dans le search bloc date x ID'
            
        numero_ligne += 1
        continue


    # test search par bloc temps X en limitant ID
    taille = len(ID_reference_base)
    # min
    i = 0
    i_ID = 2
    ID_min = ("0000"+ str(i_ID)) [-4:] 
    date_evenement_min = (ID_reference_base + str(i))[-taille:]

    ID_reference_min = (ID_reference_base  +str(i))[-taille:],

    #max
    i = 10
    ID_max = ("0000"+ str(i_ID + 1 )) [-4:] 
    date_evenement_max = (ID_reference_base + str(i))[-taille:]

    ID_reference_max = (ID_reference_base  +str(i))[-taille:]






    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = False,

                                     isID = True,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = 'asc',

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = date_evenement_min,
                                     variable_max = date_evenement_max,
                                     variable_sort = 'asc',

                                     size = pas*10 ,)





    assert taille == 20 , 'erreur de taille dans la lecture par bloc date X ID avec  limitation de ID'
        

    ID_reference_base = systeme ["ID_reference_base"]
    taille = len(ID_reference_base)
    isFirst = True
    numero_ligne = 0
    ID_cherche = ("0000"+ str(i_ID)) [-4:]
    ID_cherche_suivant  = ("0000"+ str(i_ID+1)) [-4:]
    for hit in hits :
        doc = hit ['_source']
        if doc ['ID']  != ID_cherche and doc ['ID']  != ID_cherche_suivant:
            print ('erreur de contenu dans le search bloc date x ID avec  limitation de ID')
            print (" voulu =", ID_cherche)
            print()
            print (' lu =', doc ['ID'])
            raise ValueError
        numero_ligne += 1
        continue



    # on test le count

    taille = k.count(index)

    assert taille == 100000 , 'erreur du count sur index lu='
        


    #  on essaye le count by search


    

    taille = len(ID_reference_base)
    # min
    i = 1
    i_ID = 2
    ID_min = ("0000"+ str(i_ID)) [-4:] 
    date_evenement_min = (ID_reference_base + str(i))[-taille:]



    #max
    i = 1
    i_ID = 2
    inc = 20
    ID_max = ("0000"+ str(i_ID + inc )) [-4:] 
    date_evenement_max = (ID_reference_base + str(i+inc))[-taille:]

    ID_reference_min = 0

    ID_reference_max = 1000

    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = True,

                                     isID = True,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = 'asc',

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = date_evenement_min,
                                     variable_max = date_evenement_max,
                                     variable_sort = 'asc',

                                     size = 100 ,

                                     )

    




    taille = len(ID_reference_base)
    # min
    i = 1
    i_ID = 2
    ID_min = ("0000"+ str(i_ID)) [-4:] 
    date_evenement_min = (ID_reference_base + str(i))[-taille:]



    #max
    i = 1
    i_ID = 2
    inc = 20
    ID_max = ("0000"+ str(i_ID + inc )) [-4:] 
    date_evenement_max = (ID_reference_base + str(i+inc))[-taille:]


    ID_reference_min = 12
    
    ID_reference_max = 1000

    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = True,

                                     isID = True,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = 'asc',

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = date_evenement_min,
                                     variable_max = date_evenement_max,
                                     variable_sort = 'asc',

                                     size = 100 ,

                                     )


    



    taille = len(ID_reference_base)
    # min
    i = 1
    i_ID = 2
    ID_min = ("0000"+ str(i_ID)) [-4:] 
    date_evenement_min = (ID_reference_base + str(i))[-taille:]



    #max
    i = 1
    i_ID = 2
    inc = 20
    ID_max = ("0000"+ str(i_ID + inc )) [-4:] 
    date_evenement_max = (ID_reference_base + str(i+inc))[-taille:]


    ID_reference_min = 0
    #print ('ID_reference_min =', ID_reference_min)
    ID_reference_max = 1000

    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = True,

                                     isID = True,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort = None,

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = date_evenement_min,
                                     variable_max = date_evenement_max,
                                     variable_sort = None,

                                     size =100 ,

                                     )


    



    #### ##########
    taille = len(ID_reference_base)
    # min
    i = 1
    i_ID = 2
    ID_min = ("0000"+ str(i_ID)) [-4:] 
    date_evenement_min = (ID_reference_base + str(i))[-taille:]



    #max
    i = 1
    i_ID = 2
    inc = 20
    ID_max = ("0000"+ str(i_ID + inc )) [-4:] 
    date_evenement_max = (ID_reference_base + str(i+inc))[-taille:]

    ID_reference_min = 0

    ID_reference_max = 1000

    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = False,

                                     isID = True,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = 'asc',

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = date_evenement_min,
                                     variable_max = date_evenement_max,
                                     variable_sort = 'asc',

                                     size = 100 ,

                                     )

    

    # on avance en prenant la derniere date 


    hit = hits [len(hits) - 1]
    enreg = hit ['_source']
    date_evenement_min = enreg ['date_evenement']


    taille = len(ID_reference_base)
    # min
    i = 1
    i_ID = 2
    ID_min = ("0000"+ str(i_ID)) [-4:] 
    hit = hits [len(hits) - 1]
    enreg = hit ['_source']
    date_evenement_min_int = int(enreg ['date_evenement'])
    date_evenement_min = (ID_reference_base + str(date_evenement_min_int + 1))[-taille:]



    #max
    i = 1
    i_ID = 2
    inc = 20
    ID_max = ("0000"+ str(i_ID + inc )) [-4:] 
    date_evenement_max = (ID_reference_base + str(i+inc))[-taille:]

    ID_reference_min = 0

    ID_reference_max = 1000000

    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = False,

                                     isID = True,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = 'asc',

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = date_evenement_min,
                                     variable_max = date_evenement_max,
                                     variable_sort = 'asc',

                                     size = 100 ,

                                     )

    


    hit = hits [len(hits) - 1]
    enreg = hit ['_source']
    date_evenement_min = enreg ['date_evenement']

    

    ######## data_fake

    index = 'data_fake_'

    # min

    ID_min = "couple_cadre_1"
    date_evenement_min = '2021-02-01 00:00:00'

    #     "couple_cadre_sup_0", "couple_cadre_sup_1"               
    #max

    ID_max = "couple_cadre_sup_1"
    date_evenement_max = '2021-02-20 00:00:00'

    ID_reference_min = 0
    ID_reference_max = 1000000

    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = False,

                                     isID = True,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = 'asc',

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = date_evenement_min,
                                     variable_max = date_evenement_max,
                                     variable_sort = 'asc',

                                     size = 100 ,

                                     )

    



    hit = hits [len(hits) - 1]
    enreg = hit ['_source']

    date_evenement_min = enreg ['date_evenement']
    #v = convertir ( date_evenement_min )
    r = date_evenement_min.split ('.')
    date_evenement_min = r[0]
    dateCourante = datetime.strptime(date_evenement_min, "%Y-%m-%d %M:%S:%f")
    timestamp = datetime.timestamp(dateCourante)
    timestamp +=1
    date_evenement_min = datetime.fromtimestamp(timestamp)

    taille, hits = k.search_par_bloc (index,

                                     ID,                     # inused Mais compatibilite oblige
                                     ID_reference_min,
                                     ID_reference_max ,
                                     ID_reference_sort = 'asc',
                                     isReference = False,

                                     isID = False,
                                     ID_min = ID_min,
                                     ID_max  = ID_max,
                                     ID_sort  = None,

                                     isVariable = True,
                                     nom_variableQuery = "date_evenement",
                                     variable_min = date_evenement_min,
                                     variable_max = date_evenement_max,
                                     variable_sort  = None,

                                     size = 100 ,

                                     )


    


    hit = hits [0]
    enreg = hit ['_source']
    date_evenementcourant = enreg ['date_evenement']

    for hit in hits :
        enreg = hit ['_source']
        date_evenement = enreg ['date_evenement']
        ID = enreg ['ID']
        variable = enreg ['nom_variable'] 





    isFirst = True
    for hit in hits :
        if isFirst :
            enreg = hit ['_source']
            ID_reference = enreg ['ID_reference']
            courant = ID_reference
            continue

        enreg = hit ['_source']
        ID_reference = enreg ['ID_reference']
        
        assert courant <= ID_reference , 'erreur de tri sur ID_reference' 
            
        courant= enreg ['ID_reference']
        continue

    


if __name__ == '__main__' :
    test_kernel_general ()
    print ('Fin du test')


        
   
