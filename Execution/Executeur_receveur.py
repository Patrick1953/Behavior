# coding: utf-8
import os, sys, time, random
import subprocess


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
    
from Gestion_commandes import Gestion_commandes, Gestion_reponses, Gestion_erreurs
from lire_dico_json import lire_dico_json

path = "../Alimentation"
if path not in sys.path : 
    sys.path.append (path)
from Alimentation import Alimentation, Mise_a_jour_alimentation

path = "../Apprentissage"
if path not in sys.path : 
    sys.path.append (path)
from Apprentissage import Apprentissage, Mise_a_jour_apprentissage


from Execution import Execution,  Mise_a_jour_execution
from Gestion_etat import Gestion_receveur

    
    
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
    
    def __init__ (self, nom_worker) :
        
        self.nom_worker = nom_worker
        
        self.Gestion_commandes = Gestion_commandes ()
        self.Gestion_reponses = Gestion_reponses()
        
        
           
        
        
        self.path = '../data/general/parametres/'
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
                if self.isStop :
                    break
                    
                message = self.Gestion_commandes.get_message ()
                
                if message is None :
                    
                    temps = random.uniform(1, self.temps_attente + 1) - 1.0
                    time.sleep (temps)
                    continue
                
                try :
                    comportement = message ['comportement']
                    if comportement == 'STOP':
                        self.isStop = True
                        continue
                except:
                    pass
                
                
                
                # retour running sur ce worker
                message_retour = message
                message_retour ['nom_worker'] = self.nom_worker
                message_retour ['etat'] = 'RUNNING'
                
                
                self.Gestion_reponses.put_message (message_retour,)
                
                nom_appel = message ['nom_appel']
                class_appel = self.dico_execution [nom_appel]
                arg = message ['arg']
                resultat = class_appel(arg).run()
                
                # retour resultat 
                message_retour = message
                message_retour ['resultat'] = resultat
                message_retour ['etat'] = 'OK'
                
                self.Gestion_reponses.put_message (message_retour,)
                
            except Exception as e:
                message_retour = {}
                message_retour ['etat'] = 'KO'
                message_retour ['exception'] = str(e)
                self.Gestion_reponses.put_message (message_retour,)
                
                
            continue
            
    def lancement_executeur (self,) :
        self.creation_lancement ()
        
        bashCommand = "python lancement_executeur.py"
        self.process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        return
    
    def arret_executeur (self,) :
        self.process.terminate ()
        return
    
    def creation_lancement (self,):
        worker = str(self.worker)
        data = """from Executeur import Executeur
Executeur ("""+worker+""").run()
"""
        
        path_file = "lancement_executeur.py"
        f = open (path_file, 'w')
        f.write (data)
        f.close()
            
class Receveur (Gestion_receveur) :
    
    def __init__ (self,) :
        
        
        
        super().__init__ ()
        
        self.Gestion_reponses = Gestion_reponses()
        
        
        self.path = '../data/general/parametres/'
        pathExecuteur = self.path + 'dico_receveur.json'
        dico_executeur = lire_dico_json (pathExecuteur)
        self.temps_attente = dico_executeur ['temps_attente']
        
        
        self.dico_execution = {'test1' : test1,
                               'test2' : test2,
                               'test3' : test3,
                               'Alimentation' : Mise_a_jour_alimentation ,
                               'Apprentissage' : Mise_a_jour_apprentissage,
                               'Execution' : Mise_a_jour_execution
                              }
           
        self.isStop = False
        
        
            
        
        
         
        
        
    def run (self,) :
        
        
        
        while (True) :
            
            try:
                if self.isStop :
                    break
                message = self.Gestion_reponses.get_message ()
                
                if message is None :
                    
                    temps = random.uniform(1, self.temps_attente + 1) - 1.0
                    time.sleep (temps)
                    continue
                
                try :
                    comportement = message ['comportement']
                    if comportement == 'STOP':
                        self.isStop = True
                        continue
                except:
                    pass
                              
                
                etat = essage ['etat']
                if etat == 'RUNNING' :
                    self.tache_running (message)
                    continue
                elif etat == 'OK' :
                    self.tache_OK (message)
                    continue
                elif etat == 'KO' :
                    self.tache_KO (message)
                    continue
                raise ValueError
                
            except Exception as e:
                message_retour = {}
                message_retour ['etat'] = 'erreur_receveur'
                message_retour ['exception'] = str(e)
                self.Gestion_erreurs.put_message (message_retour,)
                
            continue
            
    def lancement_receveur (self,) :
        self.creation_lancement ()
        
        bashCommand = "python lancement_receveur.py"
        self.process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        return
    
    def arret_receveur (self,) :
        self.process.terminate ()
        return
    
    def creation_lancement (self,):
        
        data = """from Executeur import Receveur
Receveur ().run()
"""
        
        path_file = "lancement_receveur.py"
        f = open (path_file, 'w')
        f.write (data)
        f.close()

                
                   

    
          
            
