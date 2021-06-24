# coding: utf-8

import json, sys
import streamlit as st



path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from Interface_parametres import Interface_parametres


def page1 (mon_instance, dico,) :    
    
    
    def display_message (message) :
        st.write (message)
        return
    
    
    
    st.header ('Enter zone and its position') 
    
    
    nom  = st.text_input ('Enter new zone ?', value = "", )
    
    if nom != '' :
        value = st.number_input('Enter ' + nom + ' range',  min_value= 0, max_value= 1000,)
        dico ['position' ] [nom] = value
        dico ['type'] [nom] = {'format': None, 'type': None}
        dico ['creation_dictionnaire'] [nom] = {'travail' : None,
                                                'parametres' : []}
        mon_instance.save_dico_local (dico)
        

    liste = [nom for nom in dico ['position' ].keys() if nom != 'ID' and nom != 'date_evenement' ]
     
    for nom_delete in liste :
        choix = st.radio( "Do you want delete " + nom_delete, ('no', 'yes'))
        if choix == 'yes' :
            st.write('<span style="color:red;font-size:15px;" >'+'Always delete ' + nom_delete + '</span>', unsafe_allow_html=True) 
            del dico ['position'] [nom_delete]
            del dico ['type'] [nom_delete]
            del dico ['creation_dictionnaire'] [nom_delete]
            mon_instance.save_dico_local (dico)
        
        st.write('' )
        continue
        

        
    
    
    
    st.sidebar.header("Zones")
    st.sidebar.json(dico ['position'])

    
    
    
    
    
        
    return
    
    
  
