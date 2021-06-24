# coding: utf-8
import random
from Entree_sortie_lock import Entree_sortie_lock


class Gestion_commandes (Entree_sortie_lock):
    """
    entete = "commande_"
    
    etat de la  commande = 'demande', 'running', 'done'
    
    nb_max_worker = nombre de worker maximum à lancer
    nb_courant_worker = nb de worker en cours d'execution
    nb_max_erreur = nombre de erreur maximum à accepter
    nb_courant_erreur = nb de erreur en cours d'execution 
    
    commande = {numero : {etat, nb_max_worker , nb_courant_worker,
                               nb_max_erreur , nb_courant_erreur,
                               parametres : {execution},
                            }
    
    appels :
    
    put_new_message (message)   
         => dico, numero 
         
    get_commande_elligible ()
        => dico, commande OU dico, None
    
    finish_commande (numero)
        => dico, 'OK' OU dico, 'done'
        
    crash_commande (self,numero)
        => => dico, 'OK' OU dico, 'crash'
     
    """
    
    def __init__ (self, arg) :
        
        super ().__init__ (arg)
        self.entete = arg ['entete']
        self.len_entete = len(self.entete)
        
      
    
    def get_new_numero (self, dico) :
        
        if len(dico) == 0 :
            return  self.entete+str(0)
        liste_cle_numero = [int(cle [self.len_entete:]) for cle in dico.keys()]
        numero_max = max(liste_cle_numero) + 1
        
        return self.entete+str(numero_max)
    
    
    
    def _put_new_message (self, dico, message) :
        
        cle = self.get_new_numero (dico)
        dico [cle] = message
        
        return dico, cle
    
    def put_new_message (self, message) :
        """
        mis etat demande et positionne le nombre deworkers  permis
        """
        message ['etat'] = 'demande'
        message ['nb_courant_worker'] = 0
        message ['nb_courant_erreur'] = 0
        
        return self.execution_with_lock (self._put_new_message, data = message)
    
    def isElligible_pour_execution (self, message) :
        
        etat = message ['etat']
        if etat == 'done' :
            return False
        
        nb_max_worker = message ['nb_max_worker']
        nb_courant_worker = message ['nb_courant_worker']
        if nb_courant_worker >= nb_max_worker :
            return False
        
        return True
    
    def _get_commande_elligible (self, dico, data) :
        liste_cle_elligible = []
        for cle, message in dico.items() :
            if not self.isElligible_pour_execution (message):
                continue
            liste_cle_elligible.append (cle)
            continue
        
        if len(liste_cle_elligible) == 0 :
            return dico , None
        
        # on sort la cle elligible random 
        cle_elligible = random.sample (liste_cle_elligible, 1) [0]
        
        message = dico [cle_elligible]
        message ['etat'] = 'running'
        message ['nb_courant_worker'] += 1
        dico [cle_elligible] = message
        commande = {}
        commande [cle_elligible] = message
        return dico, commande
    
    def get_commande_elligible (self,) :
        return self.execution_with_lock (self._get_commande_elligible, data = None)
        
    
    def _finish_commande (self,dico, numero) :
        
        message = dico [numero]
        nb_courant_worker = message ['nb_courant_worker']
        nb_courant_worker -= 1
        message ['nb_courant_worker'] = nb_courant_worker
                
        if nb_courant_worker > 0 :
            dico [numero] = message
            return dico, 'OK'
        
        message ['etat'] = 'done'
        dico [numero] = message
        return dico, 'done'
    def finish_commande (self,numero) :
        return self.execution_with_lock (self._finish_commande, data = numero)
    
    def _crash_commande (self,dico, numero) :
        
        message = dico [numero]
        
        nb_courant_worker = message ['nb_courant_worker']
        nb_courant_worker -= 1
        message ['nb_courant_worker'] = nb_courant_worker
        
        nb_courant_erreur = message ['nb_courant_erreur']
        nb_courant_erreur += 1
        message ['nb_courant_erreur'] = nb_courant_erreur
        
        nb_max_erreur = message ['nb_max_erreur']
        if nb_courant_erreur >= nb_max_erreur :
            message ['etat'] = 'done'
            dico [numero] = message
            return dico, 'crash'
        
        dico [numero] = message
        return dico, 'OK'
    def crash_commande (self,numero) :
        return self.execution_with_lock (self._crash_commande, data = numero)
    
    
    

        
        
        
