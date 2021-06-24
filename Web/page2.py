# coding: utf-8

import json, sys
import streamlit as st






def page2 (mon_instance,dico,) :    
    
    @st.cache (allow_output_mutation = True,)
    def display_message (message) :
        st.write (message)
        return
    
    
    
    
    
    @st.cache (allow_output_mutation = True)
    def type_to_travail (data_type) :
        return mon_instance.type_to_travail (data_type)
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    st.header ('Enter zone format')

    liste = [nom for nom in dico ['position' ].keys() if nom != 'ID'  ]
     
    for nom in liste :
        
        st.write ('')
        
        st.write ('<span style="color:black;font-size:15px;" >'+'    **'+ nom +'**'+ '</span>', unsafe_allow_html=True)
        
        if nom != 'date_evenement' :
            choix_type = st.radio( "Choose type :", ('', 'string', 'date', 'numeric'), key = 'type'+ nom )
            if choix_type != '' :
                dico ['type'] [nom] ['type'] = choix_type
                dico ['creation_dictionnaire'] [nom] ['travail']  = type_to_travail (choix_type)
                dico ['creation_dictionnaire'] [nom] ['parametres']  = []
                if choix_type != 'date' :
                    st.write ('Format  :standard')
                    dico ['type'] [nom] ['format'] = 'standard'
                    mon_instance.save_dico_local (dico)
                if choix_type == 'date' :
                    choix_format = st.radio( "Choose entry format :", ('','standard', 'no standard', ), key = 'format'+nom )
                    if choix_format == 'standard' :
                        dico ['type'] [nom] ['format'] = choix_format
                        st.write ('Format :standard')
                        mon_instance.save_dico_local (dico)

                    if choix_format == 'no standard':
                        format_date = st.text_input ('Enter date format   ', value = "", key = 'format' + nom )
                        if format_date !=  '' and not mon_instance.is_good_date (format_date) :
                            st.write ('Wrong date format :' + format_date)


                        if  format_date !=  '' and mon_instance.is_good_date (format_date) :
                            dico ['type'] [nom] ['format'] = format_date
                            st.write ('Format  :' + format_date)
                            mon_instance.save_dico_local(dico)
                    
        
        
            
        
            
        
            
                   
        if nom == 'date_evenement' :
            choix_format = st.radio( "Choose entry format :", ('','standard', 'no standard', ), key = 'format'+nom )
            if choix_format == 'standard' :
                dico ['type'] [nom] ['format'] = choix_format
                st.write ('Format :standard')
                mon_instance.save_dico_local (dico)
                
            if choix_format == 'no standard':
                format_date = st.text_input ('Enter date format   ', value = "", key = 'format' + nom )
                if format_date !=  '' and not mon_instance.is_good_date (format_date) :
                    st.write ('Wrong date format :' + format_date)
                    
                    
                if  format_date !=  '' and mon_instance.is_good_date (format_date) :
                    dico ['type'] [nom] ['format'] = format_date
                    st.write ('Format  :' + format_date)
                    mon_instance.save_dico_local(dico)
            
                
        
        
            
         
            
            
                    
                 
        
        st.write('' )
        continue
        

        
    
    
    display_message ('')
    
    st.sidebar.header("Type and format zone")
    st.sidebar.json(dico ['type'])

            
    return
    
    
  
