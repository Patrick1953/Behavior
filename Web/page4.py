# coding: utf-8

import json, sys
import streamlit as st

from page5 import page5






def page4 (mon_instance, dico_general, ) :    
    
    
    def display_message (message) :
        st.write (message)
        return
    
    
    
    
    
    
    
    
    @st.cache (allow_output_mutation = True)
    def get_liste_choix_pas () :
        liste = mon_instance.get_liste_travail ('pas')
        return liste
    
    
     
    liste_choix_pas = get_liste_choix_pas ()
    st.header ('Enter vector and its size time') 
    
    pas  = st.selectbox("Choice pas :", liste_choix_pas, key = 'pas' )
    
    if pas != '' :
        value = st.number_input('Enter ' + pas + ' vector size',  min_value= 0, max_value= 301,key = ' vector size')
        try :
            dico_pas = dico_general ['pas'] [pas] 
        except:
            pass
            
            
        dico_general ['pas'] [pas] = {'liste_execution'  : [], 'taille_vecteur' : value,}
        mon_instance.save_dico_local (dico_general)
        

    
    liste = [nom for nom in dico_general ['pas' ].keys()  ] 
    for nom_delete in liste :
        choix = st.radio( "Do you want delete " + nom_delete, ('no', 'yes'))
        if choix == 'yes' :
            st.write('<span style="color:red;font-size:15px;" >'+'Always delete ' + nom_delete + '</span>', unsafe_allow_html=True)
            try:
                del dico_general ['pas'] [nom_delete ]
            except:
                pass
            mon_instance.save_dico_local (dico_general)
        
        st.write('' )
        continue
    
    
     
    
        

        
    
    
    display_message ('')
    
    st.sidebar.header("Vectors managemment")
    st.sidebar.json(dico_general ['pas'])
               
    return
    
    
  
