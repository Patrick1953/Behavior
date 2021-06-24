# coding: utf-8
import sys,  time, os, json
from datetime import datetime
import subprocess
from pprint import PrettyPrinter 
def PP (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Executeur import Executeur

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
    
from Gestion_commandes import Gestion_commandes
from Gestion_reponses import  Gestion_reponses

from lire_dico_json import lire_dico_json

def test_executeur () :


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

        E = Executeur()




        path = '../data/'+ nom_environnement + '/parametres/'
        pathReponses = path + 'dico_reponses.json'
        dico_reponses = lire_dico_json (pathReponses)

        pathFile = path + dico_reponses ['pathFile']
        verif_vide (pathFile)

        pathCommandes = path + 'dico_commandes.json'
        dico_commandes = lire_dico_json (pathCommandes)
        pathFile = path + dico_commandes ['pathFile']
        verif_vide (pathFile)

        return

    clean()
    
    
    
    
    
    G = Gestion_commandes ()
    R = Gestion_reponses ()

    date = datetime.now()
    date_voulu = date. strftime('%y/%m/%d %H:%M:%S.%f')
    assert isinstance(date_voulu, type(' '))

    message = {'nb_max_worker' : 1, 'nb_max_erreur' : 1, 'date_voulu' : date_voulu, 'nom_appel' : 'test1',
           'parametres' : {'arg' : {'test' : 'hello world nouveau'}, 'nom_appel' : 'test1'}}

    dico, numero_commande = G.put_new_message (message)

    assert numero_commande == 'commande_0'

    time.sleep (2)

    dico, resultat = R.get_dico_reponses_done ()
    


    voulu = {'commande_0': {'resultat': 'merci de fonctionner',
                          'parametres': {'nom_appel': 'test1',
                                         'arg': {'test': 'hello world nouveau',
                                                 'envoie': 'à vous le test'},
                                        },
                          'etat': 'non_lu'},
          }
    
    
    #print (resultat)
    assert resultat == voulu


    message = {'resultat': 'merci',
              'parametres': {'nom_appel': 'test2',
                          'arg': {'test': 'hello world nouveau',
                                  'envoie': 'à vous le test'},
                          },
                'etat': 'done'}




    dico, numero_commande = G.put_new_message (message)

    assert numero_commande == 'commande_1'

    time.sleep (1.5)

    dico, resultat = R.get_dico_reponses_crash ()
    
    assert dico == {'commande_0': {'resultat': 'merci de fonctionner',
                                   'parametres': {'nom_appel': 'test1',
                                                  'arg': {'test': 'hello world nouveau',
                                                          'envoie': 'à vous le test'}},
                                   'etat': 'non_lu'},
                    'commande_1': {'etat': 'non_lu',
                                   'exception': 'division by zero'}
                   }
    
    message = resultat ['commande_1']
    assert message ['exception'] == 'division by zero'
    assert message ['etat'] == 'non_lu'
    

    
    def lire_file (pathFile) :
        f = open (pathFile, 'r')
        data = f.read()
        return json.loads (data)
    
    pathEvenements = '../data/test/parametres/dico_evenements_2.json'
    pathSysteme = '../data/test/parametres/dico_systeme_2.json'
    nom_environnement = 'test'
    
    dico_evenements = lire_file (pathEvenements)
    dico_systeme = lire_file (pathSysteme)
    
    
    arg = {}
    arg ['nom_environnement'] = nom_environnement
    arg ['isPurge_existing_index'] = True
    
    message = {'parametres' : {'arg' : arg, 'nom_appel' : 'Alimentation'}}
    
    # demande pour alimentation
    dico, numero_commande = G.put_new_message (message)
    time.sleep (2)
    
    dico, resultat = R.get_dico_reponses_crash ()
    
    assert resultat == {}
    
    # test Apprentissage
    nom_environnement = 'test'
    pathFile_evenements = '/dico_evenements_2.json'
    pathFile_systeme = '/dico_systeme_2.json'
    
    arg = {}
    arg ['isTrace'] = False
    arg ['nom_environnement'] = nom_environnement
    
    arg ['variable_min'] = '2021-02-01 00:00:00'
    arg ['variable_max'] = '2021-03-30 00:00:00'
    
    message = {'parametres' : {'arg' : arg, 'nom_appel' : 'Apprentissage'}}
    
    dico, numero_commande = G.put_new_message (message)
    
    time.sleep (2)
    
    dico, resultat = R.get_dico_reponses_crash ()
    
    assert resultat == {}
    
    
    
    
def lancement_executeur () :
    bashCommand = "python lancement_executeur.py"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    
    return process

def arret_executeur (process) :
    process.terminate ()
    return
    

    
if __name__ == '__main__' :
    process = lancement_executeur ()
    
    try :
        test_executeur () 
    except:
        arret_executeur (process)
        raise
        
        
    print ('fin test_executeur')
    
    
