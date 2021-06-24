# coding: utf-8
import time, json, os, json
from datetime import datetime
import luigi
from Kernel_BE import Kernel

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


from Generic_simulation import  Generic_simulation, Generic


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
    arg['isTrace'] = True

    arg['isTrace'] = False

    arg['pathDico_evenements'] = "../data/dico_evenements_2.txt"
    arg ['pathDico_systeme'] =  "../data/dico_systeme_2.txt"
    arg ['pathListe_ID'] =  "../data/listeID.txt"
    arg ['etape'] =  'test'

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
    voulu = [['couple_cadre_0', 'couple_enfant_ouvrier_0'],
     ['couple_enfant_ouvrier_1', 'femme_ouvrier_0'],
     ['femme_ouvrier_1', 'homme_ouvrier_1']]
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
    return

if __name__ == '__main__' :
    test_generic ()
    print ('fin test generic') 
