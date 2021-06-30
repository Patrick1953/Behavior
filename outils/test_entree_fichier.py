# coding: utf-8
import json
from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Entree_fichier import Entree_fichier

def  test_entree_fichier () :
    
    #print ('demarrage')
    
    def lire_file (pathFile) :
        f = open (pathFile, 'r')
        data = f.read()
        return json.loads (data)
    
    nom_environnement = '#test'
    pathSysteme = '../data/' + nom_environnement + '/parametres/dico_evenements_2.json'
    dico_evenements = lire_file (pathSysteme)
    #P(dico_evenements) 
    arg_lecture = dico_evenements  ['environnement']  ['parametres_lecture']
    arg_lecture ['nom_fichier'] = 'evenements.csv'
    
    #P(arg_lecture)
    
    E = Entree_fichier (arg_lecture)
    
    E.init_lecture ()
    
    numero = 0
    for data in E.readIterator () :
        numero += 1
        continue
        
    #print (numero)
    E.close ()   
    assert numero == 192
    
    return

        
    
if __name__ == '__main__' :
    test_entree_fichier ()
    print ('fin test_entree_fichier ')      
    
    
    
    
