# coding: utf-8
import sys,  time, os, json
from datetime import datetime
import subprocess

from Emetteur_receveur import Emetteur_receveur

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
    
from Gestion_commandes import Gestion_commandes
from Gestion_reponses import  Gestion_reponses
from lire_dico_json import lire_dico_json

def test_emetteur_receveur () :


    def clean () :
        def detruire (pathFile,) :
            if os.path.exists(pathFile) :
                os.remove(pathFile)
                print ('fichier detruit en ', pathFile)
            else: 
                print ('n existe pas = ', pathFile)

        def verif_vide (pathFile) :
            try:
                f = open (pathFile, 'r')
                data = f.read ()
                resultat = json.loads (data)
                assert resultat == {} , "fichier " + pathFile + " non vide ?"
            except :
                assert False, "fichier " + pathFile + " n'existe pas ?"
            return


        # initialisation à zero des messages    
        nom_environnement = 'general'

        path = '../data/'+ nom_environnement + '/parametres/'
        pathReponses = path + 'dico_reponses.json'
        dico_reponses = lire_dico_json (pathReponses)

        pathFile = path + dico_reponses ['pathFile']
        pathFile_lock = pathFile + ".lock"

        detruire (pathFile_lock)
        detruire (pathFile,)



        pathCommandes = path + 'dico_commandes.json'
        dico_commandes = lire_dico_json (pathCommandes)
        pathFile = path + dico_commandes ['pathFile']
        pathFile_lock = pathFile + ".lock"
        detruire (pathFile_lock,)
        detruire (pathFile,)

        # test init on test en réel le demarrage avec mise à vide de la liste des messages

        R = Emetteur_receveur()
           
        


        path = '../data/'+ nom_environnement + '/parametres/'
        pathReponses = path + 'dico_reponses.json'
        dico_reponses = lire_dico_json (pathReponses)

        pathFile = path + dico_reponses ['pathFile']
        print (pathFile, " et ", os.path.exists(pathFile))
        1/0
        verif_vide (pathFile)

        pathCommandes = path + 'dico_commandes.json'
        dico_commandes = lire_dico_json (pathCommandes)
        pathFile = path + dico_commandes ['pathFile']
        verif_vide (pathFile)

        return

    clean()
    
    def lancement_executeur () :
        bashCommand = "python lancement_executeur.py"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        """
        output, error = process.communicate()
        if not error is None :
            raise ValueError
        """
        return process
    
    def arret_executeur (process) :
        process.terminate ()
        return
    
    #process = lancement_executeur ()
    
    G = Gestion_commandes ()
    R = Gestion_reponses ()

    date = datetime.now()
    date_voulu = date. strftime('%y/%m/%d %H:%M:%S.%f')
    assert isinstance(date_voulu, type(' '))

    message = {'nb_max_worker' : 1, 'nb_max_erreur' : 1, 'date_voulu' : date_voulu, 'nom_appel' : 'test1',
           'parametres' : {'arg' : {'test' : 'hello world nouveau'}, 'nom_appel' : 'test1'}}

    dico, numero_commande = G.put_new_message (message)

    assert numero_commande == 'commande_0'

    time.sleep (1)

    dico, resultat = R.get__liste_reponses ( 'done')



    voulu = {'commande_0': {'resultat': 'merci',
                          'parametres': {'nom_appel': 'test1',
                                         'arg': {'test': 'hello world nouveau',
                                                 'envoie': 'à vous le test'},
                                        },
                          'etat': 'done'},
          }

    assert resultat == voulu


    message = {'resultat': 'merci',
           'parametres': {'nom_appel': 'test2',
                          'arg': {'test': 'hello world nouveau',
                                  'envoie': 'à vous le test'},
                          },
           'etat': 'done'}




    dico, numero_commande = G.put_new_message (message)

    assert numero_commande == 'commande_1'

    time.sleep (1)

    dico, resultat = R.get__liste_reponses ( 'crash')

    assert dico == {}
    
    message = resultat ['commande_1']
    assert message ['exception'] == 'division by zero'
    assert message ['etat'] == 'crash'
    
    arret_executeur (process)
    

    
if __name__ == '__main__' :
    test_emetteur_receveur () 
    print ('fin test_emetteur_receveur')
