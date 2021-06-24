# coding: utf-8
import shutil


def detruirePath(dir_path ) :
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))
