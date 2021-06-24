# coding: utf-8
from  lecture_log import lecture_log
import os

def Lire () :
    
    L = lecture_log ()



    debut_message = ""
    while (True) :

        message = debut_message + """logs:
        trace   : 1 
        warning : 2 
        error   : 3  
        \n
        FIN     : 4 """

        rep1 = input(message)
        print ('\n\n')
        try :
            x = int (rep1)
        except:
            debut_message = " faite attention BORDEL !!!! \n"
            continue

        if x < 1 or x > 4  :
            debut_message = " faite attention BORDEL !!!! \n"
            continue

        if x == 4 :
            break
        if x == 1 :
            L.lecture_trace ()
        if x == 2 :
            L.lecture_warning ()
        if x == 3 :
            L.lecture_error ()
        debut_message = ""
        continue

        
