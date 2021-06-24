# coding: utf-8
# coding: utf-8
import json, sys
import streamlit as st

from execution1 import execution1


path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from Interface_executions import Interface_executions


st.set_page_config(
                        page_title="Variables parameters",
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



def execution0 (mon_instance, arg) :
    
    

    
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
    def get_liste_environnement ():
        liste = mon_instance.get_liste_environnements ()
        return liste
    
    
    
    
    
    
    
       
    image = get_image()    
    
    st.sidebar.image(image)
    st.title ('Execution management') 
    
    liste = get_liste_environnement ()
    value = st.sidebar.selectbox("Environment choice :", liste,)
    if value != '' :
        arg = {'nom_environnement' : value }
          
    return arg
   
    
    

    

# execute only if run as a script
@st.cache (allow_output_mutation = True)  
def _cached_instanciate_interface():
    mon_instance = Interface_executions ()
    return mon_instance

@st.cache (allow_output_mutation = True)  
def _cached_instanciate_arg():
    dico = {}
    return dico

mon_instance = _cached_instanciate_interface ()
liste = mon_instance.get_liste_fichiers ('test')
st.write (liste)
arg = _cached_instanciate_arg ()
arg = execution0 (mon_instance, arg)


with st.beta_expander('ALIMENTATION'):
    arg = execution1 (mon_instance, arg)
'''
with st.beta_expander('Entry zone format'):
    dico = mon_instance.get_dico_local ()
    page2 (mon_instance, dico )
with st.beta_expander('Behavior parameters'):
    dico = mon_instance.get_dico_local ()
    page3 (mon_instance, dico )
with st.beta_expander('Vector parameters'):
    dico = mon_instance.get_dico_local ()
    page4 (mon_instance, dico )
with st.beta_expander('Save parameters'):
    dico = mon_instance.get_dico_local ()
    page5 (mon_instance, dico )
'''


