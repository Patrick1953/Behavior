# coding: utf-8
import json, sys
import streamlit as st

path = "../outils"
if path not in sys.path : 
    sys.path.append (path)






def page3 (Interface, dico, isCall = True) :    
    if not isCall :
        st.set_page_config(
                            page_title="Time parameters",
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
        
    
    
    

        

    @st.cache (allow_output_mutation = True)
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
    def get_all_petit_nom (Interface) :
        liste = Interface.get_liste_environnement ()
        liste.insert(0, '')
        return liste
    
    @st.cache (allow_output_mutation = True)
    def save_parametres ( dico_out, Interface) :
        I.put_dico_evenements (dico_evenements)
        return 
    
    
        
    
    
    dico_position, dico_type, dico_dictionnaire, dico_pas, taille = load_dico(dico)
    liste_petit_nom = get_all_petit_nom()
    image = get_image()
    
    
    """
    agree4 = st.checkbox('Create or Update systeme Parameters')
    if agree4 :
        
        dico_out = {}
        dico_out ['position'] = dico_position
        dico_out ['type']  = dico_type
        dico_out ['creation_dictionnaire'] = dico_dictionnaire
        dico_out ['pas'] = dico_pas
        save_dico (dico_out)
        
        page4 (dico_out,)
        st.stop
    """

        
        
        
        
    agree5 = st.checkbox('Stop & Backup', key = 'Stop & Backup')
    if agree5  :
        dico_out = {}
        dico_out ['position'] = dico_position
        dico_out ['type']  = dico_type
        dico_out ['creation_dictionnaire'] = dico_dictionnaire
        dico_out ['pas'] = dico_pas
        save_dico (dico_out)
        st.stop()

    agree6 = st.checkbox('Stop & no Backup', key = 'Stop & no Backup')
    if agree6:
        st.warning('Stop & no Backup done')
        st.stop()
        
     

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
    st.sidebar.image(image)
    

    st.sidebar.header ('Time size for vector')

    liste = ['','half_day', 'day', 'week', '2 weeks',  'month', '3 months','year',]
    
    value = st.sidebar.selectbox("Time size ? ", liste,)
    if value != "" and not value in dico_pas :
        dico_pas [value] = {}
        
    value = st.sidebar.selectbox("Delete time size ? ", liste,)
    if value != "" and  value in dico_pas :
        del dico_pas [value]
    

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
    page3 ()



