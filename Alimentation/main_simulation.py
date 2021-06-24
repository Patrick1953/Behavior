# coding: utf-8
import time
#from Indexation_evenements import indexation
#from Indexation_evenements import delete

# simulation
def indexation (pathDico_evenements = "../data/dico_evenements_2.txt",
                pathDico_systeme = "../data/dico_systeme_2.txt",
                isPurge_existing_index = False,
                isTrace = False,):
    return

def delete (parametre = "", 
            pathDico_evenements = "../data/dico_evenements_2.txt",
            pathDico_systeme = "../data/dico_systeme_2.txt",
            isPurge_existing_index = False,
            isTrace = False,):
    return



t = time.time()

# on lit sur elasticsearch la commande  et ses parametres 
commande = 'insertion' # 'delete'
parametres = ['ajout0000038', ] #ou  ['all', ]

# execution simulée

if commande == 'insertion' :
    
    indexation (pathDico_evenements = "../data/dico_evenements_2.txt",
                pathDico_systeme = "../data/dico_systeme_2.txt",
                isPurge_existing_index = False,
                isTrace = False)

elif commande == 'delete' :
    
    delete (parametre = parametres [0],
            pathDico_evenements = "../data/dico_evenements_2.txt",
            pathDico_systeme = "../data/dico_systeme_2.txt",
            isPurge_existing_index = False,
            isTrace = False)
else :
    """
    ecriture kernel.log_error (" mauvaise commande ") sur elasticsearch
    """
    
# tout c est bien passé
"""
message = "OK with time = "+str(time.time() - t)
ecriture kernel.log_trace (message) sur elasticsearch

fin

"""
    
        
        
        
