# coding: utf-8
import json
from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Kernel_entree import Kernel_entree

def  test_kernel_entree () :
    def lire_file (pathFile) :
        f = open (pathFile, 'r')
        data = f.read()
        return json.loads (data)
    
    pathEvenements = '../data/#test/parametres/dico_evenements_2.json'
    dico_systeme = lire_file (pathEvenements)
           
    arg_kernel_fichier = dico_systeme  ['environnement']['parametres_lecture']
    arg_kernel_fichier ['nom_fichier'] = 'evenements.json'
    
    E = Kernel_entree (arg_kernel_fichier)
    
    E.init_lecture ()
    
    numero = 0
    for data in E.readIterator () :
        numero += 1
        continue
    E.close ()   
    assert numero == 192
    
    return

        
    
if __name__ == '__main__' :
    test_kernel_entree ()
    print ('fin test_kernel_entree ')    
