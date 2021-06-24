# coding: utf-8

import json, sys
import streamlit as st







def page3 (mon_instance,dico_general,) :    
    
    
    def display_message (message) :
        st.write (message)
        return
    
    
    
    
    
    
    @st.cache (allow_output_mutation = True)
    def get_liste_choix_quantile () :
        liste = mon_instance.get_liste_travail ('quantile')
        return liste
    
    @st.cache (allow_output_mutation = True)
    def get_liste_choix_date () :
        liste = mon_instance.get_liste_travail ('date')
        return liste
    
 
    st.header ('Enter behavior parameters')
    liste = [nom for nom in dico_general ['position' ].keys() if nom != 'ID' ]
    liste_choix_quantile = get_liste_choix_quantile ()
    liste_choix_date = get_liste_choix_date ()
    
    
     
    for nom in liste :
                
        travail = dico_general ['creation_dictionnaire'] [nom ] 
        liste_parametres = travail ['parametres']
        type_travail = travail ['travail']
        
        if type_travail == 'analyse_mot' :
            if len (liste_parametres) == 0 :
                liste_parametres = [{'type' : 'standard'}]
                dico_general ['creation_dictionnaire'] [nom ] ['parametres'] = liste_parametres
                mon_instance.save_dico_local (dico_general)
            continue  
        
        st.write ('')
        
        st.write ('<span style="color:black;font-size:15px;" >'+'    **'+ nom +'**'+ '</span>', unsafe_allow_html=True)
        
        
        
            
        operation_type = st.radio( "Create or delete : ", ('', 'Create', 'Delete'),  key = nom + "Delete")
        
                
            
        if type_travail == 'quantile' :
            value = st.selectbox("Calculation choice :", liste_choix_quantile, key = nom )
                 
                    
            if value == 'manuel' :
                nom_manuel = st.text_input ('Name delimiter : ' , value = "" , key = nom )
                
                if operation_type == 'Delete' :
                    isExists = None
                    for dico in liste_parametres :
                        if dico ['type'] != 'manuel' :
                            continue
                        if dico ['nom_manuel'] != nom_manuel :
                            continue
                        isExists = dico
                        break
                    if  not isExists is None :
                        liste_parametres.remove (isExists)
                        dico_general ['creation_dictionnaire'] [nom ] ['parametres'] = liste_parametres
                        mon_instance.save_dico_local (dico_general)
                    continue
              
                
                
                separateur = st.number_input ('separateur value =',
                                                      min_value= -100000.0,
                                                      max_value = 100000.0,
                                                      value = 0.0,
                                                      )
                
                if separateur != 0.0 :
                    isNew = True
                    dico_new = {'type' : 'manuel', 'nom_manuel' : nom_manuel,
                                'separateurs' : [separateur,],
                               }
                    
                    liste_parametres_new = []            
                    for dico in liste_parametres :
                                                                   
                        if dico ['type'] != 'manuel' :
                            liste_parametres_new.append (dico)
                            continue
                        if dico ['nom_manuel'] != nom_manuel :
                            liste_parametres_new.append (dico)
                            continue

                        liste_separateurs = dico  ['separateurs']
                        if not separateur in liste_separateurs :
                                liste_separateurs.append (separateur)
                                liste_separateurs.sort()
                        dico ['separateurs'] = liste_separateurs
                        liste_parametres_new.append (dico)
                        isNew = False
                        continue
                    if isNew :
                        liste_parametres_new.append (dico_new)
                    
                        
                    dico_general ['creation_dictionnaire'] [nom ] ['parametres'] = liste_parametres_new
                    mon_instance.save_dico_local (dico_general)
             
                   
            if value != 'manuel' and value != '' :
                if operation_type == 'Delete' :
                    dico =  {'type' : value }
                    if dico in liste_parametres :
                        liste_parametres.remove(dico)
                        mon_instance.save_dico_local (dico_general)
                        dico_general ['creation_dictionnaire'] [nom ] ['parametres'] = liste_parametres
                        mon_instance.save_dico_local (dico_general)
                    
                    
                if operation_type == 'Create' :
                    st.write ('Create numeric ' + nom + ' et ' + value + ' pour ' + str(liste_parametres ) )
                    dico_new = {'type' : value }
                    if not dico_new in liste_parametres :
                        
                        liste_parametres.append (dico_new)
                        dico_general ['creation_dictionnaire'] [nom ] ['parametres'] = liste_parametres
                        mon_instance.save_dico_local (dico_general)
                                
                    
                  
        if type_travail == 'date' :
            value = st.selectbox("Calculation choice  :", liste_choix_date , key = nom)
            if operation_type == 'Delete' and value in liste_parametres and value != '' :
                liste_parametres.remove(value)
                                                   
                dico_general ['creation_dictionnaire'] [nom ] ['parametres'] = liste_parametres
                mon_instance.save_dico_local (dico_general)
                
            if operation_type == 'Create' and not value in liste_parametres and value != '' :
                #st.write ('Create date' + nom + ' et ' + value + ' pour ' + str(liste_parametres ) )
                liste_parametres.append (value)
                dico_general ['creation_dictionnaire'] [nom ] ['parametres'] = liste_parametres
                mon_instance.save_dico_local (dico_general)
            
        
        continue
        

        
    
    
    display_message ('')
    
    
    st.sidebar.header("Behavior measurement management")
    st.sidebar.json(dico_general['creation_dictionnaire'])

    
    
    
               
    return
    
    
  
