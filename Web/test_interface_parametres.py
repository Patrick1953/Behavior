# coding: utf-8
import shutil

from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)

from Interface_parametres import Interface_parametres

def test_interface_parametres () :
    
    I = Interface_parametres ()
    
    liste = I.get_liste_environnements ()
    
    
    
    assert '#test' in liste
    
    dico_evenements = I.get_dico_evenements ('#test')
    
    liste = [cle for cle in dico_evenements.keys()]
    
    
    
    voulu = [ 'pas', 'type', 'position',
             'creation_dictionnaire', ]
      
    assert liste == voulu
    
    I.put_dico_evenements ('test', dico_evenements)
    
    dico_evenements_1 = I.get_dico_evenements ('test')
    
    assert dico_evenements_1 == dico_evenements
    
    dico_evenements ['creation_dictionnaire'] ['date_evenement'] ['travail'] = 'test'
    
    I.put_dico_evenements ('test', dico_evenements)
    dico_evenements_1 = I.get_dico_evenements ('test')
    
    assert dico_evenements_1 == dico_evenements
    
    
    
    # remise en etat
    dico_evenements ['creation_dictionnaire'] ['date_evenement'] ['travail'] = 'date'
    I.put_dico_evenements ('test', dico_evenements)
    dico_evenements_1 = I.get_dico_evenements ('test')
    
    
    format_string = '%Y-%m-%d %H:%M:%S.%f'
    resultat = I.is_good_date (format_string)
    assert resultat == True
    
    format_string = 'toto%Z'
    resultat = I.is_good_date (format_string)
    assert resultat == False
    
    format_string = '%Y-%m-%d %H:%M:%S'
    resultat = I.is_good_date (format_string)
    assert resultat == True
    
    data_type = 'date'
    voulu = 'date'
    resultat = I.type_to_travail (data_type)
    assert voulu == resultat
    
    data_type = 'string'
    voulu = 'analyse_mot'
    resultat = I.type_to_travail (data_type)
    assert voulu == resultat
    
    data_type = 'numeric'
    voulu = 'quantile'
    resultat = I.type_to_travail (data_type)
    assert voulu == resultat
    
    resultat = I.get_liste_travail ( 'date')
    voulu = ['', 'demi_jour', 'jour', 'semaine', 'mois', 'annee','ferie']
    assert resultat == voulu
    
    resultat = I.get_liste_travail ( 'quantile')
    voulu = ['','quartile', 'quintile', 'decile', 'vingtile', 'cinquantile', 'centile', 'manuel']
    assert resultat == voulu
    
    resultat = I.get_liste_travail ( 'pas')
    voulu = ['','demi_jour', 'jour', 'semaine', 'mois', 'annee','trimester']
    assert resultat == voulu
    
    resultat = I.get_dico_evenements (' New_one')
    voulu = {   'creation_dictionnaire': {   'ID': {'parametres': [], 'travail': None},
                                 'date_evenement': {   'parametres': [],
                                                       'travail': 'date'}},
    'pas': {},
    'position': {'ID': None, 'date_evenement': None},
    'type': {   'ID': {'format': 'standard', 'type': 'string'},
                'date_evenement': {'format': None, 'type': 'date'}}}
    
    assert resultat == voulu
    
    resultat = I.call_liste_environnements ()
    voulu ='#test'
    assert voulu in  resultat
    
    resultat = I.get_liste_environnements ()
    
    for voulu in I.liste_choix:
        assert voulu in  resultat
        
        
    resultat = I.get_dico_evenements (I.liste_choix [0])
    
    assert isinstance (resultat, type ({}))
    
    voulu ={   'creation_dictionnaire': {   'ID': {'parametres': [], 'travail': None},
                                 'date_evenement': {   'parametres': [],
                                                       'travail': 'date'}},
    'pas': {},
    'position': {'ID': None, 'date_evenement': None},
    'type': {   'ID': {'format': 'standard', 'type': 'string'},
                'date_evenement': {'format': None, 'type': 'date'}}}
    
    
    
    
    I.save_dico_local (voulu)
    resultat = I.get_dico_local ()
    
    assert resultat == voulu
    
    voulu = {   'creation_dictionnaire': {   'ID': {'parametres': [], 'travail': None},
                                 'date_evenement': {   'parametres': [],
                                                       'travail': 'date'}},
    'pas': {},
    'position': {'ID': 0, 'date_evenement': 2},
    'type': {   'ID': {'format': 'standard', 'type': 'string'},
                'date_evenement': {'format': None, 'type': 'date'}}}
    
    nom_environnement = 'ephemere'
    
    I.save_dico_evenements (nom_environnement, voulu )
    
    resultat = I. get_dico_evenements (nom_environnement)
    
    assert voulu == resultat
    
    voulu = {   'creation_dictionnaire': {   'ID': {'parametres': [], 'travail': None},
                                 'date_evenement': {   'parametres': [],
                                                       'travail': 'date'}},
    'pas': {},
    'position': {'ID': 1, 'date_evenement': 2},
    'type': {   'ID': {'format': 'standard', 'type': 'string'},
                'date_evenement': {'format': None, 'type': 'date'}}}
    
    I.save_dico_evenements (nom_environnement, voulu )
    
    resultat = I. get_dico_evenements (nom_environnement)
    
    assert voulu == resultat
    
    # detruire la directory
    nom_environnement_complet = '#' + nom_environnement
    path = '../data/'+ nom_environnement_complet
    shutil.rmtree(path)
    return
    
    
if __name__ == '__main__' :
    test_interface_parametres ()
    print ('fin test_interface_parametres')
