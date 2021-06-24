# coding: utf-8
import os, sys, json
from datetime import datetime

path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
from PARAMETRAGES_2_2 import Get_new_dico_evenements, Update_create__environnement

path = "../Calcul"
if path not in sys.path :
    sys.path.append (path)
from Calcul_quantile import Description_travail_quantile
from Calcul_date import Calcul_date


class Interface_parametres_engine () :
    
    def __init__ (self,) :
        
        
        self.path = '../data/'
        
        self.Description_travail_quantile = Description_travail_quantile()
        self.Description_travail_date = Calcul_date ()
        
        self.dico_type_to_travail = {
            
                                            'string' : 'analyse_mot',
                                            'numeric' : 'quantile',
                                            'date' : 'date',

                                        }
        
        
       
        
        
    def call_liste_environnements (self,) :
        
        l = os.listdir(self.path)
        
        resultat = []
        for i in l:
            if os.path.isdir(self.path + i):
                if i [:1] =='#' :
                    nom_environnement = i
                    resultat.append (nom_environnement)
        
        return resultat
    
    
        
        
    
    def call_dico_evenements (self, nom_environnement) :
        
        vrai_nom = nom_environnement       
        path_dico_environnement = self.path + vrai_nom + '/parametres/dico_evenements_2.json'
        
        arg_entree_sortie_lock = {} 
        arg_entree_sortie_lock['pathFile'] = path_dico_environnement
        Entree_sortie_evenements = Entree_sortie_lock (arg_entree_sortie_lock)
        dico_evenements = Entree_sortie_evenements.lire_with_lock()
        Entree_sortie_evenements.unlock_lire()
        
        return dico_evenements
      
    
    def send_dico_evenements (self,nom_environnement, dico_evenements) :
            
        vrai_nom = nom_environnement       
        path_dico_environnement = self.path + vrai_nom + '/parametres/dico_evenements_2.json'
        
        arg_entree_sortie_lock = {} 
        arg_entree_sortie_lock['pathFile'] = path_dico_environnement
        Entree_sortie_evenements = Entree_sortie_lock (arg_entree_sortie_lock)
        
        Entree_sortie_evenements.acquire()
        Entree_sortie_evenements.ecrire_with_unlock (dico_evenements)
        return
    
    
            
    def type_to_travail (self, data_type ) :
        return self.dico_type_to_travail [data_type]
    
    
    
    
    def get_dico_new (self,) :
        
        dico = {

            # decrit les executions par type de pas

                'pas' : {},


                'type': {'ID': {'format': 'standard','type': 'string'},
                          'date_evenement': {'format': None, 'type': 'date'},
                          },

                'position': {'ID': None,
                          'date_evenement': None,
                          },

                'creation_dictionnaire' : {'ID' : {'travail' : None,
                                                  'parametres' : []},
                                            'date_evenement' : {'travail' : 'date',
                                                                'parametres' : []},



                                           },


                                      
                }
        
        return dico
    
    def update_create__environnement (self,nom_environnement) :
        return Update_create__environnement (nom_environnement)
            

        
    
    
    
    
    
class  Interface_parametres ( Interface_parametres_engine ) :
    
    def __init__ (self,) :
        
        self.pathFile_local = './created.json'
               
        self.action_choix = {' New_one' : self.get_dico_new,
                                                        
                            }
        liste_choix = [choix for choix in self.action_choix.keys()]
        self.liste_choix = []
        self.liste_choix.extend (liste_choix)
        
        self.filtre = ['pas', 'type', 'position', 'creation_dictionnaire']
        self.dico_saisie = {}
        
        
        
        
        
        
        super ().__init__ ()
        
        
       
    def get_dico_local (self,) :
        
        if os.path.exists(self.pathFile_local) :
            
            with open (self.pathFile_local, 'r') as f :
                data = f.read ()
            dico = json.loads (data)
            return dico
        return self.get_dico_new ()
    
    def save_dico_local (self,dico):
        
        data = json.dumps (dico)
        with open (self.pathFile_local, 'w') as f :
                data = f.write (data)
        return
        
        
    
    def get_existing_dico (self, nom_environnement) :
        return self.call_dico_evenements (nom_environnement)
    
    def nettoyage_dico (self, dico) :
        
        liste_cle = [cle for cle in dico.keys()]
        
        for cle in liste_cle :
            if not cle in self.filtre :
                del dico [cle]
        
        return dico
    
    def get_dico_evenements (self, nom_environnement ) :
        
        
        
        if nom_environnement in self.action_choix :
            dico = self.action_choix [nom_environnement] ()
            dico = self.nettoyage_dico (dico)
            self.save_dico_local (dico)
            return dico
        else:
            dico = self.get_existing_dico (nom_environnement)
            dico = self.nettoyage_dico (dico)
            self.save_dico_local (dico)
            return dico

    
    def get_liste_environnements (self,) :
        
        liste = self.call_liste_environnements ()
        liste.extend (self.liste_choix)
        liste.sort()
               
        return liste
    
    def put_dico_evenements (self,nom_environnement, dico_evenements) :
        
        old_dico_evenements = self.call_dico_evenements ( nom_environnement)
        
        for nom in self.filtre :
            old_dico_evenements [nom] =  dico_evenements [nom]
            
        self.send_dico_evenements (nom_environnement, old_dico_evenements)
        
        return
    
    
    
        
        
        
    
    def is_good_date (self, format_string) :
          
        date_now = datetime.now()
        date_time_str = 'erreur de lecture du format'
        date_str =  'erreur de passage en format standard'
              
        try:
            date_time_str = date_now.strftime(format_string)
            date = datetime.strptime(date_time_str, format_string)
            date_str = date.strftime(format_string)
        except:
            return False
        if date_time_str != date_str :
            return False
        return True
    
    def get_liste_travail (self, type_travail) :
                     
        liste = ['']
        if type_travail == 'quantile' :
            liste1 = self.Description_travail_quantile.get_liste_travail_quantile ()
        if type_travail == 'date' :
            liste1 = self.Description_travail_date.get_liste_travail_date ()
        if type_travail == 'pas' :
            liste1 = self.Description_travail_date.get_liste_travail_date ()
            try:
                liste1.remove ('ferie')
            except:
                pass
            liste1.append('trimester')
            
            
        liste.extend(liste1)
        return liste
    
    def save_dico_evenements (self, nom_environnement, dico_evenements ) :
        
        liste_nom_environnement_existant = self.call_liste_environnements ()
        
        if nom_environnement in liste_nom_environnement_existant :
            self.put_dico_evenements (nom_environnement, dico_evenements)
            return
        else:
            new_dico_evenements = self.update_create__environnement (nom_environnement)
            for nom in self.filtre :
                new_dico_evenements [nom] =  dico_evenements [nom]
            self.send_dico_evenements (nom_environnement, new_dico_evenements)
        
        return
            
            
 
    
        
        
        
        
