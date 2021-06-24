# coding: utf-8
##### coding: utf-8
import bz2 
import lzma
import gzip 
from datetime import datetime, timedelta
from random import randint
import numpy as np

from elasticsearch import Elasticsearch 
from elasticsearch.connection import Urllib3HttpConnection
from elasticsearch.helpers import bulk

class rien () :
    def compress (self, x) :
        return x
    def decompress (self, x) :
        return x



class Kernel () :
    def __init__ ( self, dico, dispersion = 1000000) :
        '''
        
                  createur = "generic", 
                  date_emetteur = datetime.now(),
                  http_auth = None,
                  timeout=10,
                  host = "localhost", 
                  port = 9200 ,
                  zipChoisi = 'bz2',
                  index_log_error = "trace1",
                  index_log_warning = "trace2",
                  index_log_trace = "trace3",
                  index_system = "systeme",
                  isPurge_existing_index_log = True,
                  extra_elasticsearch_args = None,
                  trace = False,
                  FF
        
        ######### centralise les I/O #########
        en entree 
        le createur du process (esemble de taches) 
        la date de lancement par defaut ce jour
        
        ensuite
        pour elastic : host, port
        pour le zip : le choix par nom if none on ne fait rien,
        
        ensuite pour debug la trace (log elastic)
        '''
        self.dispersion = int(dispersion)
        
        self.createur = dico ["createur"]
        date_emetteur = dico ["date_emetteur"]
        http_auth = dico ["http_auth"]
        timeout = dico ["timeout"]
        host = dico ["host"]
        port = dico ["port"]
        zipChoisi = dico ["zipChoisi"]
        index_log_error = dico ["index_log_error"]
        index_log_warning = dico ["index_log_warning"]
        index_log_trace = dico ["index_log_trace"]
        index_system = dico ["index_system"]
        isPurge_existing_index_log = dico ["isPurge_existing_index_log"]
        extra_elasticsearch_args = dico ["extra_elasticsearch_args"]
        trace = dico ["trace"]
        #modif ##########################################"
        self.ID_reference_base = dico ["ID_reference_base"]
        
        self.lecture_evenements = "../data/generation/evenements1.txt" # modif client dico ['lecture_evenements']
        
        
        self.date_emetteur = date_emetteur
        self.trace = trace
        
        self.index_log_error = index_log_error
        self.index_log_warning = index_log_warning
        self.index_log_trace = index_log_trace
        self.isPurge_existing_index_log = isPurge_existing_index_log
        
        
        
        self.host = host
        self.port = port
        self.http_auth = http_auth
        self.timeout = timeout
        
        if extra_elasticsearch_args is None:
            extra_elasticsearch_args = {}
        self.extra_elasticsearch_args = extra_elasticsearch_args
         
        
        self.es = Elasticsearch(
                        connection_class = Urllib3HttpConnection, # fonction externe
                        host=self.host,
                        port=self.port,
                        http_auth=self.http_auth, # donne pour authentification
                        timeout=self.timeout,
                        **self.extra_elasticsearch_args,
                        )
        
        
        # init du system
        self.index_system = index_system
        index = index_system
        if isPurge_existing_index_log or not self.es.indices.exists(index=index):
            self.delete_index (index)
            self.create_index (index)
            # init date pour recuperer les logsdate = datetime.datetime.now() mis dans creationDoc
            doc = self.creationDoc ("systeme", "kernel", "init",  "pour recuperer les logs",)
            self.index_doc (doc, index, _id = 1 )
        
        # intialisation compression de données voir pb "byte to string et inversement"        
        self.dicoZip = {'bz2' : bz2,
                  'lzma' : lzma,
                   'gzip' : gzip,
                        }
        self.initZip (zipChoisi = zipChoisi)
        
        
        
               
        # pour la lemmatization       
        
        self.liste_type = ['NOM', 'AUX', 'VER', 'ADV', 'PRE', 'ADJ', 'ONO', 'CON',
                  'ART:def', 'ADJ:ind', 'PRO:ind', 'PRO:int', 'PRO:rel',
                  'ADJ:num', 'PRO:dem', 'ADJ:dem', 'PRO:per', 'ART:ind',
                  'LIA', 'PRO:pos', 'ADJ:pos', '', 'ADJ:int']
        
        self.index_regroupement = "regroupement"
        
        self.settings_regroupement = { "settings" : {
                                      'index.mapping.total_fields.limit':100000,
                                     }
        }
        
        self.dico_settings = {'regroupement' : self.settings_regroupement ,
                             }
                              
                              
        
        self.structure_du_lexique = ["1_ortho" , 
                                     "3_lemme" , 
                                     "4_cgram" , 
                                     "5_genre" , 
                                     "6_nombre" , 
                                     "7_freqlemfilms2" , 
                                     "8_freqlemlivres" , 
                                     "9_freqfilms2" , 
                                     "10_freqlivres" , 
                                     "11_infover" , 
                                     "12_nbhomogr" , 
                                     "13_nbhomoph" , 
                                     "14_islem" , 
                                     "15_nblettres" , 
                                     "19_voisorth" , 
                                     "21_puorth" , 
                                     "22_puphon" , 
                                     "29_cgramortho" , 
                                     "30_deflem" , 
                                     "31_defobs" , 
                                     "32_old20" , 
                                     "33_pld20" , 
                                     "35_nbmorph" , 
                                    ]
        

        
        self.debut_fichier_regroupement = "../../../data/Lexique383_group" # a voir
        
    @property
    def raise_on_error(self):
        """
        Renvoyer False pout permettre à l'appelant de gérer le log d'erreur
        dans le cas du bulk
        """
        return False
    
    @property
    def mapping_log(self,) :
        """
        Dictionary with custom mapping or `None`.
        probleme avec Elastic sur le mapping ??????????
        """
        return None
        
    @property
    def mapping(self):
        """
        Dictionary with custom mapping or `None`.
        probleme avec Elastic sur le mapping ??????????
        """
        mapping =  {
                        "properties": {
                            "ID": {
                                "type": "keyword" # formerly "string"
                            },
                            "ID_reference": {
                                "type": "keyword"
                            },
                            "date_evenement": {
                                "type": "keyword"
                            },
                            "nom_variable": {
                                "type": "keyword"
                            },
                            "valeur" : {
                                "type" : "keyword"
                            }
                        }
                    }
                
        
        return mapping
    
    @property
    def mapping_vecteur(self):
        """
        Dictionary with custom mapping or `None`.
        
        """
        mapping =  {
                        "properties": {
                            "ID": {
                                "type": "integer" 
                            },
                            "ID_random": {
                                "type": "integer"
                            },
                            "vecteur": {
                                "type": "float"
                            },
                            "paragraphe": {
                                "type": "keyword"
                            }
                        }
                    }
                
        
        return mapping
    
    def liste2array(self, data,dtype = np.int32) :
        return np.array(data, dtype = dtype)
    
    def array2liste (self,array,):
        return array.tolist()
        
    
    
    
       
    def compression (self, data) :
        return self.zip.compress (data)
    
    def decompression (self, dataCompresse) :
        return self.zip.decompress (dataCompresse)
    
    def initZip (self, zipChoisi = None ) :
        if zipChoisi is None :
            self.zip = rien()
        else:
            self.zip = self.dicoZip[zipChoisi]
            
    def create_index(self, index):
        """
        creation de l' index si il n'existe pas.
        """
        
        if not self.es.indices.exists(index=index):
            self.es.indices.create(index=index)
            
    def delete_index(self, index):
        """
        Supprime l'index, si il existe.
        """
        
        if self.es.indices.exists(index=  index):
            self.es.indices.delete(index = index)
            
    def _docs_vecteur (self, docIterator, index) :
        dico = {'_index' : index, }
        for doc in docIterator :
            doc ['ID_random'] = randint (0,self.dispersion)
            dico ['_source'] = doc
            yield dico
        return
            
    
            
    def _docs (self, docIterator, index) :
        dico = {'_index' : index,}
        for doc in docIterator :
            dico ['_source'] = doc
            yield dico
        return
    
    def bulk_vecteur (self,
                      docs,
                      index,
                      isPurge_existing_index = False,
                      chunk_size = 2000,
                     ):
        """
        
        docs est un iterateur comme son nom ne l'indique pas
        
        """
        
        
        if isPurge_existing_index:
            self.delete_index(index) # si existe detruit
            
        self.create_index(index) # si existe ne fait rien
        
        if not self.mapping_vecteur is None and isPurge_existing_index:
                self.es.indices.put_mapping(index = index, body = self.mapping_vecteur)
        
        self.es.indices.put_settings({"index": {"refresh_interval": "-1"}},
                                    index= index)

        bulk(self.es, self._docs_vecteur (docs, index) , chunk_size = chunk_size,
                  raise_on_error=self.raise_on_error) # en cas d'erreur on renvoie False

        self.es.indices.put_settings({"index": {"refresh_interval": "1s"}},
                                         index = index)
        self.es.indices.refresh()
        
        return True # tout est OK
    
    
       
    def bulk (self, docs, index,
              isPurge_existing_index = False,
              chunk_size = 2000,
             ):
        """
        
        docs est un iterateur comme son nom ne l'indique pas
        
        """
        mapping = self.mapping
        #print ("mapping =", mapping)
        
        if isPurge_existing_index:
            self.delete_index(index) # si existe detruit
            
        self.create_index(index) # si existe ne fait rien
        
        if not mapping is None and isPurge_existing_index:
            #print ("mapping =", mapping)
            self.es.indices.put_mapping(index = index, body = mapping)
        
        self.es.indices.put_settings({"index": {"refresh_interval": "-1"}},
                                    index= index)

        bulk(self.es, self._docs (docs, index) , chunk_size = chunk_size,
                  raise_on_error=self.raise_on_error) # en cas d'erreur on renvoie False

        self.es.indices.put_settings({"index": {"refresh_interval": "1s"}},
                                         index = index)
        self.es.indices.refresh()
        
        return True # tout est OK 
    
    def count (self, index) :
        if not self.es.indices.exists(index=  index):
            return 0
        
        self.es.indices.refresh(index)
        r = self.es.cat.count(index, params={"format": "json"})
        return int (r [0] ['count'])
    
    # exemple de query sur les mots pour trouver les lemmes
    def search_mot (self, index, mot, zone) :
        self.es.indices.refresh (index)
        query = {'query' : {'match' : {zone : mot}}}
        #print ("query =", query )
        res= self.es.search (index= index, body = query )
        #res = self.elastic.search(index=index , body={"query": {"match_all": {}}})
        #print ([hit['_source'] for hit in res ['hits'] ['hits']])
        return [hit['_source'] for hit in res ['hits'] ['hits']]
    
    def creationDoc (self,origine, auteur, etape,  message,) :
               
        return {"origine": origine,
               "auteur" : auteur,
                "etape" : etape,
                  "date" : datetime.now(),
                   "message" : message, }
        
    
    def log_error (self, auteur, etape,  message,) :
        index = self.index_log_error
        doc = self.creationDoc ("error", auteur, etape,  message,)
        return self.index_doc (doc, index,)
    
    def log_warning (self, auteur, etape,  message,) :
        index = self.index_log_warning
        doc = self.creationDoc ("warning", auteur, etape,  message,)
        return self.index_doc(doc, index,  )
        
    def log_trace (self, auteur, etape, message,  messagesStop = False) :
        index = self.index_log_trace
        doc = self.creationDoc ("trace", auteur, etape,  message,)
        return self.index_doc (doc, index)
        
    def index_doc (self,doc, index, _id = None):
        # on index l'erreur
        if _id is None :
            res = self.es.index (index = index, body = doc)
        else :
            res = self.es.index (index = index, id = _id, body = doc)
        
        self.es.indices.refresh()
        #print ( "dans ecriture erreur res =", res['result'])
        return True # tout est OK
    
    def get_date_system (self,) :
        res = self.es.get(index=self.index_system, id=1)
        doc = res['_source'] 
        return  doc ['date']

    
    
    def get_logs_error (self,) :
        return self.get_logs(self.index_log_error)
    def get_logs_warning (self,) :
        return self.get_logs(self.index_log_warning)
    def get_logs_trace(self,) :
        return self.get_logs(self.index_log_trace)
    
    def get_logs (self, index, size = 10000) :
        
        self.es.indices.refresh (index)
        
        date_system = self.get_date_system ()
        query = {'query' : {'range' : {"date": {"gte" : date_system}}} }
        #print ("query =", query )
        res= self.es.search (index= index, body = query,  size = size )
        #res = self.elastic.search(index=index , body={"query": {"match_all": {}}})
        #print ([hit['_source'] for hit in res ['hits'] ['hits']])
        return [hit['_source'] for hit in res ['hits'] ['hits']]
    
    def calculRandom_vecteur (self, proportion, index,) :
        """
        apres avoir randomiser la variable IDrandom (bulk_vecteur) entre 0 et self.dispersion
        on calcul en fonction de la proportioon voulu des bornes inferieure et superieure
        qui encadreront la recherche dans l-index qui contiend les vecteurs/paragraphes
        """
                
        nombreElements = self.count (index)
        nombreElements_voulu = int ((proportion * nombreElements)/100.)
        borne_inferieur_max = (nombreElements - nombreElements_voulu)
        
        borne_inferieur_random = randint (0, borne_inferieur_max)
        borne_superieur = borne_inferieur_random + nombreElements_voulu
        # en proportion
        borne_inferieur_random = int((borne_inferieur_random*self.dispersion)/nombreElements)
        borne_superieur = int((borne_superieur*self.dispersion)/nombreElements)
        return borne_inferieur_random, borne_superieur
        
        
    
    def search_par_bloc_vecteur(self,
                                 index,
                                 isVecteur = True,
                                 isParagraphe = False,
                                 ID_random_min = 0,
                                 ID_random_max = 0,
                                 isRandom = True,

                                 isID = False,
                                 ID_min = "",
                                 ID_max  = "",
                                 ID_sort  = 'asc',
                                 


                                 size = 1000 ,

                                ) :
        
        
        _source = ['ID',]
        if isVecteur: 
            _source .append( 'vecteur')
        if isParagraphe :
            _source.append('paragraphe')
            
                
        
        listeMust = []
        listeSort = []
        
             
        
        if isRandom :
                  
            listeMust.append({ "range" : {
                                    "ID_random" : {
                                        "gte" :ID_random_min,
                                        "lt" : ID_random_max,
                                                    },
                                    },
                              })
                    
        if isID :
            rangeID = { "range" : {
                                    "ID" : {
                                        "gte" :ID_min,
                                        "lte" : ID_max,
                                                    },
                                    },
                              }
            
            
            listeMust.append (rangeID)
            
            
        
        if not ID_sort is None :
            sort = {'ID' : {'order' : ID_sort},}
            listeSort.append(sort)
        
        
        
        query = {'_source': _source,
                      "query": {'bool': {'must': listeMust,
                                        },},
                                                    
                       "sort" : listeSort,
                    }
                        
                    

            
        
        
        
        
        #print (index, " et ",query, 'pour size =', size)
        res = self.es.search (index = index, body = query , size = size)
        hits = res['hits']
        nombre= hits['total'] ['value']
        vrai_hits= hits['hits']
                   
        return nombre, vrai_hits
    
    
    
    def search_par_bloc (self,
                         index,
                         
                         ID,                     # inused Mais compatibilite oblige
                         ID_reference_min,
                         ID_reference_max ,
                         ID_reference_sort = 'asc',
                         isReference = True,
                         
                         isID = False,
                         ID_min = "",
                         ID_max  = "",
                         ID_sort  = 'asc',
                         
                         isVariable = False,
                         nom_variableQuery = None,
                         variable_min = "",
                         variable_max = "",
                         variable_sort = 'asc',
                         _source = None,
                         
                         size = 10000 ,
                         
                        ) :
        
        #modif ################################################
        # warning toujours encadre par ID reference (à mettre au pas.....)
        #         ascendant ou descendant est une propriete de chaque variable
        listeMust = []
        listeSort = []
        
        
        
        
        if isReference :
            taille = len (self.ID_reference_base)
            ID_reference_min_string  = (self.ID_reference_base + str(ID_reference_min) ) [-taille:]
            ID_reference_max_string  = (self.ID_reference_base + str(ID_reference_max) ) [-taille:]
            
            listeMust.append({ "range" : {
                                    "ID_reference" : {
                                        "gte" :ID_reference_min_string,
                                        "lt" : ID_reference_max_string,
                                                    },
                                    },
                              })
        
        if not ID_reference_sort is None :
            sort = {'ID_reference' : {'order' : ID_reference_sort},}
            listeSort.append(sort)
            
        
        
        
        if isVariable :
            
            
            rangeVariable = { "range" : {
                                    nom_variableQuery : {
                                                    "gte" :variable_min,
                                                    "lt" : variable_max,
                                                                },
                                    },
                              }
            listeMust.append (rangeVariable)
            
        if not variable_sort is None :
            
            sort = {nom_variableQuery : {'order' : variable_sort},}
            listeSort.append(sort)
            
            
            
            
                
        if isID :
                           
            rangeID = { "range" : {
                                    "ID" : {
                                        "gte" :ID_min,
                                        "lte" : ID_max,
                                                    },
                                    },
                              }
            
            
            listeMust.append (rangeID)
            
            
        
        if not ID_sort is None :
            sort = {'ID' : {'order' : ID_sort},}
            listeSort.append(sort)
        
        
        if _source is None :
            query = {"query": {'bool': {'must': listeMust,
                                        },},
                  "sort" : listeSort,
                    }
        else :
            query = {'query' : query,
                     '_source' : _source}
        
            
        
        
        
        
        #print('dans la classe, query =', query)
        
        res = self.es.search (index= index, body = query , size = size)
        hits = res['hits']
        nombre= hits['total'] ['value']
        vrai_hits= hits['hits']
        return nombre, vrai_hits 
    
    def tri (self, hits) :
        liste = []
        i = 0
        for data in hits :
            x = data ['_source'] ['ID_reference']
            liste.append([i, x])
            i += 1
            continue

        liste_trie = sorted (liste, key = lambda d  : (d[1], d[0]) )

        liste_hits_trie = []
        for numero, _ in liste_trie :
            data = hits [numero]
            liste_hits_trie.append(data)
            continue

        return liste_hits_trie
        
    
    
    def close (self,) :
        
        self.es.indices.refresh()       
        self.es.close()
        
        return
    
      

    
