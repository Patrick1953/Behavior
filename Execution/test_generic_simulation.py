# coding: utf-8
import time, json, os, json, sys
from datetime import datetime
import luigi

from Generic import  Generic_simulation, Generic
from Calcul_bloc_ID import Calcul_bloc_ID, get_liste_bloc


from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)
from Entree_sortie_lock import Entree_sortie_lock
from detruirePath import detruirePath

def test_generic_simulation () :
    t = time.time()
    #  variable pour alimentation bloc
    arg = {}
    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = None
    arg ['isReference'] = False






    arg ['isVariable'] =  True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00.000'
    arg ['variable_max'] = '2021-02-08 00:00:00.000'
    arg ['variable_sort'] = None

    arg ['isID'] = False
    arg ['ID_min'] = ""
    arg ['ID_max']  = ""
    arg ['ID_sort']  = 'asc'
    
    arg ['isTrace'] = False
        
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
    
    pas = 'semaine'
    pas_date = '2021-02-08 00:00:00.000000'.replace (':', '.').replace (' ', '_')
    
    arg ['pathLuigi_file'] = '../data/test/data/'+ pas + '/' + pas_date + '/'
    
    arg_json = json.dumps(arg)
    luigi.build([Calcul_bloc_ID (arg_travail = arg_json)],
                 workers= 1, local_scheduler = True)
    
    
    
    resultat, nombre_ID = get_liste_bloc (arg) 
    arg  ['liste_blocs_ID'] = resultat
    dir_path = arg ['pathLuigi_file']
    detruirePath (dir_path)
    
     
    

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
    
    
    voulu = [   ['couple_cadre_0', 'couple_cadre_1'],
                ['couple_cadre_sup_0', 'couple_cadre_sup_1'],
                ['couple_enfant_cadre_0', 'couple_enfant_cadre_1'],
                ['couple_enfant_cadre_sup_0', 'couple_enfant_cadre_sup_1'],
                ['couple_enfant_ouvrier_0', 'couple_enfant_ouvrier_1'],
                ['couple_ouvrier_0', 'couple_ouvrier_1'],
                ['femme_cadre_0', 'femme_cadre_1'],
                ['femme_cadre_sup_0', 'femme_cadre_sup_1'],
                ['femme_ouvrier_0', 'femme_ouvrier_1'],
                ['homme_cadre_0', 'homme_cadre_1'],
                ['homme_cadre_sup_0', 'homme_cadre_sup_1'],
                ['homme_ouvrier_0', 'homme_ouvrier_1']]
    
    
    assert r == voulu
    
    


    r = T.get_liste_dates ()
    
    

    voulu = [   ['2021-02-01 00:00:00.000000', '2021-02-03 08:00:00.000000'],
    ['2021-02-03 08:00:00.000000', '2021-02-05 16:00:00.000000'],
    ['2021-02-05 16:00:00.000000', '2021-02-08 00:00:00.000000']]
    assert r == voulu
    
    
    

    def simul (arg_travail = None) :
        r = json.loads(arg_travail)
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
        assert len(dico_resultat) < 30
        
        
    arg ['ID_min'] = "couple_cadre_0"
    arg ['ID_max']  = "couple_cadre_sup_1"
    #["couple_cadre_0", "couple_cadre_1", "couple_cadre_sup_0", "couple_cadre_sup_1",]
    arg_travail_json = json.dumps (arg)

    T = MyTask ( arg_travail = arg_travail_json )
    
    T.get_travail()
    
    r = T.get_liste_blocs_ID ()
    
    
    
    voulu = [   ['couple_cadre_0', 'couple_cadre_1'],
                ['couple_cadre_sup_0', 'couple_cadre_sup_1'],
                ['couple_enfant_cadre_0', 'couple_enfant_cadre_1'],
                ['couple_enfant_cadre_sup_0', 'couple_enfant_cadre_sup_1'],
                ['couple_enfant_ouvrier_0', 'couple_enfant_ouvrier_1'],
                ['couple_ouvrier_0', 'couple_ouvrier_1'],
                ['femme_cadre_0', 'femme_cadre_1'],
                ['femme_cadre_sup_0', 'femme_cadre_sup_1'],
                ['femme_ouvrier_0', 'femme_ouvrier_1'],
                ['homme_cadre_0', 'homme_cadre_1'],
                ['homme_cadre_sup_0', 'homme_cadre_sup_1'],
                ['homme_ouvrier_0', 'homme_ouvrier_1']]
    assert r == voulu
    
    
    
    
    
    
    
    return

if __name__ == '__main__' :
    test_generic_simulation ()
    print ('fin test generic_simulation') 
