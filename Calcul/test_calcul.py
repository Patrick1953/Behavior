# coding: utf-8
import random, time, copy, json, sys
from datetime import datetime

from Calcul import Calcul


path = "../outils"
if path not in sys.path : 
    sys.path.append (path)

from Entree_sortie_lock import Entree_sortie_lock
from Kernel_BE import Kernel





from pprint import PrettyPrinter 
def P (stuff , pp = PrettyPrinter(indent=4)) :
    return pp.pprint(stuff)


def  test_calcul () :
    arg = {}
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
    #P (dico_evenements)

    arg_entree_sortie_lock ['pathFile'] = pathFile_systeme
    Entree_sortie_systeme = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_systeme, etat = Entree_sortie_systeme.lire()
    arg ['pathDico_systeme'] = dico_systeme
    
    
    
    #  variable pour alimentation bloc

    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = 'asc'
    arg ['isReference'] = False






    arg ['isVariable'] =  True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00'
    arg ['variable_max'] = '2021-02-04 00:00:00'
    arg ['variable_sort'] = 'asc'

    arg ['isID'] = True
    arg ['ID_min'] = "couple_cadre_1"
    arg ['ID_max']  = "couple_cadre_sup_1"
    arg ['ID_sort']  = None
    arg ['isTrace'] = False

    C = Calcul (arg)
    
    
    
    

    resultat = C.calcul_paragraphe()
    
    #P(resultat)
    
    
    


    voulu = {   'couple_cadre_1': [   'date_evenement_bpm',
                          'date_evenement_mercredi',
                          'date_evenement_5',
                          'date_evenement_fevrier',
                          'date_evenement_2021',
                          'date_evenement_non_ferie',
                          'autres',
                          'bio',
                          'bas',
                          'normal',
                          'ue',
                          'autres',
                          'bio',
                          'bas',
                          'normal',
                          'prix_quartile_3',
                          'prix_decile_7',
                          'prix_manuel1_3',
                          'prix_panier_quartile_3',
                          'date_evenement_bpm',
                          'date_evenement_mercredi',
                          'date_evenement_5',
                          'date_evenement_fevrier',
                          'date_evenement_2021',
                          'date_evenement_non_ferie',
                          'pomme',
                          'de',
                          'terre',
                          'bio',
                          'bas',
                          'normal',
                          'espagne',
                          'pomme',
                          'de',
                          'terre',
                          'bio',
                          'bas',
                          'normal',
                          'prix_quartile_3',
                          'prix_decile_7',
                          'prix_manuel1_3',
                          'prix_panier_quartile_3',
                          'date_evenement_bpm',
                          'date_evenement_mercredi',
                          'date_evenement_5',
                          'date_evenement_fevrier',
                          'date_evenement_2021',
                          'date_evenement_non_ferie',
                          'pomme',
                          'de',
                          'terre',
                          'bio',
                          'bas',
                          'normal',
                          'espagne',
                          'pomme',
                          'de',
                          'terre',
                          'bio',
                          'bas',
                          'normal',
                          'prix_quartile_3',
                          'prix_decile_7',
                          'prix_manuel1_3',
                          'prix_panier_quartile_3'],
    'couple_cadre_sup_0': [   'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'pomme',
                              'de',
                              'terre',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'pomme',
                              'de',
                              'terre',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'autres',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'autres',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_3',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_4',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'laitue',
                              'standart',
                              'moyen',
                              'normal',
                              'france',
                              'laitue',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_9',
                              'prix_manuel1_3',
                              'prix_panier_quartile_4',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'pomme',
                              'de',
                              'terre',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'pomme',
                              'de',
                              'terre',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_4',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'pomme',
                              'de',
                              'terre',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'pomme',
                              'de',
                              'terre',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_4',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'pomme',
                              'de',
                              'terre',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'pomme',
                              'de',
                              'terre',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'carotte',
                              'standart',
                              'moyen',
                              'normal',
                              'espagne',
                              'carotte',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_3',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3'],
    'couple_cadre_sup_1': [   'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'carotte',
                              'standart',
                              'moyen',
                              'normal',
                              'espagne',
                              'carotte',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_3',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'autres',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'autres',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_3',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'ue',
                              'orange',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_3',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'laitue',
                              'standart',
                              'moyen',
                              'normal',
                              'france',
                              'laitue',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_9',
                              'prix_manuel1_3',
                              'prix_panier_quartile_4',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'carotte',
                              'standart',
                              'moyen',
                              'normal',
                              'espagne',
                              'carotte',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_3',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_4',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'laitue',
                              'standart',
                              'moyen',
                              'normal',
                              'france',
                              'laitue',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_4',
                              'prix_decile_9',
                              'prix_manuel1_3',
                              'prix_panier_quartile_4',
                              'date_evenement_bpm',
                              'date_evenement_mardi',
                              'date_evenement_5',
                              'date_evenement_fevrier',
                              'date_evenement_2021',
                              'date_evenement_non_ferie',
                              'carotte',
                              'standart',
                              'moyen',
                              'normal',
                              'espagne',
                              'carotte',
                              'standart',
                              'moyen',
                              'normal',
                              'prix_quartile_3',
                              'prix_decile_8',
                              'prix_manuel1_3',
                              'prix_panier_quartile_4']}
    
    
    
    
    
    
    for cle in resultat.keys() :
        
        if not cle in voulu :
            print (cle, " pas dans voulu")
            continue
        l1 = resultat [cle]
        l2 = voulu [cle]
        if l1 != l2 :
            print ('differents')
            i = 0
            for mot1 in l1 :
                mot2 = l2 [i]
                if mot1 != mot2 :
                    print (mot1, ' != ', mot2)
                i += 1
                
                
        continue

    assert voulu == resultat
    
    arg = {}
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
    #P (dico_evenements)

    arg_entree_sortie_lock ['pathFile'] = pathFile_systeme
    Entree_sortie_systeme = Entree_sortie_lock (arg_entree_sortie_lock)
    dico_systeme, etat = Entree_sortie_systeme.lire()
    arg ['pathDico_systeme'] = dico_systeme
    
    
    
    #  variable pour alimentation bloc

    arg ['ID_reference_min'] = 0
    arg ['ID_reference_max'] = 100000000
    arg ['ID_reference_sort'] = None
    arg ['isReference'] = False






    arg ['isVariable'] = True
    arg ['nom_variableQuery'] = "date_evenement"
    arg ['variable_min'] = '2021-02-01 00:00:00'
    arg ['variable_max'] = '2021-02-08 00:00:00'
    arg ['variable_sort'] = 'asc'

    arg ['isID'] = True
    arg ['ID_min'] = "couple_cadre_0"
    arg ['ID_max']  = "homme_ouvrier_1"
    arg ['ID_sort']  = 'asc'
    arg ['isTrace'] = False

    C = Calcul (arg)
    
    resultat = C.calcul_paragraphe()
    
    liste_ID = [ID for ID in resultat.keys()]

    liste_ID.sort()
    #P(liste_ID)
    voulu = ["couple_cadre_0", "couple_cadre_1", "couple_cadre_sup_0", "couple_cadre_sup_1",
             "couple_enfant_cadre_0", "couple_enfant_cadre_1", "couple_enfant_cadre_sup_0",
             "couple_enfant_cadre_sup_1", "couple_enfant_ouvrier_0", "couple_enfant_ouvrier_1",
             "couple_ouvrier_0", "couple_ouvrier_1", "femme_cadre_0", "femme_cadre_1",
             "femme_cadre_sup_0", "femme_cadre_sup_1", "femme_ouvrier_0", "femme_ouvrier_1",
             "homme_cadre_0", "homme_cadre_1", "homme_cadre_sup_0", "homme_cadre_sup_1",
             "homme_ouvrier_0", "homme_ouvrier_1"]
    
    voulu.sort()
    
    assert liste_ID == voulu
            
    return

if __name__ == '__main__' :
    t = time.time()
    test_calcul ()
    print ('fin test calcul en ', time.time() - t)    
 
