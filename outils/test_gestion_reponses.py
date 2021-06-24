# coding: utf-8
import os, json
from datetime import datetime
from lire_dico_json import lire_dico_json


from Gestion_reponses import Gestion_reponses

def test_gestion_reponses () :
    
    nom_environnement = 'general'
       
    # on clean le fichier d'echange
    path = '../data/'+ nom_environnement + '/parametres/'
                
    pathReponses = path+'dico_reponses.json'
    dico_commandes = lire_dico_json (pathReponses)
    
    pathFile_echanges = path + dico_commandes ['pathFile']
    
    
    try:
        os.remove(pathFile_echanges)
    except:
        pass
    
    pathFile_lock = pathFile_echanges + ".lock"
    try:
        os.remove(pathFile_lock)
    except:
        pass
      
    
        
    G = Gestion_reponses ()
    
    message = {'parametres' : {'test' : 'OK'} }
    entete = "command_"
    
    etat = 'done'
    for i in range(0, 5) :
        cle = entete + str(i)
        commande = {}
        commande [cle] = message
        G.put_reponse (commande, etat)
        
        
    etat = 'crash'
    for i in range(5, 8) :
        cle = entete + str(i)
        commande = {}
        commande [cle] = message
        G.put_reponse (commande, etat)
    
    
    etat = 'crash' 
    dico, resultat = G.get_dico_reponses_crash ()
    assert (len(dico) == 8)
    assert (len(resultat)) == 3
    
    
    etat = 'done' 
    dico, resultat = G.get_dico_reponses_done ()
    assert (len(dico) == 8)
    assert (len(resultat)) == 5
    
    # on recupere et retire tous les non_lus
    etat = 'non_lu'
    dico, resultat = G.get_dico_a_lire (etat)   
    assert (len(dico) == 0)
    assert (len(resultat)) == 8
    
    
    
    
    
if __name__ == '__main__' :
    test_gestion_reponses ()
    print ('fin test_gestion_reponses') 
    
    
