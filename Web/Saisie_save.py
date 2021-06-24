# coding: utf-8
import json
import streamlit as st
import sys
path = "../outils"
if path not in sys.path : 
    sys.path.append (path)

from validationPath import validationPath
from Parametres  import Gestion_petit_nom_evenements

def page4 (dico, isCall = True) :    
    if not isCall :
        st.set_page_config(
                            page_title="Save parameters",
                            page_icon="🧊",
                            layout="wide",
                            initial_sidebar_state="expanded",
                            )

        hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>

        """

        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        
        
    
    


    @st.cache (allow_output_mutation = True)
    def save_dico ( dico, nameFile = "./Saisie.json") :
        data = json.dumps (dico)
        f = open (nameFile, 'w')
        f.write (data)
        f.close()
        return 
    
    @st.cache (allow_output_mutation = True)
    def load_dico ( dico, nameFile = "./Saisie.json") :
        r2 = dico ['type']
        r1 = dico ['position']
        try :
            r3 = dico ['creation_dictionnaire']
        except:
            r3 = {'ID' : {'travail' : None, 'parametres' : []},
                     'date_event' : {'travail' : None, 'parametres' : [] },
                    }
        
        try :
            r4 = dico ['pas']
        except:
            r4 = {}
        
        taille = str(dico)  
        return r1, r2, r3, r4, taille
        
    
    
    

        

    
    def display_message (message) :
        st.write (message)
        return

    
    

    @st.cache (allow_output_mutation = True)
    def get_image (path = "./image/4x/Fichier 1@4x.png" ) :
        f = open (path, "rb" )
        image = f.read()
        f.close()
        return image
    
    @st.cache (allow_output_mutation = True)
    def get_all_petit_nom (path = '../data/test' ) :
        G =  Gestion_petit_nom_evenements (path)
        liste = G.get_all_petit_nom()
        liste.insert(0, '')
        return liste
    
    @st.cache (allow_output_mutation = True)
    def save_parametres (nom, dico_out, path = '../data/test' ) :
        G =  Gestion_petit_nom_evenements (path)
        G.save_parametres (nom, dico)
        return 
        
               
    
    
        

    
    dico_position, dico_type, dico_dictionnaire, dico_pas, taille = load_dico(dico)
    liste_petit_nom = get_all_petit_nom()
    
    image = get_image()
    
    agree6 = st.checkbox('Stop & Backup', key = 'Stop & Backup6')
    if agree6  :
        dico_out = {}
        dico_out ['position'] = dico_position
        dico_out ['type']  = dico_type
        dico_out ['creation_dictionnaire'] = dico_dictionnaire
        dico_out ['pas'] = dico_pas
        save_dico (dico_out)
        st.stop()

    agree7 = st.checkbox('Stop & no Backup', key = 'Stop & no Backup7')
    if agree7:
        st.warning('End & no Backup done')
        st.stop()


    st.title ('Parameters (all)')
    
    
    #st.sidebar.image(image)
    #st.sidebar.header ("Parameters management")
    
    
    liste_question = ['', 'Creation',  'Update' ]
    question  = st.selectbox("What do you want create new paramemeters or update an existing parameters ? ", liste_question,)

    if question != '' and question == 'Creation' :
        nom_name  = st.text_input ('Enter new name ', value = "", max_chars= 10, key = "new_name")
        if nom_name != '' and not nom_name in liste_petit_nom :
            dico_out = {}
            dico_out ['position'] = dico_position
            dico_out ['type']  = dico_type
            dico_out ['creation_dictionnaire'] = dico_dictionnaire
            dico_out ['pas'] = dico_pas
            save_parametres (nom_name, dico_out)
            st.warning('Creation of '+ nom_name + ' systeme parameters')
            st.stop()
        nom_name = ''

    if question != '' and question == 'Update' :
        petit_nom = st.selectbox("Choose existing name ? ", liste_petit_nom,)
        if petit_nom != '' :
            dico_out = {}
            dico_out ['position'] = dico_position
            dico_out ['type']  = dico_type
            dico_out ['creation_dictionnaire'] = dico_dictionnaire
            dico_out ['pas'] = dico_pas
            save_dico (dico_out)
            save_parametres (petit_nom, dico_out)
            st.warning('Update '+ petit_nom + ' systeme parameters')
            st.stop()
            
    
               
        
    
    
       
        
    
    st.title ('Parameters (all)')

    col1, col2, col3, col4 = st.beta_columns(4)
    with col1:
        st.header("Vector time size")
        st.json(dico_pas)

    with col2 :
        st.header("Execution parameters")
        st.json(dico_dictionnaire)

    with col3 :
        st.header("Variable type")
        st.json(dico_type)
    with col4 :
        st.header("Variable position")
        st.json(dico_position)
        
    return
    

if __name__ == "__main__":
    # execute only if run as a script
    page4 ()



