# coding: utf-8
import argparse

    
parser = argparse.ArgumentParser()
parser.add_argument("nom_environnement", help='executeur de tache param = nom_environnement (test)')
args = parser.parse_args()
nom_environnement = args.params


arg_executeur = {}
arg_executeur ['nom_environnement'] = nom_environnement

print ('execution lancée', nom_environnement)
