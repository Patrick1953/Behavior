# coding: utf-8
import copy, json
from  datetime import datetime
import sys

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Parametres import Parametres
from Kernel_BE import Kernel

class Alimentation_bloc () :
    
    def __init__ (self, arg) :
        
        """ variable à l appel de search_par_bloc de Kernel donc dans arg
                                Search_par_bloc
                                 
                                 ID,                     # inused Mais compatibilite oblige
                                 ID_reference_min,
                                 ID_reference_max ,
                                 ID_reference_sort = 'asc',

                                 isID = True,
                                 ID_min = ID_min ,
                                 ID_max  = ID_max ,
                                 ID_sort  = 'asc',

                                 isVariable = False,
                                 nom_variableQuery = None,
                                 variable_min = "",
                                 variable_max = "",
                                 variable_sort = 'asc',

                                 size = pas ,
        """
        
        
        self.ID_reference_min = arg['ID_reference_min']
        self.ID_reference_max = arg['ID_reference_max']
        self.ID_reference_sort = arg ['ID_reference_sort']
        self.isReference = arg ['isReference']
        
        
        
        self.isID = arg['isID']
        self.ID_min = arg ['ID_min']
        self.ID_max  = arg ['ID_max']
        self.ID_sort  = arg ['ID_sort']
        
        self.isVariable =  arg ['isVariable']
        self.nom_variableQuery = arg ['nom_variableQuery']
        self.variable_min = arg ['variable_min']
        self.variable_max = arg ['variable_max']
        self.variable_sort = arg ['variable_sort']
        
        
        self.isTrace = arg ['isTrace']
        
        
        # on a besoin du format standart de ES
        self.dico_systeme = Parametres (arg ['pathDico_systeme'], [])
        
        #P (arg ['pathDico_systeme'])
        
        
        self.format_date_standard = self.dico_systeme ['calcul'] ['format_date_standard']
        self.taille_bloc = self.dico_systeme ['calcul']['taille_bloc']
        self.arg_kernel = self.dico_systeme ['elasticsearch']
        
               
        self.kernel = Kernel(self.arg_kernel)
        
        # variables dans dico_evenements
        dico_evenements = Parametres (arg ['pathDico_evenements'], [])
        
                
        self.index_data = dico_evenements ['alimentation'] ['execution'] ['index_data']
        position_variable = dico_evenements ["position"]
        self.nombre_variable_par_ligne = len(position_variable)
        
        # permet de minimise le travail de ES (encadredement) dans l acces par bloc
        #  et  on colle la fin de chaque bloc sur la fin d'une ligne
        self.size = (self.nombre_variable_par_ligne -2 ) * self.taille_bloc
        
        if self.isTrace :
            print ('#initialisation#')
            print ('self.isReference =', self.isReference )
            print ()
            print ('self.isVariable =', self.isVariable )
            print ('self.nom_variableQuery=', self.nom_variableQuery )
            print ('self.variable_min =', self.variable_min )
            print ('self.variable_max =', self.variable_max )
            print ('self.variable_sort =', self.variable_sort )
            print ()

            print ('self.isID =', self.isVariable )
            print ('self.ID_min=', self.ID_min )
            print ('self.ID_max =', self.ID_max )
            print ('self.ID_sort =', self.ID_sort )
            print ()
            print ()
        
        
        
        return
    
    def alimentation_bloc_date (self,) :
        """
         lit un bloc de variable 
         entre Date_min et Date max
         et
         entre IDmin IDmax
          => yield les variables
          
          
        ex :# min

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
                                 ID_reference_sort = None,
                                 isReference = False,

                                 isID = True,
                                 ID_min = ID_min,
                                 ID_max  = ID_max,
                                 ID_sort  = None,

                                 isVariable = True,
                                 nom_variableQuery = "date_evenement",
                                 variable_min = date_evenement_min,
                                 variable_max = date_evenement_max,
                                 variable_sort = 'asc',

                                 size = 100 ,
                                 
                                 )
        
        
        
        r = 
        self.isReference = False

        self.isVariable = True
        self.nom_variableQuery= date_evenements
        self.variable_min = 2021-02-01 00:00:00
        self.variable_max = 2021-02-20 00:00:00
        self.variable_sort = asc

        self.isID = True
        self.ID_min= couple_cadre_0
        self.ID_max = couple_cadre_1
        self.ID_sort = None
        """
    
        
        if self.isTrace :
            print ('#get_bloc_date#')
            print ('self.isReference =', self.isReference )
            print ()
            nombre_en_cours -= 1
            
            print ('self.isVariable =', self.isVariable )
            print ('self.nom_variableQuery=', self.nom_variableQuery )
            print ('self.variable_min =', self.variable_min )
            print ('self.variable_max =', self.variable_max )
            print ('self.variable_sort =', self.variable_sort )
            print ()

            print ('self.isID =', self.isID )
            print ('self.ID_min=', self.ID_min )
            print ('self.ID_max =', self.ID_max )
            print ('self.ID_sort =', self.ID_sort )
            print ()
            print ('size =', self.size)
        ID = "" # deprecated
        size = self.size
        date_evenement_min = self.variable_min
        debut_bloc = 0
        fin_bloc = 9999999999999
        taille_lu = 1  
        hits = []
        while (taille_lu > len(hits) ):
            
                                                
            taille_lu, hits = self.kernel.search_par_bloc (self.index_data,
                                                           ID, #deprecated
                                                           debut_bloc,
                                                           fin_bloc,
                                                           size = size,
                                                           isReference = self.isReference,
                                                           ID_reference_sort = self.ID_reference_sort,
                                                           
                                                           isID = self.isID,
                                                           ID_min = self.ID_min,
                                                           ID_max  = self.ID_max ,
                                                           ID_sort  = self.ID_sort,
                                                           
                                                           isVariable = self.isVariable,
                                                           nom_variableQuery = self.nom_variableQuery,
                                                           variable_min = date_evenement_min,
                                                           variable_max = self.variable_max,
                                                           variable_sort = self.variable_sort,
                                                         )
               
            
            if len(hits) != 0 :
                
                
                hit = hits [len(hits)- 1]
                enreg = hit ['_source']
                date_evenement_min = enreg ['date_evenement']
                timestamp = self.timestamp(date_evenement_min)
                timestamp += .000001
                date_evenement_min = self.fromtimestamp(timestamp)
                
                yield hits
                
            else :
                continue
                
                return
        
        
        return
    
    def timestamp (self, date) :
        d = datetime.strptime(date, self.format_date_standard)
        return datetime.timestamp(d)
    
    def fromtimestamp (self, timestamp) :
        d = datetime.fromtimestamp(timestamp)
        return datetime.strftime(d, self.format_date_standard)
    
        
        
        
        
    def alimentation_bloc (self,ID,):
        """
        fournit un blocs de variables 
            chacun est compris entre reference_min et reference_max 
                                et (ou non) entre ID_min et ID_max (isID )
                                et (ou non) variable_min et variable_max (isVariable) 
                                                        
               
        remarque taille_bloc est une variable systeme (pour disperser les appels à ES)
        
        
        
        """
        
        
        
    
        
        
        for debut_bloc in range(self.ID_reference_min,
                                self.ID_reference_max ,
                                self.taille_bloc ) :
            
            
            
            fin_bloc = debut_bloc + self.taille_bloc
            if fin_bloc > self.ID_reference_max :
                fin_bloc = self.ID_reference_max 

            size = self.size
            
            if self.isTrace :
                print ("1 ____debut lecture bloc____________________________________________________________")
                print ("debut_bloc = ", debut_bloc)
                print ("fin_bloc =", fin_bloc )
                print ("self.taille_bloc =", self.taille_bloc)
                print ('ID_reference_sort =',self.ID_reference_sort)
                print ()
                print ('self.isID =', self.isID)
                print ('self.ID_min =',  self.ID_min)
                print('self.ID_max =', self.ID_max)
                print ()
                print ('self.isVariable =', self.isVariable)
                print ('self.nom_variableQuery =', self.nom_variableQuery)
                print ('self.variable_min =', self.variable_min)
                print ('self.variable_max =', self.variable_max)
                print ('self.isVariable_sort =', self.isVariable_sort)
                print ()
                
                
                
            

            taille_lu, hits = self.kernel.search_par_bloc (self.index_data,
                                                           ID, #deprecated
                                                           debut_bloc,
                                                           fin_bloc,
                                                           size = size,
                                                           ID_reference_sort = self.ID_reference_sort,
                                                           isReference = self.isReference,
                                                           
                                                           isID = self.isID,
                                                           ID_min = self.ID_min,
                                                           ID_max  = self.ID_max ,
                                                           ID_sort  = None,
                                                           
                                                           isVariable = self.isVariable,
                                                           nom_variableQuery = self.nom_variableQuery,
                                                           variable_min = self.variable_min,
                                                           variable_max = self.variable_max,
                                                           variable_sort = 'asc',
                                                         )
            
            
            #reconstitution de l'evenement par ID_reference => ligne ... evenement
            # et mise au fur et à mesure dans dico_globale par ID_reference
            if len(hits) == 0 and not self.isID :
                createur = self.arg_kernel ['createur']
                etape =  "alimentation par bloc"
                message = "dans alimentation sans ID un bloc est vide"
                
                if self.isTrace :
                    print ('#######  pas de hits ?#', taille_lu)
                else :
                    self.kernel.log_warning(createur, etape, message)
                    
                continue
            
            
            if self.isTrace :
                print ('taille_lu =', taille_lu)
                print ('size =', self.taille_bloc * 7)
                print ()
            

            yield hits
        
    
    
    
    def get_ligne_variable (self,ID) :
        """
        recoit bloc à bloc les contenu de chaque variables pour chaque ligne
        ou sur un bloc si isReference is False
        regroupe par ligne (chaque ligne a un unique ID_reference )
        
        renvoie (iterateur) la ligne en forme dico {nom_variable : valeur}
        
        """
        if self.isReference :
            for hits in self.alimentation_bloc(ID) :
                #print ('len(hits) =', len(hits))
                for hit in hits :
                    yield hit['_source']
        else :
            nombre = 0
            for hits in self.alimentation_bloc_date () :
                #print ('len(hits) =', len(hits))
                for hit in hits :
                    nombre += 1
                    yield hit['_source']
            
           
        return
    
    
    def get_ligne (self,ID):
        
        isStart = True
        _isFirst = True
        nombre_variable = 0
        nombre_ligne = 0        
        for _variable in self.get_ligne_variable (ID) :
            
            nombre_variable += 1
            
                        
            if _isFirst :
                _dico_ligne = {'ID' : _variable ['ID'] , 'date_evenement' : _variable ['date_evenement']}
                _ID_reference_courant = _variable  ['ID_reference']
                _isFirst = False          
                
                
            _ID_reference = _variable  ['ID_reference']
            if _ID_reference == _ID_reference_courant :
                _nom_variable = _variable ['nom_variable']
                _dico_ligne [_nom_variable] = _variable ['valeur']
                continue
                   
            # le _dico est valide mais la variable suivante est en cours 
            # copie _dico_ligne pour yield
            # preparation pour la variable suivante
            # yield la copie du dico_ligne
            
            dico_ligne = copy.deepcopy (_dico_ligne)
            _dico_ligne = {'ID' : _variable ['ID'], 'date_evenement' : _variable ['date_evenement'] }
            _nom_variable = _variable ['nom_variable']
            _dico_ligne [_nom_variable] = _variable ['valeur']
            _ID_reference_courant = _variable  ['ID_reference']
            nombre_ligne += 1
            yield dico_ligne
            
        if isStart and not _isFirst:
            
            isStart = False
            nombre_ligne += 1
            yield _dico_ligne
        
            
            
            
        
        
        #print ('nombre_ligne =',nombre_ligne)
        #print ("nombre_variable =", nombre_variable)
        return

        
                         
