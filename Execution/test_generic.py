# coding: utf-8
import time, json, os, json, sys
from datetime import datetime
import luigi


from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
from Generic import  Generic_simulation, Generic


def test_generic () :
    t = time.time()


    arg = {}



    #  variable pour alimentation bloc

    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = 'asc'
    arg ['isReference'] = False
    
    arg ['isVariable'] =  True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00.000'
    arg ['variable_max'] = '2021-02-04 00:00:00.000'
    arg ['variable_sort'] = 'asc'

    arg ['isID'] = True
    arg ['ID_min'] = "couple_cadre_0"
    arg ['ID_max']  = "couple_cadre_1"
    arg ['ID_sort']  = None
    

    arg['isTrace'] = False
    

        
    nom_environnement = 'test'
    arg ['nom_environnement'] =  'nom_environnement'
    
    
    pathFile_evenements = '/dico_evenements_2.json'
    pathFile_systeme = '/dico_systeme_2.json'

    arg_entree_sortie_lock = {} 
    arg_entree_sortie_lock ['nom_environnement'] = nom_environnement
    arg_entree_sortie_lock['pathFile'] = pathFile_evenements
    Entree_sortie_evenements = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_evenements, etat = Entree_sortie_evenements.lire()
    arg ['pathDico_evenements'] = dico_evenements
    
    arg_entree_sortie_lock ['pathFile'] = pathFile_systeme
    Entree_sortie_systeme = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_systeme, etat = Entree_sortie_systeme.lire()
    arg ['pathDico_systeme'] = dico_systeme

    class MyTask (Generic_simulation) :



        #arg_travail = luigi.Parameter(default = "")


        def get_execution (self) :
            self.appels = {'appel' : None,
                          'type_repetition' : 'rien',
                           }
            return

        def output(self):
            self.nom_tache_luigi = 'MyTask'
            return #luigi.LocalTarget("task.txt")

    arg_travail_json = json.dumps (arg)

    T = MyTask ( arg_travail = arg_travail_json )


    T.get_travail()
    
    r = T.get_liste_blocs_ID ()
    
    
    voulu = [['couple_cadre_0', 'couple_cadre_1']]
    assert r == voulu
    
    


    r = T.get_liste_dates ()

    voulu = [['2021-02-01 00:00:00', '2021-02-02 00:00:00'],
     ['2021-02-02 00:00:00', '2021-02-03 00:00:00'],
     ['2021-02-03 00:00:00', '2021-02-04 00:00:00']]
    assert r == voulu
    

    def simul (arg_travail = None) :
        r = json.loads(arg_travail)
        #P(r)
        #print()
        return


    class MyTask1 (Generic_simulation) :



        #arg_travail = luigi.Parameter(default = "")


        def get_execution (self) :
            self.appels = {'appel' : simul,
                          'type_repetition' : 'ID',
                           }
            return

        def output(self):
            self.nom_tache_luigi = 'MyTask'
            return #luigi.LocalTarget("task.txt")


    T = MyTask1 (arg_travail = arg_travail_json)




    class MyTask2 (Generic_simulation) :



        #arg_travail = luigi.Parameter(default = "")


        def get_execution (self) :
            self.appels = {'appel' : simul2,
                          'type_repetition' : 'date_evenement',
                           }
            return

        def output(self):
            self.nom_tache_luigi = 'MyTask'
            return #luigi.LocalTarget("task.txt")

    def simul2 (arg_travail = None) :
        r = json.loads(arg_travail)
        #P(r)
        #print()
        return 'toto'

    T = MyTask2 (arg_travail = arg_travail_json)

    assert T.requires() == ['toto', 'toto', 'toto']
    
    dico_voulu = {'a' : 'aaaaaaaa', 'b' : 'bbbbbbbbbbbbbb', 'c' : 'ccccc'}
    fout = open('test.json', 'w')
    T.ecrire_luigi_file (fout, dico_voulu)
    fout.close()
    
    fin = open('test.json', 'r')
    dico_resultat = T.lire_luigi_file(fin)
    fin.close()
    
    assert dico_resultat == dico_voulu
    
    dico_voulu = {}
    for i in range(0,  100) :
        dico_voulu [str(i)] = 'aaaaaa'
        
    fout = open('test.json', 'w')
    T.ecrire_luigi_file (fout, dico_voulu)
    fout.close()
    
    T.dico_systeme ['calcul'] ['pourcentage_echantillon'] = 10
    
    
    for i in range(0, 100) :
        fin = open('test.json', 'r')
        dico_resultat = T.lire_luigi_file_random (fin)
        fin.close()
        assert len(dico_resultat) < 20
    
    
    
    
    
    
    
    return

if __name__ == '__main__' :
    test_generic ()
    print ('fin test generic') 
