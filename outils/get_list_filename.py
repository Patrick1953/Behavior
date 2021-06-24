# coding: utf-8
import glob

def get_list_filename (mypath,expansion):
    return glob.glob('*.' + expansion)
