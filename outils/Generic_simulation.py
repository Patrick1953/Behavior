# coding: utf-8
import  os, sys, json, luigi, time, copy
from datetime import datetime

from Kernel_BE import Kernel
from Parametres import Parametres       
        

        
            
    
'''
###### self.get_execution() est fourni par l'utilisateur (la tache principale)
#exemple__________________def get_execution (self) :
#        
#                             self.appels = {'appel' : MyTask,
#                                           'type_repetition' : 'ID',
#                                           }
#                             return
#   permet de fournir les parametres pour les appels distribution par variables, bloc ou ID
#   si appel is None alors pas d'appel 
#
###### self.nom_entree permet à requires de fournir le nombre d appels
#                                        pour self.input [i] for i in range(nom_entree)
#                                        
# attention il est possible de choisir dans output un nom de fichier qui est le meme 
# que ceux des taches paralleles (luigi recupere les noms de fichier pour  self.input [i].open...
#______________ l'ordre semble etre respecté meme si dans cce cas cela n'a aucun interet
#
# pour les descriptions de arg_kernel et arg_travail voir les documents d' architure
# mais le format est du texte (json) compatibilité simple avec luigi sans perte de perf


le code est equivallent entre simulation et Generic

'''            


class Generic_simulation ():
    
    def __init__(self, arg_travail = "" ) :
        
        
        self.arg_travail = arg_travail
        
    def run (self,) :
        """
        run generique
         - pour les traces et gesion des erreurs
         - appel run_tache fournit par  la classe dependante
        """
        # on trace 
        createur = self.arg_kernel_data ['createur']
        etape = self.arg_travail_data ['etape']
        message_trace = "depart de la tache : " + self.nom_tache_luigi 
        self.kernel.log_trace (createur, etape,  message_trace)
                
        # on execute la tache
        t = time.time()
        try :
            self.get_travail ()
            message = self.run_tache()
        except Exception as e:
            createur = self.arg_kernel_data ['createur']
            etape = self.arg_travail_data ['etape']
            message = "erreur de la tache : " + self.nom_tache_luigi + ' du type '+ str(e.args)
            self.kernel.log_error (createur, etape,  message)
            
        duree = time.time() - t
        # on trace la fin
        createur = self.arg_kernel_data ['createur']
        etape = self.arg_travail_data ['etape']
        message_trace = "fin de la tache : " + self.nom_tache_luigi + ' en ' + str(duree)
        self.kernel.log_trace (createur, etape,  message_trace)
        
        # on marque la fin
        # dans le cas de recuperation du travail des taches required
        # on doit jouer sur les differents self.input qui ouvre les fichiers trvud
        
        return message
    
            

    
    def get_travail (self,) :
        self.arg_travail_data = json.loads (self.arg_travail)
        
        try :
            a = self.dico_evenements
        except :
            pathDicoEvenements = self.arg_travail_data ['pathDico_evenements']
            self.dico_evenements = Parametres (pathDicoEvenements, [])
            
        
        try :
            a = self.dico_systeme
        except:
            pathDico_systeme = self.arg_travail_data ['pathDico_systeme']
            self.dico_systeme = Parametres (pathDico_systeme, [])
            
            # on recupere le kernel
            self.arg_kernel_data = self.dico_systeme ['elasticsearch']
            self.kernel = Kernel (self.arg_kernel_data)
            
                   
        
        return
    
    def run_tache (self,) :
        return
    
        
    

    
    def get_execution(self,) :
        self.appels = {'appel' : None, 'type_repetition' : None}
        auteur = 'Generic'
        etape = "pas de garantie de fonctionnement"
        message = "la tache n'a pas de fonction get_execution  ????"
        self.kernel.log_warning (auteur, etape,  message)
                
        
    def requires(self):
                 
        # initialisation
        self.get_travail ()
        self.get_execution()
                
        appel = self.appels ['appel']
        type_repetition = self.appels ['type_repetition']
        
        if appel is None :
            self.nombre_appels = 0
            return []
        
           
        
        if type_repetition == "date_evenement" :
            
            liste_bloc_date = self.get_liste_dates ()
                       
            
            liste_requires = []
            
            arg_travail_local = copy.deepcopy (self.arg_travail_data)
            self.liste_requires = []
            for date_debut, date_fin in liste_bloc_date :
                arg_travail_local ['variable_min'] = date_debut
                arg_travail_local ['variable_max'] = date_fin
                arg_travail1 = json.dumps (arg_travail_local)
                travail = appel (arg_travail = arg_travail1, )
                
                liste_requires.append (travail)
                
                continue
            self.nombre_appels = len(liste_requires)
            return liste_requires 
        
        if type_repetition == "ID" :
                        
            liste_blocs_ID = self.get_liste_blocs_ID ()
            arg_travail_local = copy.deepcopy (self.arg_travail_data)
            
            liste_requires = []
            
            for ID_reference_min, ID_reference_max in liste_blocs_ID  :
                
                arg_travail_local ['ID_min'] = ID_reference_min
                arg_travail_local ['ID_max'] = ID_reference_max
                
                arg_travail1 = json.dumps (arg_travail_local)
                travail = appel (arg_travail = arg_travail1, )
                
                liste_requires.append (travail)
                
                continue
                
            self.nombre_appels = len(liste_requires)
            return liste_requires
                  
        raise ValueError
        
        
    
    
    def get_liste_blocs_ID (self,) :
        
        path_liste_ID = self.arg_travail_data['pathListe_ID']
        
        f = open (path_liste_ID, 'r')
        liste = f.read ()
        f.close()
        liste = json.loads(liste)
        taille_liste_ID = len(liste)
        
        nombre_bloc_ID = self.dico_systeme ['calcul'] ['nombre_bloc_ID']
        taille_bloc_ID = int(taille_liste_ID/nombre_bloc_ID)
        
        resultat = []
        debut = 0
        fin = taille_bloc_ID
        while (True) :
            if fin >= taille_liste_ID - 1 :
                fin = taille_liste_ID - 1
                resultat.append ([liste [debut], liste[fin]])
                break
            resultat.append ([liste [debut], liste[fin]])
            debut = fin + 1
            fin = fin + taille_bloc_ID 
            continue
        
        return resultat
    
    def timestamp (self, date) :
        d = datetime.strptime(date, self.format_date_standart)
        return datetime.timestamp(d)
        
        
    
    def get_liste_dates (self,) :
        date_debut = self.arg_travail_data ['variable_min']
        date_fin = self.arg_travail_data ['variable_max']
        self.format_date_standart = self.dico_systeme ['calcul']['format_date_standard']
        
        date_debut_timestamp = self.timestamp (date_debut)
        date_fin_timestamp = self.timestamp (date_fin)
        
        nombre_bloc_date = self.dico_systeme ['calcul'] ['nombre_bloc_date']
        
        timedelta = (date_fin_timestamp - date_debut_timestamp) / nombre_bloc_date
        
        resultat = []
        time_debut = date_debut_timestamp
        time_fin = date_debut_timestamp + timedelta
        
        while (True) :
            if time_fin >= date_fin_timestamp :
                d1  = str(datetime.fromtimestamp(time_debut) )
                d2 =   str(datetime.fromtimestamp(time_fin) )
                resultat.append ([d1, d2])
                break
            d1  = str(datetime.fromtimestamp(time_debut) )
            d2 =   str(datetime.fromtimestamp(time_fin) )
            resultat.append ([d1, d2])
            
            time_debut = time_fin
            time_fin = time_fin + timedelta
            continue
        return resultat
                          
                          
                          
                
class Generic (luigi.Task):
    
    
        
    def run (self,) :
        """
        run generique
         - pour les traces et gesion des erreurs
         - appel run_tache fournit par  la classe dependante
        """
        # on trace 
        createur = self.arg_kernel_data ['createur']
        etape = self.arg_travail_data ['etape']
        message_trace = "depart de la tache : " + self.nom_tache_luigi 
        self.kernel.log_trace (createur, etape,  message_trace)
                
        # on execute la tache
        t = time.time()
        try :
            self.get_travail ()
            message = self.run_tache()
        except Exception as e:
            createur = self.arg_kernel_data ['createur']
            etape = self.arg_travail_data ['etape']
            message = "erreur de la tache :" + self.nom_tache_luigi + ' du type ' + str(e.args)
            self.kernel.log_error (createur, etape,  message)
            
        duree = time.time() - t
        # on trace la fin
        createur = self.arg_kernel_data ['createur']
        etape = self.arg_travail_data ['etape']
        message_trace = "fin de la tache : " + self.nom_tache_luigi + ' en ' + str(duree)
        self.kernel.log_trace (createur, etape,  message_trace)
        
        # on marque la fin
        # dans le cas de recuperation du travail des taches required
        # on doit jouer sur les differents self.input qui ouvre les fichiers trvud
        
        return message
    
            

    
    def get_travail (self,) :
        self.arg_travail_data = json.loads (self.arg_travail)
        
        try :
            a = self.dico_evenements
        except :
            pathDicoEvenements = self.arg_travail_data ['pathDico_evenements']
            self.dico_evenements = Parametres (pathDicoEvenements, [])
        try :
            a = self.dico_systeme
        except:
            pathDico_systeme = self.arg_travail_data ['pathDico_systeme']
            self.dico_systeme = Parametres (pathDico_systeme, [])
            
            # on recupere le kernel
            self.arg_kernel_data = self.dico_systeme ['elasticsearch']
            self.kernel = Kernel (self.arg_kernel_data)
            
                   
        
        return
    
    def run_tache (self,) :
        return
    
        
    

    
    def get_execution(self,) :
        self.appels = {'appel' : None, 'type_repetition' : None}
        auteur = 'Generic'
        etape = "pas de garantie de fonctionnement"
        message = "la tache n'a pas de fonction get_execution  ????"
        self.kernel.log_warning (auteur, etape,  message)         
        
    def requires(self):
                 
        # initialisation
        self.get_travail ()
        self.get_execution()
                
        appel = self.appels ['appel']
        type_repetition = self.appels ['type_repetition']
        
        if appel is None :
            self.nombre_appels = 0
            return []
        
           
        
        if type_repetition == "date_evenement" :
            
            liste_bloc_date = self.get_liste_dates ()
                       
            
            liste_requires = []
            
            arg_travail_local = copy.deepcopy (self.arg_travail_data)
            self.liste_requires = []
            for date_debut, date_fin in liste_bloc_date :
                arg_travail_local ['variable_min'] = date_debut
                arg_travail_local ['variable_max'] = date_fin
                arg_travail1 = json.dumps (arg_travail_local)
                travail = appel (arg_travail = arg_travail1, )
                
                liste_requires.append (travail)
                
                continue
            self.nombre_appels = len(liste_requires)
            return liste_requires 
        
        if type_repetition == "ID" :
                        
            liste_blocs_ID = self.get_liste_blocs_ID ()
            arg_travail_local = copy.deepcopy (self.arg_travail_data)
            
            liste_requires = []
            
            for ID_reference_min, ID_reference_max in liste_blocs_ID  :
                
                arg_travail_local ['ID_min'] = ID_reference_min
                arg_travail_local ['ID_max'] = ID_reference_max
                
                arg_travail1 = json.dumps (arg_travail_local)
                travail = appel (arg_travail = arg_travail1, )
                
                liste_requires.append (travail)
                
                continue
                
            self.nombre_appels = len(liste_requires)
            return liste_requires
                  
        raise ValueError
        
        
    
    
    def get_liste_blocs_ID (self,) :
        
        path_liste_ID = self.arg_travail_data['pathListe_ID']
        
        f = open (path_liste_ID, 'r')
        liste = f.read ()
        f.close()
        liste = json.loads(liste)
        taille_liste_ID = len(liste)
        
        nombre_bloc_ID = self.dico_systeme ['calcul']['nombre_bloc_ID']
        taille_bloc_ID = int(taille_liste_ID/nombre_bloc_ID)
        
        resultat = []
        debut = 0
        fin = taille_bloc_ID
        while (True) :
            if fin >= taille_liste_ID - 1 :
                fin = taille_liste_ID - 1
                resultat.append ([liste [debut], liste[fin]])
                break
            resultat.append ([liste [debut], liste[fin]])
            debut = fin + 1
            fin = fin + taille_bloc_ID 
            continue
        
        return resultat
    
    def timestamp (self, date) :
        d = datetime.strptime(date, self.format_date_standart)
        return datetime.timestamp(d)
        
        
    
    def get_liste_dates (self,) :
        date_debut = self.arg_travail_data ['variable_min']
        date_fin = self.arg_travail_data ['variable_max']
        self.format_date_standart = self.dico_systeme ['calcul']['format_date_standard']
        
        date_debut_timestamp = self.timestamp (date_debut)
        date_fin_timestamp = self.timestamp (date_fin)
        
        nombre_bloc_date = self.dico_systeme ['calcul']['nombre_bloc_date']
        
        timedelta = (date_fin_timestamp - date_debut_timestamp) / nombre_bloc_date
        
        resultat = []
        time_debut = date_debut_timestamp
        time_fin = date_debut_timestamp + timedelta
        
        while (True) :
            if time_fin >= date_fin_timestamp :
                d1  = str(datetime.fromtimestamp(time_debut) )
                d2 =   str(datetime.fromtimestamp(time_fin) )
                resultat.append ([d1, d2])
                break
            d1  = str(datetime.fromtimestamp(time_debut) )
            d2 =   str(datetime.fromtimestamp(time_fin) )
            resultat.append ([d1, d2])
            
            time_debut = time_fin
            time_fin = time_fin + timedelta
            continue
        return resultat               
            



    
    

        
       
    
    
                
