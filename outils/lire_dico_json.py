# coding: utf-8
import json

def lire_dico_json (pathFile) :
    f = open (pathFile, "r")
    data = f.read()
    f.close()
    dico = json.loads (data)
    return dico
