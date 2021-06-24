# coding: utf-8
from Entree_sortie_lock import  Entree_sortie_lock
from lire_dico_json import lire_dico_json


class  Gestion_reponses(Entree_sortie_lock ):
    """
     init voir Entree_sortie_lock
    
    -insertion_done (message, etat): met le message dans le fichier 
        en utilisant la cle du message 
        avec etat == etat fourni
        return  dico , "?"
    
        
        
    -appel get_liste_reponse (etat) : recupere tous les message (etat) et les supprime
        return dico, dico(tous les messages etat == etat demande)
    
    
    
    """
    def __init__ (self, ) :
        
        nom_environnement = 'general'
        self.path = '../data/'+ nom_environnement + '/parametres/'

        pathCommandes = self.path + 'dico_reponses.json'
        dico_commandes = lire_dico_json (pathCommandes)


        self.entete = dico_commandes ['en_tete']
        self.len_entete = len(self.entete)


        arg_ES = {}
        arg_ES ['nom_environnement'] = nom_environnement
        arg_ES ['pathFile'] = dico_commandes ['pathFile']

        Entree_sortie_lock.__init__ (self,arg_ES)
        #super ().__init__ (arg_ES)
    
    def _put_reponse (self, dico, commande) :
        cle = [cle for cle in commande.keys()] [0]
        message =commande [cle]
        dico [cle] = message
        return dico, 'OK'
          
    
    def put_reponse (self, commande, etat) :
        cle = [cle for cle in commande.keys()] [0]
        message = commande [cle]
        message ['etat'] = etat
        commande [cle] = message
        return self.execution_with_lock (self._put_reponse, data = commande)
    
    def _get_dico_reponses (self, dico, type_etat) :
        nouveau_dico = {}
        resultat = {}
        for cle, message in dico.items() :
            if message ['etat'] == type_etat :
                    resultat [cle] = message
                    message ['etat'] = 'non_lu'
                    nouveau_dico [cle] = message
                    continue
            nouveau_dico [cle] = message
            continue
        return nouveau_dico, resultat
    
    def get_dico_reponses_done (self,) :
        return self.execution_with_lock (self._get_dico_reponses, data = 'done')
    def get_dico_reponses_crash (self, ) :
        return self.execution_with_lock (self._get_dico_reponses, data = 'crash')
    
    
    def _get_dico_a_lire (self, dico, type_etat) :
        nouveau_dico = {}
        resultat = {}
        for cle, message in dico.items() :
            if message ['etat'] == type_etat :
                    resultat [cle] = message
                    continue
            nouveau_dico [cle] = message
            continue
        return nouveau_dico, resultat
    
    def get_dico_a_lire (self, etat) :
        return self.execution_with_lock (self._get_dico_a_lire, data = etat)
        
