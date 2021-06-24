# coding: utf-8
# coding: utf-8
import json, sys
import streamlit as st

from page1 import page1
from page2 import page2
from page3 import page3
from page4 import page4
from page5 import page5

path = "../outils"
if path not in sys.path :
    sys.path.append (path)
from Interface_parametres import Interface_parametres


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



def page0 (mon_instance,dico) :
    
    

    
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
    
    
    
    @st.cache (allow_output_mutation = True)
    def get_dico_evenements (nom_environnement):
        dico = mon_instance.get_dico_evenements (nom_environnement)
        return dico
       
    image = get_image()    
    
    st.sidebar.image(image)
    st.title ('Parameters management') 
    
    liste = get_liste_environnement ()
    value = st.sidebar.selectbox("Environment choice :", liste,)
    if value != '' :
        dico = get_dico_evenements (value)
    
    
    
    
        
    return
   
    
    
@st.cache (allow_output_mutation = True)  
def _cached_instanciate_interface():
    mon_instance = Interface_parametres ()
    return mon_instance
    
    

# execute only if run as a script
mon_instance = _cached_instanciate_interface()
dico = mon_instance.get_dico_local ()
page0 (mon_instance, dico)


with st.beta_expander('Create entry zone'):
    dico = mon_instance.get_dico_local ()
    page1 (mon_instance, dico)
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
