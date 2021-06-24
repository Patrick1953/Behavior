# coding: utf-8
import json, sys 
import pprint as p
from datetime import datetime
from validationPath import validationPath


  




dico_lock = {'isSoft' : False, 
            'time_out' : 10,
            }


dico_commandes = {'en_tete' : 'commande_',
                  'pathFile' : "echanges/commandes.json",
               }

dico_reponses = {'en_tete' : 'reponse_',
                 'pathFile' : "echanges/reponses.json",
                }



dico_receveur =  {'nom_receveur' : 'test',
                  'temps_attente' :1,
                  'isTest' : True,
                  }

dico_executeur = {'nom_executeur' : 'test',
                  'temps_attente' : 1,
                  'isTest' : True,}






dico_evenements =  {
    
'alimentation' : {
    
    
    
    
    'execution' : {
            'dico_ajout' : {},# {"date_execution type '2021-02-01 00:00:00':{ date_debut, date_fin, numero_ligne..}  }
            'date_debut_alimentation' : '2021-02-01 00:00:00',
            
            'taille_globale' : [0, 0], # en nombre de lignes
            'index_data': 'data_fake',
            'nombre_erreur_max'  : 0,
                    },
                },
    
    

               

    




# decrit les executions par type de pas

'pas' : {'demi_jour' : {'liste_execution' : [] , },
        },
    
'apprentissage' : {'liste_execution' : [], # liste dico qui decrit un calcul quantile
                   
                   },

'type': {'ID': {'format': 'standard','type': 'string'},
          'date_evenement': {'format': 'standard', 'type': 'date'},
          'description': {'format': 'standard','type': 'string'},
          'nomenclature_1': {'format': 'standard','type': 'string'},
          'nomenclature_2': {'format': 'standard','type': 'string'},
          'nomenclature_3': {'format': 'standard','type': 'string'},
          'nomenclature_4': {'format': 'standard','type': 'string'},
          'prix': {'format': 'standard','type': 'numeric'},
          'prix_panier': {'format': 'standard','type': 'numeric'}},

'position': {'ID': 0,
          'date_evenement': 1,
          'description': 7,
          'nomenclature_1': 3,
          'nomenclature_2': 4,
          'nomenclature_3': 5,
          'nomenclature_4': 6,
          'prix': 8,
         'prix_panier': 2},

'creation_dictionnaire' : {'ID' : {'travail' : None,
                                'parametres' : []},
                            'date_evenement' : {'travail' : 'date',
                                                'parametres' : []},

                            'description': {'travail' : 'analyse_mot',
                                                'parametres' : [{'format': 'standard', },]},

                              'nomenclature_1':{'travail' : 'analyse_mot',
                                                'parametres' : [{'format': 'standard', },]},

                              'nomenclature_2': {'travail' : 'analyse_mot',
                                                'parametres' : [{'format': 'standard', },]},

                              'nomenclature_3': {'travail' : 'analyse_mot',
                                                'parametres' : [{'format': 'standard', },]},

                              'nomenclature_4': {'travail' : 'analyse_mot',
                                                'parametres' : [{'format': 'standard', },]},

                        'prix': {'travail' : 'quantile',
                                'parametres' : [{'type' : 'quartile'},
                                                           {'type' : 'decile',},
                                                           {'type': 'manuel',
                                                             'nom_manuel' : 'manuel1',
                                                            'separateurs' : [10., 20.,100.] } 
                                                           ],
                                                           },


                      'prix_panier': {'travail' : 'quantile',
                                      'parametres' : [{'type' : 'quartile'},],
                                     },

           },
'dictionnaire' : {'ID' : {'travail' : None,
                                'parametres' : []},
                        'date_evenement' : {'travail' : 'date',
                                            'parametres' : [{'type' : 'demi_jour'},
                                                           {'type' : 'jour'},
                                                            {'type' : 'semaine'},
                                                            {'type' : 'mois'},
                                                            {'type' : 'annee'},
                                                            {'type' : 'ferie'},
                                                           ]},

                        'description': {'travail' : 'analyse_mot',
                                            'parametres' : [{'type' : 'standard'}]},

                          'nomenclature_1':{'travail' : 'analyse_mot',
                                            'parametres' : [{'type' : 'standard'}]},

                          'nomenclature_2': {'travail' : 'analyse_mot',
                                            'parametres' : [{'type' : 'standard'}]},

                          'nomenclature_3': {'travail' : 'analyse_mot',

                                              'parametres' : [{'type' : 'standard'}]},

                          'nomenclature_4': {'travail' : 'analyse_mot',
                                            'parametres' : [{'type' : 'standard'}]},


                        'prix': {'travail' : 'quantile',
                                'parametres' : [{'type' : 'quartile'},
                                                           {'type' : 'decile',},
                                                           {'type': 'manuel',
                                                             'nom_manuel' : 'manuel1',
                                                            'separateurs' : [10., 20.,10.] } 
                                                           ],
                                                           },


                      'prix_panier': {'travail' : 'quantile',
                                      'parametres' : [{'type' : 'quartile'},],
                  'en_tete' : 'commande_', 
                               'pathFile' : '../data/test/commandes.json'                   },

           },
}
              
    
    
dico_systeme = {
    
    
    

                            
                                 

'environnement' : {'test' : {'parametres_lecture' : {'path_fichier' : '../data/test/data_alimentation/',
                                                     'separateur' : "|",
                             
                                                     'parametres_execution' : {'type_lecteur' : 'fichier',
                                                                              },
                                                    },
                                                    
                              'parametres_ecriture' : {'path_sortie' : '../data/data_sortie/test/',
                                                     'parametres_execution' : {'type_lecteur' : 'fichier',},
                                                     },
                        },
                  },
                         
                           
            
    
'calcul' : {
        'format_date_standard' : '%Y-%m-%d %H:%M:%S.%f',
        'format_string_standard' : "",
        'format_float_standard' : 1.0,
           
        'nombre_ID_par_bloc' : 2, #  >1
        'nombre_bloc_date' : 3,
        'nombre_ID_pour_apprentissage' : 50000,
    
        'taille_bloc' : 100,   # nombre de ligne à lire à chaque appel de ES
        'pourcentage_echantillon' : 100.0 , # permet de faire un echantillon pour apprentissage model
        },




# parametres du Reseau de Neurones

'embedding' : {'vector_size' : 100,
                 'alpha' : 0.025,
                 'min_alpha' : 0.00025,
                 'min_count' : 1,
                 'dm' : 1,
                 'max_epoch' : 10,
                 'decrease_alpha' : 0.0002,
                 'isOublie' : False,
                 
                },


    
'elasticsearch' : {  
          "createur" : "generic", 
          "date_emetteur" : str(datetime.now()),
          "ID_reference_base" : "000000000000000000000000000000",
          "http_auth" : None,
          "trace" : False,
                  
          "timeout" : 10,
          "host" : "localhost", 
          "port" : 9200 ,
          "zipChoisi" : 'bz2',
           "index_log_error" : "trace1",
           "index_log_warning" : "trace2",
            "index_log_trace" : "trace3",
            "index_system" : "systeme",
            "isPurge_existing_index_log" : False,
            "extra_elasticsearch_args" : None,
             
     

                        },

}
                            
                   


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
        
def  ecriture (isApprentissage = False ):         
        
        
    nom_environnement = "test"        
    path = '../data/'+ nom_environnement + '/parametres/'        
    validationPath (path)

    path_general =  '../data/general/parametres/'
    #path_general =  '../data/'+ nom_environnement + 'parametres/' 
    validationPath (path_general)       




    string = json.dumps (dico_lock)
    pathFile = path_general + "dico_lock.json"
    f = open (pathFile, "w")
    f.write (string)
    f.close()        

    string = json.dumps (dico_receveur)
    pathFile = path_general + "dico_receveur.json"
    f = open (pathFile, "w")
    f.write (string)
    f.close()         

    string = json.dumps (dico_executeur)
    pathFile = path_general + "dico_executeur.json"
    f = open (pathFile, "w")
    f.write (string)
    f.close() 

    string = json.dumps (dico_commandes)
    pathFile = path_general + "dico_commandes.json"
    f = open (pathFile, "w")
    f.write (string)
    f.close()


    string = json.dumps (dico_reponses)
    pathFile = path_general + "dico_reponses.json"
    f = open (pathFile, "w")
    f.write (string)
    f.close()



    string = json.dumps (dico_evenements)
    pathFile = path + "dico_evenements_2.json"
    f = open (pathFile, "w")
    f.write (string)
    f.close()                



    string = json.dumps (dico_systeme)
    pathFile = path + "dico_systeme_2.json"

    f = open (pathFile, "w")
    f.write (string)
    f.close() 


    if isApprentissage :


        path = "../Apprentissage"
        if path not in sys.path :
            sys.path.append (path)
        from Apprentissage import Apprentissage

        nom_environnement = 'test'
        pathFile_evenements = '/dico_evenements_2.json'
        pathFile_systeme = '/dico_systeme_2.json'

        arg = {}
        arg ['isTrace'] = False
        arg ['nom_environnement'] = nom_environnement

        arg ['variable_min'] = '2021-02-01 00:00:00'
        arg ['variable_max'] = '2021-02-09 00:00:00'

        A = Apprentissage (arg)
        A.run()
        
if __name__ == '__main__' :
    ecriture ()
    print ('end_of_job')
