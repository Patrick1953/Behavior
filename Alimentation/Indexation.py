# coding: utf-8
# coding: utf-8
from copy import deepcopy
import json, sys
from datetime import datetime



from pprint import PrettyPrinter 
def PP (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

path = "../outils"
if path not in sys.path :
    sys.path.append (path)
    
from Kernel_BE import Kernel
from Parametres import Parametres
from myFloat import myFloat
from myDate import myDate
from myString import myString
from Dico_ajout import Dico_ajout


class Indexation_evenements () :
    """
    # par exemple pour
    dico_evenements_data = {  'ID' : 0,
                             'date_evenement' : 1,
                             'prix_panier' : 2,
                             'nomenclature_1' : 3,
                             'nomenclature_2' : 4,
                             'nomenclature_3' : 5,
                             'nomenclature_4' : 6,
                             'description' : 7,
                             'prix' : 8,
                         }

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
                  pathDico_evenements,
                  pathDico_systeme,
                  isTrace = False,
                  
                  ) :
        
        
        self.isTrace = isTrace
        ## on load le dico qui contiend la structure des données evenements ########
        
        self.pathDico_evenements = pathDico_evenements
        self.dico_alimentation  = Parametres (self.pathDico_evenements, listeData = ['alimentation',
                                                              'execution'])
        
        self.ID_reference_depart, self.ID_reference_fin = self.dico_alimentation ["taille_globale"]
        self.index_bulk = self.dico_alimentation ['index_data']
        self.nombre_erreur_max = self.dico_alimentation ['nombre_erreur_max']
        
        self.parametres_lecture  = Parametres (self.pathDico_evenements, listeData = ['alimentation',
                                                               'parametres_lecture',
                                                              ])
        self.sep = self.parametres_lecture ['sep']
        self.pathFile = self.parametres_lecture ['pathFile']
        
        
        
        self.pathDico_systeme =  pathDico_systeme
        self.dico_systeme = Parametres (self.pathDico_systeme, listeData = [])
        
        self.arg_kernel = self.dico_systeme ['elasticsearch']
        self.ID_reference_base = self.arg_kernel ['ID_reference_base']
        self.kernel = Kernel (self.arg_kernel)
        self.kernel.initRead ( self.pathFile )
        
        
        self.dico_evenements = Parametres (self.pathDico_evenements, listeData = [])
        
        
        #self.pas = self.dico_evenements ['pas']
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
            
        

        self.F = myFloat (pathDico_systeme)
        self.S = myString (pathDico_systeme)
        self.D = myDate (pathDico_systeme)
        
        self.date_min = self.D.convert_date ('9999-04-11 00:53:44', '%Y-%m-%d %H:%M:%S')
        self.date_max = self.D.convert_date ('1800-04-11 00:53:44', '%Y-%m-%d %H:%M:%S')
    
    
            
        
    def memorisation_date_min_max(self, date) :
        if date < self.date_min :
            self.date_min = date
            
        if date > self.date_max :
            self.date_max = date
        return
            
        
        
        
        
            
        
    
    def convertir (self, val, nom ) :
        if nom == 'ID' :
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
        
        typeVal = self.type_zone [nom]
        formatEntree = self.format_zone [nom]
        
        if typeVal == "date" :
            return self.D.test_date (val, formatEntree )
        if typeVal == "numeric" :
            return self.F.test_float (val, formatEntree )
        if typeVal == "string" :
            return self.S.test_string (val, formatEntree )
        raise ValueError
        
            
        return valeur        
        
               

    def _indexation (self,) :
        
        
        
        
        ID_reference_base = self.ID_reference_base
        taille = len (self.ID_reference_base)
        ID_reference = self.ID_reference_fin
        kernel = self.kernel
        position = self.position
        liste_nom_zone = self.liste_nom_zone
        
        
        isFirst = True
        nombre_variable = 0
        nombre_ligne = 0
        self.nombre_erreur = 0
        
        
        
        for liste in kernel.readIterator (sep = self.sep) :
            
            
            if len(liste) == 0 :
                #print ('nombre_ligne =', nombre_ligne)
                #print ('nombre de variable =', nombre_variable)
                #print ()
                break
            
            
            
            # extraction des données de la ligne dans le dico data
            data = {}
            for nom in liste_nom_zone :
                rang = position [nom]
                valeur = liste [rang]
                if not self.test_val (valeur, nom) :
                    self.nombre_erreur += 1 
                    continue
                data [nom] = self.convertir(valeur, nom)
                continue
                
            
            if self.nombre_erreur > self.nombre_erreur_max :
                break
                
            
                
            if len(data) != len(liste_nom_zone) :
                continue # on abandonne la ligne
                
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
                       }
            
            
                
            nombre_ligne += 1
            
            # pour chaque valeur autre que ID et date_evenement envoie de la valeur et de son nom
            for nom in liste_nom_zone :
                
                dico_out = deepcopy (dico_out_initiale)
                if nom == "ID" or nom == "date_evenement" or nom == "ID_reference":
                    continue
                
                dico_out ["nom_variable"] = nom
                dico_out ["valeur"] = data [nom]
                nombre_variable += 1
                               
                yield dico_out
                    
            
            
        
        # on met à jour dico_evenements ('alimentation.execution')
        
        
        dico_ajout = self.dico_alimentation  ['dico_ajout']
        
            
        if len(dico_ajout) == 0 :
            numero = 0
        else:
            liste_ajout = [nom_ajout for nom_ajout in dico_ajout.keys()]
            liste_ajout.sort()
            dernier_ajout = liste_ajout [len(liste_ajout) - 1]
            
            _ , numero = dernier_ajout.split ('_')
            numero = int(numero) + 1
            
                   
        numero_string = ("0000000000000000000"+str(numero) ) [-10:] 
        name_ajout = "ajout_" + numero_string
        
        nombre_debut = self.ID_reference_fin
        nombre_fin = self.ID_reference_fin + nombre_ligne
        new_ajout = {}
        new_ajout ['numero_ligne_debut'] = nombre_debut
        new_ajout ['numero_ligne_fin'] = nombre_fin
        new_ajout ['date_execution'] = str(datetime.now())
        new_ajout ['date_min'] = self.date_min 
        new_ajout ['date_max'] = self.date_max
        new_ajout ['nombre_ligne'] = nombre_ligne
        new_ajout ['nombre_erreur'] = self.nombre_erreur
        
        dico_ajout [name_ajout] = new_ajout
        
        self.ID_reference_fin += nombre_ligne
        taille_globale = [self.ID_reference_depart, self.ID_reference_fin]
        
        # on relit et on sauve rapidement pour eviter au max les conflits avec
        
        self.dico_alimentation = Parametres (self.pathDico_evenements, listeData = ['alimentation', 'execution' ])
        self.dico_alimentation ['dico_ajout']  = dico_ajout
        self.dico_alimentation ["taille_globale"] = taille_globale 
        #PP (self.dico_alimentation )
        self.dico_alimentation.save()
               
        return
        
    
        
    
    def indexation (self, isPurge_existing_index = False,) :
        
        
        
        self.kernel.bulk (self._indexation (),
                         self.index_bulk,
                         isPurge_existing_index = isPurge_existing_index,)
        
        return
    
    
def Indexation (pathDico_evenements = "../data/dico_evenements_2.txt",
                pathDico_systeme = "../data/dico_systeme_2.txt",
                isPurge_existing_index = False,
                isTrace = False,
                
                ) :

    Ecrivain = Indexation_evenements (  pathDico_evenements,
                                        pathDico_systeme,
                                       isTrace = isTrace)
    
   
    


    Ecrivain.indexation (isPurge_existing_index = isPurge_existing_index,)
    return
                

            
        
    
