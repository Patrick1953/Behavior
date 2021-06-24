# coding: utf-8

import json, sys
import streamlit as st








def page5 (mon_instance, dico_general, isCall = True) :    
    
    
    def display_message (message) :
        st.write (message)
        return
    
    
    
    
    @st.cache (allow_output_mutation = True)
    def get_liste_environnement ():
        resultat = ['', ]
        liste = mon_instance.get_liste_environnements ()
        liste [0] = 'New environment'
        resultat.extend(liste)
        return resultat
    
    
    @st.cache (allow_output_mutation = True)
    def save_parametres (nom_environnement, dico_general):
        mon_instance.save_dico_evenements (nom_environnement, dico_general)
        return
    
    
     
    
    
    st.header ('Save parameters')
    
    st.write ()
    agree6 = st.checkbox('Stop', key ='stop' )
    if agree6:
        mon_instance.save_dico_local (dico_general)
        st.stop()
    
    liste_choix = get_liste_environnement ()
    nom_environnement  = st.selectbox("Environment choice :", liste_choix, key = 'save_dico' )
    
    if nom_environnement != '' and nom_environnement != 'New environment' :
        choix = st.radio( 'Are you sure ? ', ('no', 'yes'))
        if choix == 'yes' :
            #st.write('no new')
            save_parametres (nom_environnement, dico_general)
            st.stop()
            
    if nom_environnement == 'New environment':
         
        new_environnement = st.text_input ('Enter new name ?', value = "", )
        if new_environnement != "" :
            if new_environnement in liste_choix :
                st.write('<span style="color:red;font-size:15px;" >'+'Not new name ? </span>', unsafe_allow_html=True)
            if not new_environnement in liste_choix :
                choix = st.radio( 'Are you sure ? ', ('no', 'yes'))
                if choix == 'yes' :
                    #st.write('new')
                    save_parametres (new_environnement, dico_general)
                    st.stop()
                
        
            
    
    
    
    
        
      
    
    display_message ('')
    
    col1, col2, col3, col4 = st.beta_columns(4)
    
    with col1:
        st.header("Zones")
        st.json(dico_general ['position'])

    with col2:
        st.header("Zone format")
        st.json(dico_general ['type'])
        
    with col3:
        st.header("Behavior measument")
        st.json(dico_general ['creation_dictionnaire'])
    
    with col4:
        st.header("Vectors management")
        st.json(dico_general['pas'])
              
    return
    
    
  
