# coding: utf-8
import os, sys, time, random
import subprocess

#from Reception_alimentation import Reception_alimentation
#from Reception_apprentissage import Reception_apprentissage
#from Reception_Creation_vecteur import Reception_Creation_vecteur
#from Reception_exportation import Reception_exportation

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from lire_dico_json import lire_dico_json
    
from Gestion_commandes import Gestion_commandes
from Gestion_reponses import  Gestion_reponses

class test1 () :
    def __init__ (self, message_retour) :
        
        self.message_retour = message_retour
        
        
    def run () :
        
        nom_appel = self.message_retour ['nom_appel']
        
        assert nom_appel == 'test1'
        
        resultat = self.message_retour ['resultat']
        assert resultat == "merci"
        
        arg = self.message_retour ['arg']
        envoie = self.arg ['envoie']
        assert envoie == 'à vous le test'
        return 
    
    
    

class Emetteur_receveur (Gestion_reponses, Gestion_commandes) :
             
    
    def __init__ (self, ) :
        
        
        #super (Gestion_reponses, Gestion_commandes).__init__()
        super (Gestion_reponses, self).__init__()
        super (Gestion_commandes, self).__init__()
        
        
        nom_environnement = 'general'
        self.path = '../data/'+ nom_environnement + '/parametres/'
        pathReceveur = self.path + 'dico_receveur.json'
        dico_receveur = lire_dico_json (pathReceveur)
                      
        self.temps_attente = dico_receveur ['temps_attente']
        
        self.dico_reception = {'test1' : test1,
                              
                              }
                    
        self.STOP = False
        self.lancement_executeur ()
        
    
    def lancement_executeur (self,) :
        bashCommand = "python lancement_executeur.py"
        self.process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        #output, error = self.process.communicate()
        return
    
    def arret_executeur (self,) :
        self.process.terminate ()
        return
    
        
            
    
    

                
                   
