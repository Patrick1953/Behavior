# coding: utf-8
import time
from Indexation_evenements import indexation
t = time.time()

indexation (pathDico_evenements = "../data/dico_evenements_2.txt",
            pathDico_systeme = "../data/dico_systeme_2.txt",
            isPurge_existing_index = True,
            isTrace = True)



print ("end of job in time =", time.time () - t)
