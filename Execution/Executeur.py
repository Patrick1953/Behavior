# coding: utf-8
import os, sys, time, random

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
    




path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
    
from Gestion_commandes import Gestion_commandes
from Gestion_reponses import  Gestion_reponses
from lire_dico_json import lire_dico_json

path = "../Alimentation"
if path not in sys.path : 
    sys.path.append (path)
from Alimentation import Alimentation

path = "../Apprentissage"
if path not in sys.path : 
    sys.path.append (path)
from Apprentissage import Apprentissage

from Execution import Execution





#from Creation_vecteur import Creation_vecteur
#from Exportation import Exportation

    
    
class test1 () :
    
    def __init__ (self, arg) :
        
        self.arg = arg
        
    def run ( self,) :
        
        texte = self.arg ['test']
        print ('recu =', texte)
        self.arg ['envoie'] = 'à vous le test'
        time.sleep (1) 
        
        
        return "merci de fonctionner"
    
class test2 () :
    
    def __init__ (self, arg) :
        
        self.arg = arg
        
    def run ( self,) :
        
        print ('test2 crash')
        
        1/0
        
        
class test3 () :
    
    def __init__ (self, arg) :
        
        self.arg = arg
        
    def run ( self,) :
        return "coucou"
        
    

    
    
            
    
    
    
    

class Executeur () :
    
    def __init__ (self, ) :
        
        self.Gestion_commandes = Gestion_commandes ()
        self.Gestion_reponses = Gestion_reponses()
           
        
        nom_environnement = 'general'
        self.path = '../data/'+ nom_environnement + '/parametres/'
        pathExecuteur = self.path + 'dico_executeur.json'
        dico_executeur = lire_dico_json (pathExecuteur)
        self.temps_attente = dico_executeur ['temps_attente']

        
        
        self.dico_execution = {'test1' : test1,
                               'test2' : test2,
                               'test3' : test3,
                               'Alimentation' : Alimentation ,
                               'Apprentissage' : Apprentissage,
                               'Execution' : Execution
                              }
        
        self.isStop = False
        
        
            
        
        
         
        
        
    def run (self,) :
        
        
        
        while (True) :
            try: 
                dico, commande = self.Gestion_commandes.get_commande_elligible ()
                
                if commande is None :
                    # appel en stop si toutes commandes sont terminés car crash confirmé ou done confirmé
                    if self.isStop :
                        break
                    temps = random.uniform(1, self.temps_attente + 1) - 1.0
                    time.sleep (temps)
                    continue


                
                
                numero_message = [cle for cle in commande.keys()] [0]
                
                message = commande [numero_message]


                try :
                    comportement = message ['comportement']
                    if comportement == 'STOP':
                        self.isStop = True
                        continue
                except:
                    pass
                
                
                parametres = message  ['parametres']

                nom_appel = parametres ['nom_appel']
                class_appel = self.dico_execution [nom_appel]
                arg = parametres ['arg']
                
                                   
                resultat = class_appel(arg).run()

                parametres_retour = {}
                parametres_retour ['nom_appel'] = nom_appel
                message_retour = {}
                message_retour ['resultat'] = resultat
                message_retour ['parametres'] = parametres_retour
                message_retour ['etat'] = 'done'

                commande_retour = {}
                commande_retour [numero_message] = message_retour
                self.Gestion_reponses.put_reponse (commande_retour, 'done')
                
            except Exception as e:
                message_retour = {}
                message_retour ['etat'] = 'crash'
                message_retour ['exception'] = str(e)
                commande_retour = {}
                commande_retour [numero_message] = message_retour
                self.Gestion_reponses.put_reponse (commande_retour, 'crash')
                
            continue
            


                
                   

    
          
            
