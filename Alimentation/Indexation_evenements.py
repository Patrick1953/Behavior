# coding: utf-8
### coding: utf-8
from copy import deepcopy
import json, sys
from datetime import datetime


path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
from Kernel_BE import Kernel
from Parametres import Parametres
from myFloat import myFloat
from myDate import myDate
from myString import myString
from Dico_ajout import Dico_ajout


class Indexation_evenements () :
    """
    # en entree des dico en format Python 
    # par exemple pour
    arg :
    dico_evenements 
    dico_systeme
    
    iterateur (permet d iterer sur chaque ligne d'entree)
    
    
    
    format bulk dans ES :
    
    dico_out_data = {
                    "ID" : ID,
                    "date_evenement" : date_evenement,
                    "ID_reference" : ID_reference,
                    "nom_variable" : nom_variable,
                    "valeur" : valeur,
                    }
    pour chaque zone mise en base 
    """
    def __init__ (self,
                  arg,
                  iterateur,
                  
                  ) :
            
        self.nom_tache_alimentation = arg ['nom_tache_alimentation'] # pour parallelisation
        
        self.dico_alimentation  = Parametres (arg['dico_evenements'], listeData = ['alimentation',
                                                              'execution'])
        
        self.ID_reference_depart, self.ID_reference_fin = self.dico_alimentation ["taille_globale"]
        self.index_bulk = self.dico_alimentation ['index_data']
        self.nombre_erreur_max = self.dico_alimentation ['nombre_erreur_max']
        self.isPurge_existing_index = arg ['isPurge_existing_index']
           
        
        self.dico_systeme = Parametres (arg ['dico_systeme'], listeData = [])
        
        self.arg_kernel = self.dico_systeme ['elasticsearch']
        self.ID_reference_base = self.arg_kernel ['ID_reference_base']
        self.kernel = Kernel (self.arg_kernel)
              
        self.iterateur = iterateur
        
        
        self.dico_evenements = Parametres (arg ['dico_evenements'], listeData = [])
        self.position = self.dico_evenements ['position']
        self.type  = self.dico_evenements ['type']
        
        
        
        
              
        self.liste_nom_zone = [nom_zone for nom_zone in self.type.keys()]
               
        # on prepare le test sur le format et le type
        self.format_zone = {}
        self.type_zone = {}
        for nom in self.liste_nom_zone :
            dico_type_zone = self.type [nom]
            type_zone = dico_type_zone  ['type']
            format_zone = dico_type_zone  ['format']
            self.format_zone [nom] = format_zone
            self.type_zone [nom] = type_zone
            continue
            
        
        
        self.F = myFloat (self.dico_systeme)
        self.S = myString (self.dico_systeme)
        self.D = myDate (self.dico_systeme)
        
        self.date_min = self.D.convert_date ('9999-04-11 00:53:44', '%Y-%m-%d %H:%M:%S')
        self.date_max = self.D.convert_date ('1800-04-11 00:53:44', '%Y-%m-%d %H:%M:%S')
        
        nom_file_erreur = '_'.join(['error', self.nom_tache_alimentation,]) +'.txt'
        pathFile_erreur = '../data/alimentation_evenements/' + nom_file_erreur
        self.f_erreur = open (pathFile_erreur, 'w')
    
    
            
        
    def memorisation_date_min_max(self, date) :
        if date < self.date_min :
            self.date_min = date
            
        if date > self.date_max :
            self.date_max = date
        return
            
        
        
        
        
            
        
    
    def convertir (self, val, nom ) :
        if nom == 'ID' :
            return val
        if val == '' :
            return val
        typeVal = self.type_zone [nom]
        formatEntree = self.format_zone [nom]
        if typeVal == "date" :
            return self.D.convert_date (val, formatEntree )
        if typeVal == "numeric" :
            return self.F.convert_float (val, formatEntree )
        if typeVal == "string" :
            return self.S.convert_string (val, formatEntree )
        raise ValueError
    
    def test_val (self, val, nom ) :
        if nom == 'ID' :
            return True
        if val == '' :
            return True
        typeVal = self.type_zone [nom]
        formatEntree = self.format_zone [nom]
        
        if typeVal == "date" :
            return self.D.test_date (val, formatEntree )
        if typeVal == "numeric" :
            return self.F.test_float (val, formatEntree )
        if typeVal == "string" :
            return self.S.test_string (val, formatEntree )
        raise ValueError
        
    
    def ecrire_dico_erreur (self, dico) :
        data_json = json.dumps(dico)
        self.f_erreur.write (data_json + '\n')
        return
    
    def remise_a_zero (self,) :
        # on detruire ID_reference > ID_reference_min et ID_alimentation == self.
        #self.kernel.delete (index, ID_reference_min, ID_alimentation)
        self.isError = True
        return
                 

    def _indexation (self,) :
               
        ID_reference_base = self.ID_reference_base
        taille = len (self.ID_reference_base)
        ID_reference = self.ID_reference_fin
        iterateur = self.iterateur
        position = self.position
        liste_nom_zone = self.liste_nom_zone
        
        
        isFirst = True
        nombre_variable = 0
        nombre_ligne = 0
        self.nombre_erreur = 0
        self.isError = False
    
        for liste in iterateur () :
            
            
            if len(liste) == 0 :
                break
            
            
            
            # extraction des données de la ligne dans le dico data
            data = {}
            isErreur = False
            for nom in liste_nom_zone :
                rang = position [nom]
                valeur = liste [rang]
                if not self.test_val (valeur, nom) :
                    self.nombre_erreur += 1
                    isErreur = True
                    continue
                data [nom] = self.convertir(valeur, nom)
                continue
                
            if len(data) != len(liste_nom_zone) :
                self.nombre_erreur += 1
                isErreur = True
                continue # on abandonne la ligne
                
            if isErreur :
                self.ecrire_dico_erreur (data)
            
            if self.nombre_erreur > self.nombre_erreur_max :
                self.remise_a_zero ()
                break
                
            
                
            
                
            # incrementation par evenements           
            ID_reference += 1 
            ID_reference_string = str(ID_reference)
            ID_reference_courant  = (ID_reference_base + ID_reference_string) [-taille:]
                       
            
            # pour cet evenement calcul de l'entete #######################
            ID = data ["ID"]
            date = data ["date_evenement"]
            self.memorisation_date_min_max(date)
            dico_out_initiale = {"ID_reference" : ID_reference_courant,
                                 "ID" : ID,
                                 "date_evenement" : date,
                                 #'nom_tache_alimentation' : self.nom_tache_alimentation, #permet parallelisation et restauration
                                 # avec remise à zero de l'index
                       }
            
            
                
            nombre_ligne += 1
            isDebut_ligne = True
            # pour chaque valeur autre que ID et date_evenement envoie de la valeur et de son nom
            for nom in liste_nom_zone :
                dico_out = deepcopy (dico_out_initiale)
                if nom == "ID" or nom == "date_evenement":
                    continue
                
                
                dico_out ["nom_variable"] = nom
                dico_out ["valeur"] = data [nom]
                #dico_out ['isDebut_ligne'] = isDebut_ligne  # permet de reconstruire la ligne
                
                isDebut_ligne = False
                nombre_variable += 1
                                               
                yield dico_out
                    
            
        self.f_erreur.close()
        
        arg = {}
        arg ['etat'] = 'OK'
        if self.isError :
            arg ['etat'] = 'KO'
        
        arg ['nom_tache_alimentation'] = self.nom_tache_alimentation
        arg ['nombre_ligne'] = nombre_ligne
        arg ['date_min'] = self.date_min
        arg ['date_max'] = self.date_max
        arg ['nombre_erreur'] = self.nombre_erreur
        arg ['isPurge_existing_index'] = self.isPurge_existing_index
        
        self.arg_resultat = arg # resultat de l'indexation (bulk)
        
        return
            
    
    def indexation (self,) :
        
        """
        pour parallisation (future)
        reconstruire chaque ligne ou recevoir cette ligne par yield
        construire un fichier avec ligne == [enreg0, enreg1,....]
        
        une tache appellante qui pour chaque ligne calcule ID_reference et bulk dans l'ordre
        (cette tache reste un point de blocage... a voir)
        à la fin renvoie le resultat consolidé
        
        
        on gagne sur les verification et les changement de format
        en cas d'erreur abandon de l'ensemble de l alimentation 
               
        """
        
        
        
        self.kernel.bulk (self._indexation (),
                         self.index_bulk,
                         isPurge_existing_index = self.isPurge_existing_index,)
        
        return self.arg_resultat
    
    
    
    

    

            
    
