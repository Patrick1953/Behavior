# coding: utf-8

import json, sys
import streamlit as st
from Lanceur_alimentation import Lanceur_alimentation




def execution1 (mon_instance, arg,) :    
    
    
    def display_message (message) :
        st.write (message)
        return
    
    @st.cache (allow_output_mutation = True)
    def get_liste_fichier ():
        if 'nom_environnement' in arg :
            nom_environnement = arg ['nom_environnement']
            liste = mon_instance.get_liste_fichiers (nom_environnement) 
        else:
            liste = []
        return liste
    
    @st.cache (allow_output_mutation = True)
    def get_dico ():
        if 'nom_environnement' in arg :
            dico = mon_instance.get_dico_evenements (arg ['nom_environnement'] )
            return dico
        dico = {'execution' : {},  }
        return dico
    
    
    
    st.header ('Alimentation') 
    dico = get_dico ()    
    liste = get_liste_fichier ()
    
    value = st.sidebar.selectbox("File choice :", liste,)
    
    if value != '' :
        choix = st.radio( "Do you want delete existing data " + nom_delete, ('no', 'yes'))
        if choix == 'yes' :
            st.write('<span style="color:red;font-size:15px;" >'+'Always delete existing data </span>', unsafe_allow_html=True) 
            arg ['isPurge_existing_index'] = True
        if choix == 'no' :
            arg ['isPurge_existing_index'] = False
        isOK = st.radio( "OK for execution ? " + nom_delete, ('no', 'yes'))
        if isOK == 'yes' :
            arg ['nom_fichier'] =  value
            arg ['nom_tache_alimentation'] = value
            Lanceur_alimentation (arg)
            dico = mon_instance.get_dico_evenements (arg ['nom_environnement'] )
            st.stop ()
        

        

        
    
    
    
    st.sidebar.header("Execution state")
    st.sidebar.json(dico ['execution'])
            
    return arg
    
    
  
