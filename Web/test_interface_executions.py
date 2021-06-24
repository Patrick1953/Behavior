# coding: utf-8
import shutil

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Interface_executions import Interface_executions

def test_interface_executions () :
    nom_environnement = '#test'
    I = Interface_executions ()
    
    liste = I.get_liste_environnements ()
    
    assert nom_environnement in liste
    
    dico_evenements = I.get_dico_evenements (nom_environnement)
    
    liste = [cle for cle in dico_evenements.keys()]

    
    voulu = ['environnement','alimentation', 'pas', 'apprentissage', 'type', 'position',
             'creation_dictionnaire', 'dictionnaire']
    
    #print (liste)
    assert liste == voulu
    
    liste = I.get_liste_fichiers (nom_environnement)
    voulu = ['evenements.json']
    
    #print (liste)
    assert liste == voulu
    
    
    return
    
    
if __name__ == '__main__' :
    test_interface_executions ()
    print ('fin test_interface_executions')
