# coding: utf-8
import json

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Execution import Execution_ID
import luigi

arg = {}


#  variable pour alimentation bloc

arg ['ID_reference_min'] = 0
arg ['ID_reference_max'] = 100000000
arg ['ID_reference_sort'] = 'asc'
arg ['isReference'] = False




arg ['isVariable'] =  True
arg ['nom_variableQuery'] = "date_evenement"
arg ['variable_min'] = '2021-02-01 00:00:00'
arg ['variable_max'] = '2021-02-09 00:00:00'
arg ['variable_sort'] = 'asc'

arg ['isID'] = True
arg ['ID_min'] = "couple_cadre_0"
arg ['ID_max']  = "homme_ouvrier_1"
arg ['ID_sort']  = None
arg ['isTrace'] = False

arg ['pathListe_ID'] =  "../data/listeID.txt"
arg ['pathDico_evenements'] = '../data/dico_evenements_2.txt'
arg ['pathDico_systeme'] = '../data/dico_systeme_2.txt'
arg['pathModele'] = '../data/temp/test/Modele.model'
arg ['etape'] =  'test'

arg_json = json.dumps (arg)

if __name__ == '__main__':
    luigi.build([Execution_ID (arg_travail = arg_json)],
                 workers=2, local_scheduler = True)
    
    

print ('fin test Execution')
