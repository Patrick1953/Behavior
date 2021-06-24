# coding: utf-8
import json
import time
from datetime import datetime

from Kernel_BE import Kernel


class lecture_log:
    def __init__(
        self,
        arg_kernel={
            "createur": "generic",
            "date_emetteur": str(datetime.now()),
            "http_auth": None,
            "timeout": 10,
            "host": "localhost",
            "port": 9200,
            "zipChoisi": "bz2",
            "index_log_error": "trace1",
            "index_log_warning": "trace2",
            "index_log_trace": "trace3",
            "index_system": "systeme",
            "isPurge_existing_index_log": False,
            "extra_elasticsearch_args": None,
            "trace": False,
            "_ID_reference_base": "000000000000000000000000000000",
        },
    ):
        self.kernel = Kernel(arg_kernel)
        self.liste_nom_dico_lu = [
            "origine",
            "auteur",
            "etape",
            "date",
            "message",
        ]

    def lecture_trace(self, with_print=True):

        resultat = self.kernel.get_logs_trace()
        if with_print:
            self.Print(resultat)
        return resultat

    def lecture_warning(self, with_print=True):

        resultat = self.kernel.get_logs_warning()
        if with_print:
            self.Print(resultat)
        return resultat

    def lecture_error(self, with_print=True):

        resultat = self.kernel.get_logs_error()
        if with_print:
            self.Print(resultat)
        return resultat

    def Print(self, resultat):

        if len(resultat) == 0:
            return
        for dico in resultat:
            ligne = self.create_ligne(dico)
            print(ligne)
            continue
        print("\n")

        return

    def create_ligne(self, dico):
        r = []
        for nom in self.liste_nom_dico_lu:
            if nom == "message":
                r.append(" " + dico[nom])
                continue
            r.append((" " + dico[nom] + "          ")[:20])
            continue
        ligne = "|".join(r)
        return ligne
