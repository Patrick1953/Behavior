# coding: utf-8
import  os, sys, json, luigi, time, copy, random
from datetime import datetime

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


#from Alimentation_ID_bloc import Alimentation_ID_bloc
from Alimentation_date_bloc import Alimentation_date_bloc


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)

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
        etape = self.arg_travail_data ['nom_environnement']
        message_trace = "depart de la tache : " + self.nom_tache_luigi 
        self.kernel.log_trace (createur, etape,  message_trace)
                
        # on execute la tache
        t = time.time()
        try :
            self.get_travail ()
            message = self.run_tache()
        except Exception as e:
            createur = self.arg_kernel_data ['createur']
            etape = self.arg_travail_data ['nom_environnement']
            message = "erreur de la tache : " + self.nom_tache_luigi + ' du type '+ str(e.args)
            self.kernel.log_error (createur, etape,  message)
            
        duree = time.time() - t
        # on trace la fin avec la duree pour future optimisation
        createur = self.arg_kernel_data ['createur']
        etape = self.arg_travail_data ['nom_environnement']
        message_trace = "fin de la tache : " + self.nom_tache_luigi + ' en ' + str(duree)
        self.kernel.log_trace (createur, etape,  message_trace)
        
        
        
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
        
        resultat = self.arg_travail_data ['liste_blocs_ID']
        self.arg_travail_data ['isVariable'] = True
        self.arg_travail_data ['variable_sort'] = None
        self.arg_travail_data ['isID'] = True
        self.arg_travail_data ['ID_sort'] = None
        return resultat
    
    
        
        
    
    def get_liste_dates (self,) :
        
        self.arg_travail_data ['isVariable'] = True
        self.arg_travail_data ['variable_sort'] = None
        self.arg_travail_data ['isID'] = True
        self.arg_travail_data ['ID_sort'] = None
        
        A = Alimentation_date_bloc( self.arg_travail_data )
        return A.get_liste_date_bloc ()
    
    def lire_luigi_file_random(self, fin) :
        
        pourcentage_echantillon = self.dico_systeme ['calcul'] ['pourcentage_echantillon']
        if pourcentage_echantillon == 100 :
            return self.lire_luigi_file (fin)
        
        dico = {}
        for ligne_json in fin:
            x = random.uniform (0., 100.)
            if  x < pourcentage_echantillon :
                dico_ligne = json.loads (ligne_json)
                dico.update(dico_ligne)
            
            continue

        return dico
        
    
    def lire_luigi_file (self, fin) :
        
        dico = {}
        for ligne_json in fin:
            dico_ligne = json.loads (ligne_json)
            dico.update(dico_ligne)
        
        return dico
    
    def ecrire_luigi_file (self, fout, dico) :
        
        for cle, valeur in dico.items() :
            ligne_dico = {cle : valeur}
            ligne = json.dumps (ligne_dico)
            fout.write (ligne + os.linesep)
            continue
        return
    
        
                
                          
                          
                        
                          
                
class Generic (luigi.Task):
    
    
        
    def run (self,) :
        """
        run generique
         - pour les traces et gesion des erreurs
         - appel run_tache fournit par  la classe dependante
        """
        # on trace 
        createur = self.arg_kernel_data ['createur']
        etape = self.arg_travail_data ['nom_environnement']
        message_trace = "depart de la tache : " + self.nom_tache_luigi 
        self.kernel.log_trace (createur, etape,  message_trace)
                
        # on execute la tache
        t = time.time()
        try :
            self.get_travail ()
            message = self.run_tache()
        except Exception as e:
            createur = self.arg_kernel_data ['createur']
            etape = self.arg_travail_data ['nom_environnement']
            message = "erreur de la tache : " + self.nom_tache_luigi + ' du type '+ str(e.args)
            self.kernel.log_error (createur, etape,  message)
            
        duree = time.time() - t
        # on trace la fin avec la duree pour future optimisation
        createur = self.arg_kernel_data ['createur']
        etape = self.arg_travail_data ['nom_environnement']
        message_trace = "fin de la tache : " + self.nom_tache_luigi + ' en ' + str(duree)
        self.kernel.log_trace (createur, etape,  message_trace)
        
        
        
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
        
        self.arg_travail_data ['isVariable'] = True
        self.arg_travail_data ['variable_sort'] = None
        self.arg_travail_data ['isID'] = True
        self.arg_travail_data ['ID_sort'] = None
        
        resultat = self.arg_travail_data ['liste_blocs_ID']
        return resultat
    
    
        
        
    
    def get_liste_dates (self,) :
        
        self.arg_travail_data ['isVariable'] = True
        self.arg_travail_data ['variable_sort'] = None
        self.arg_travail_data ['isID'] = True
        self.arg_travail_data ['ID_sort'] = None
        
        A = Alimentation_date_bloc( self.arg_travail_data )
        return A.get_liste_date_bloc ()
    
    def lire_luigi_file_random(self, fin) :
        
        pourcentage_echantillon = self.dico_systeme ['calcul'] ['pourcentage_echantillon']
        if pourcentage_echantillon == 100 :
            return self.lire_luigi_file (fin)
        
        dico = {}
        for ligne_json in fin:
            x = random.uniform (0., 100.)
            if  x < pourcentage_echantillon :
                dico_ligne = json.loads (ligne_json)
                dico.update(dico_ligne)
            
            continue

        return dico
    
    def lire_luigi_file (self, fin) :
        
        dico = {}
        for ligne_json in fin:
            dico_ligne = json.loads (ligne_json)
            dico.update(dico_ligne)
        
        return dico
    
    def ecrire_luigi_file (self, fout, dico) :
        
        for cle, valeur in dico.items() :
            ligne_dico = {cle : valeur}
            ligne = json.dumps (ligne_dico)
            fout.write (ligne + os.linesep)
            continue
        return              
            



    
    

        
       
    
    
                
