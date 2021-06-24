# coding: utf-8
import os, shutil, sys

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Gestion_commandes import Gestion_commandes, Gestion_reponses, Gestion_erreurs
from Entree_sortie_lock import Entree_sortie_lock

class Gestion_etat_systeme (Entree_sortie_lock) :    
    
    def __init__ (self,) :
        
        pathFile = '../data/general/parametres/echanges/etat_systeme.json'
        arg = {}
        arg ['pathFile'] = pathFile
        super().__init__ (arg)
        
    def get_values (self,) :
        
        dico = self.lire_with_lock ()
        if dico == {} :
            self.dico_workers = {}
            self.dico_taches = {}
            self.dico_demandes = {}
            return
            
        self.dico_workers = dico ['workers']
        self.dico_taches = dico ['taches']
        self.dico_demandes = dico ['demandes']
        
        return
    
    def set_values (self,) :
        dico = {}
        dico ['workers'] = self.dico_workers
        dico ['taches'] = self.dico_taches
        dico ['demandes'] = self.dico_demandes
        
        self.ecrire_with_unlock (dico)
        return



        
class Gestion_etat (Gestion_etat_systeme) :
    
    """
    etat_systeme : dico {dico_workers,
                         dico_taches ,
                         dico_demandes,
                        }
    
     dico_workers : {'nom_worker' : (numero_tache | None}
     dico_taches : {'numero_tache' : {nom_worker, cle_demande}
                              
                           
     dico_demandes { cle_demande :    { 
                                         liste_running : [numero_tache, ]
                                         'message_tache' : {nom_appel: nom,  arg : dico,},
                                        
                                        },
    
    """
    
    
    def __init__ (self,) :
        
        super ().__init__ ()
        
        
        
        
    
        
    
    def create_numero_tache () :
        
        liste_numero = [int(numero) for numero in self.dico_taches.keys()]
        maximum = max(liste_numero)
        return str(maximum+1)
    
           
    def create_tache (self, cle_demande, nom_worker  ) :
               
        numero_tache = self.create_numero_tache ()       
                
        self.dico_taches [numero_tache] = {
                                           'cle_demande' : cle_demande,
                                           'worker' : nom_worker
                                          }
        
        self.dico_worker [nom_worker] = numero_tache
                       
        return
                                                 
                                                 
                                                 
                                                 
class  Gestion_receveur (Gestion_etat)  :
    
    def __init__(self,) :
        
        super ().__init__ ()
        
        self.Gestion_reponses_erreur = Gestion_reponses_erreur ()
        
    # on recoit le nom worker la tache s'execute
    def tache_running (self, message) :
        
        self.get_values()
        
        cle_demande = message ['cle_demande']      
        nom_worker = message ['nom_worker']
        self.create_tache (cle_demande, nom_worker)
        
        self.set_values ()
        
        return
    
    def tache_OK (self, message) :
        self.get_values()
        
        cle_demande = message ['cle_demande']
        demande = self.dico_demandes [cle_demande]
        
        demande ['nombre_repetition'] -= 1
        nombre_repetition = demande ['nombre_repetition']
        if nombre_repetition <= 0 :
            # demande fini
            del self.dico_demandes [cle_demande]
        
        self.tache_fini (message)
        
        self.set_values ()
        
        return
    
            
            
    def tache_fini (self, message, ):
        
        # tache fini 
        nom_worker = message ['nom_worker']
        numero_tache = self.dico_workers [nom_worker]
        del self.dico_taches [numero_tache]
        
        # worker disponible
        self.dico_workers [nom_worker] = None
        
        return
    
    def tache_KO (self, message) :
        self.get_values()
        
        cle_demande = message ['cle_demande']
        demande = self.dico_demandes [cle_demande]
        
        demande ['nombre_erreur'] -= 1
        nombre_erreur = demande ['nombre_erreur']
        if nombre_erreur <= 0 :
            # demande en erreur => on le signale au lanceur (non synchrone)
            self.Gestion_reponses_erreur.put_message(self.dico_demandes [cle_demande])
            
        
        self.tache_fini (message)
        
        demande ['nombre_repetition'] -= 1
        nombre_repetition = demande ['nombre_repetition']
        if nombre_repetition <= 0 :
            # demande fini
            del self.dico_demandes [cle_demande]
        demande ['nombre_repetition'] -= 1
        nombre_repetition = demande ['nombre_repetition']
        if nombre_repetition <= 0 :
            # demande fini
            del self.dico_demandes [cle_demande]
        self.set_values ()
        return
    

    
class Lanceur (Gestion_etat_systeme) :
    
    '''
    commande : dico
    
    {
    'nombre_repetition'
    'nombre_erreur'
    
    'nom_appel'
    'arg'
       
    }
    
    '''
    
    def __init__ (self, ) :
        
        super().__init__ (self,)
        
        self.Gestion_commandes = Gestion_commandes ()
        
        self.tache_possible  ['Alimentation', 'Apprentissage', 'Execution']
        
        self.directory_reserve = ['general', 'alimentation_evenements',
                                 'data_sortie', 'parametrages']
        
    def get_date_min_max_possible (self,commande) :
        
        arg = commande ['arg']
        nom_evenements = arg ['nom_evenements']
        pathFile = '../data/' + nom_evenements + '/parametres/dico_evenements_2.json'
        
        arg_lock = {'pathFile' : pathFile}
        Entree_sortie = Entree_sortie_lock (arg_lock)
        dico_evenements = Entree_sortie.lire_with_lock ()
        self.unlock_lire ()
        
        dico_ajout = dico_evenements ['alimentation'] ['execution'] ['dico_ajout']
        
        liste_date_max = []
        liste_date_min = []
        for dico in dico_ajout.values() :
            date_min = dico ['date_min']
            liste_date_min.append (date_min)
            date_max = dico ['date_max']
            liste_date_max.append (date_max)
            
        return min (liste_date_min), max(liste_date_max)
    
            
    
    def get_liste_environnement_possible (self,) :
        
        liste_directory = os.listdir ('../data/') 
        resultat = []
        for directory in os.listdir () :
            if directory in self.directory_reserve :
                continue
            test = directory.split ('%') [0]
            if test != directory :
                continue
            resultat.append (directory)
        return resultat
    
    
    def get_date_min_max_commande (self, commande) :
        
        arg = commande ['arg']
        date_min = arg ['date_min']
        date_max = arg ['date_max']
        
        return date_min, date_max
            
        
    def verif_commande (commande):
        
        try :
            
        
            # validation de l'existance du nom de la tache
            nom_appel = commande ['nom_appel']
            if not nom_appel in self.tache_possible :
                message = 'not existing task'
                return message
            
            # validation environnement
            arg = commande ['arg']
            nom_environnement = arg ['nom_environnement']
            liste_environnement_possible = self.get_liste_environnement_possible ()
            if not nom_environnement in liste_environnement_possible :
                message = 'not existing environment'
                return message
            
            # validation dates
            date_min_possible, date_max_possible = self.get_date_min_max_possible (nom_environnement)
            date_min, date_max = self.get_date_min_max_commande ()
            if date_min < date_min_possible or date_max >= date_max_possible :
                message = 'dates out of range'
                return message
            
        except:
            message = 'bad command format'
            return message
        return
    
    def init_commande (self, commande) :
        
        arg = commande ['arg']
        nom_environnement = arg ['nom_environnement']
        
        src = './data/' + nom_environnement
        dest = '%'.join [nom_environnement, nom_environnement]
        shutil.copytree(src, dest)
        arg ['nom_environnement'] = dest
        commande ['arg'] = arg
        
        return
    
        
    def lancement_commande (self, commande) :
        
        message = self.verif_commande (commande)
        if not message is None :
            return message
        
        
        self.init_commande (commande)
        cle_demande  = self.create_demande  (commande)
        commande ['cle_demande'] = cle_demande
        nombre_repetition = commande ['nombre_repetition']
        
        for i in range (0, nombre_repetition) :
            self.self.Gestion_commandes.put_message(commande)
            
        return
    
    def create_cle_demande (self, demande) :
               
        l = [demande ['nom_appel'],]
        valeur_variables = [str(valeur) for valeur in demande ['arg'].values()]
        l.extend (valeur_variables)
        l.sort()
        cle = ''.join(l)
                
        return cle
    
    def create_demande  (self, demande) :
        
        cle_demande = self.create_cle_demande ( demande)
        
        self.get_values ()
                
        self.self.dico_demandes [cle_demande] =  demande
        
        self.set_values ()
        
        return  cle_demande
    
                                                 
        
        
    
    
    

    
    
    
        
        
        
