# coding: utf-8
from pathlib import Path
import os
import shutil


def calcul_pas (path) :
    """
    dernier folder dans le chemin du modele
    """
    monPath = Path (path)
    liste = monPath.parts
    liste = liste[:-1]
    return liste [len(liste)-1]
