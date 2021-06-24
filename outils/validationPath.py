# coding: utf-8
from pathlib import Path
import os
import shutil
 


def validationPath (path, suffix = {'.txt' : None,
                                '.json':None,
                                ".model": None,
                                    ".lock" : None,
                               },
               ) :
    
    
    path = os.path.realpath (path)
    if os.path.exists (path):
        return path
    monPath = Path (path)
    liste = monPath.parts
    
    if monPath.suffix in suffix :
        liste = liste [:-1]
    newPath = "/".join(liste)
    
    if os.path.exists (newPath):
        return path
    
    os.makedirs (newPath)
    return path




    
    
    
    
    
