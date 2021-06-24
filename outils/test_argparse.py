# coding: utf-8
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("path", help='executeur de tache')
args = parser.parse_args()
print (type(args.path))
print(args.path)
