# coding: utf-8
import json
import streamlit as st
from Test import Test
#from Saisie_execution import page2

def page1 (mon_instance) :    
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



    @st.cache (allow_output_mutation = True)
    def dico (nameFile = "./Saisie.json", ):
        
        
        try :
            f = open (nameFile, 'r')
        except:
            r1 =  {'ID' : None, 'date_event' : None, }
            r2 = {'ID' : {'type' : 'string',
                             'format':'standard'},

                     'date_event' : {'type' : 'date',
                     'format' : 'standard'},
                     }
            r3 = {'ID' : {'travail' : None, 'parametres' : []},
                     'date_event' : {'travail' : 'analyse_date', 'parametres' : [] },
                    }

            try :
                r4 = dico ['pas']
            except:
                r4 = {}    
        

            return r1, r2, r3, r4
        
        data = f.read()
        f.close()
        dico = json.loads(data)

        r1 = dico ['position']
        r2 = dico ['type']

        try :
            r3 = dico ['creation_dictionnaire']
        except:
            r3 = {'ID' : {'travail' : None, 'parametres'  :  []},
                   'date_event' : {'travail' : 'analyse_date' , 'parametres' : [] },
                    }
            
        try :
            r4 = dico ['pas']
        except:
            r4 = {}    
        
        
        return r1, r2, r3, r4
    
    @st.cache (allow_output_mutation = True)
    def save_dico ( dico, nameFile = "./Saisie.json"):
        
        data =  json.dumps (dico)
        f = open (nameFile, 'w')
        f.write (data)
        if len(dico ['pas']) == 0 :
            return False
        return True


    def display_message (message) :
        st.write (message)
        return

    @st.cache (allow_output_mutation = True)
    def test_position (dico) :
        isOK = True
        message = "Existing position for"
        memoire = {}
        for nomV, position in dico.items() :
            if position is None :
                continue
            if str(position) in memoire :
                message += " " + nomV + ","
                isOK = False
                continue
            memoire [str(position)] = None
            continue
        if isOK :
            return ''
        message = message [:-1]
        return message

    @st.cache (allow_output_mutation = True)    
    def test_name_variable (dico) :
        isOK = True
        memoire = {}
        message = "Existing name for"
        for nom in dico.keys():
            if nom in memoire :
                message += " " + nom + ","
                isOK = False
                continue
            memoire [nom] = None
            continue
        if isOK :
            
            message = ""
            return message
        return message [:-1]

    @st.cache (allow_output_mutation = True)
    def test_value_variable (dico) :
        isOK = True
        message = "Curious name about"
        for nom in dico.keys():
            try :
                x = float(nom)
                message += " " + nom + ","
                isOK = False
            except:
                pass
            continue
        if isOK :
            return ""
        return message [:-1]

    @st.cache (allow_output_mutation = True)
    def get_image (path = "./image/4x/Fichier 1@4x.png" ) :
        f = open (path, "rb" )
        image = f.read()
        f.close()
        return image
    
    
    
    
    
    
    
    
    
                         
        
        
    
  
        






    dico_position, dico_type, dico_dictionnaire, dico_pas = dico() # la valeur permet de ne pas relancer la fonction sauf pour ecriture (n!=0)
    image = get_image()
    
    

    agree = st.checkbox('Next & Backup', key ='Next & Backup' )
    if agree:
        dico_out = {}
        dico_out ['position'] = dico_position
        dico_out ['type']  = dico_type
        dico_out ['creation_dictionnaire'] = dico_dictionnaire
        dico_out ['pas'] = dico_pas
        #st.warning('The systeme saves parameters on local disk.')
        isOK = save_dico ( dico_out )
        if not isOK :
            st.warning('dico_pas disparu')
        #page2(dico_out)
        
        st.stop()

    agree1 = st.checkbox('Next & no Backup',key = 'Next & no Backup')
    if agree1:
        #st.warning('The systeme stop.')
        dico_out = {}
        dico_out ['position'] = dico_position
        dico_out ['type']  = dico_type
        dico_out ['creation_dictionnaire'] = dico_dictionnaire
        dico_out ['pas'] = dico_pas
        #page2(dico_out)
        st.stop()


    st.title ('Parameters')
    st.sidebar.image(image)
    
    if len(dico_pas) == 0:
        st.warning ('pas disparu')
        
    
    
    

    st.sidebar.header ('Variable management')
    nom  = st.sidebar.text_input ('Enter new name ? Warning always running (have to be blank/clear after variable creation) ', value = "", )
    
    
    
    
    if nom != "" :
        dico_position [nom] = None
        nom = ""
        message = test_name_variable (dico_position)
        if message != "" :
            display_message (message)

        message = test_value_variable (dico_position)
        if message != "" :
            display_message (message)
        
    
        

    option = st.sidebar.text_input('What would you like to get out from parameters ?   Warning always running (have to be blank/clear) ', value = "",)
    if option != '' and option != 'ID' and option != 'date_event' :
        if option in dico_position :
            del dico_position [option]

        if option in dico_type :
            del dico_type [option]
        option = ''

    st.sidebar.write ('Enter variable position (integer) ')
    for nomV in dico_position.keys():
        value = st.sidebar.text_input (nomV , value = "" , )
        if value != "" :
            try :
                position = int(value)
                dico_position [nomV] = position

            except Exception as e:
                display_message ("Curious value for position in "+ str(value) )
                pass
            value = ""


        continue



    message = test_position (dico_position)
    if message != "" :
        display_message (message  )



    st.sidebar.write ('Choose variable  type')
    liste = ['', 'string', 'date', 'numeric']
    for nomV in dico_position.keys():
        if nomV == 'ID' or nomV == 'date_event':
            continue

        value = st.sidebar.selectbox(nomV + " ? ", liste,)
        if value != '':
            try :
                r = dico_type [nomV]
            except:

                r = {}
            try:
                r ['type'] = value
                dico_type [nomV] = r
            except:
                display_message ("erreur #"+str(dico_type)+ ' '+ str(type(dico_type)) )

        value = ""
        continue


    st.sidebar.write ('Choose variable  format')
    liste = ['', 'standard', 'no standard',]
    for nomV in dico_position.keys():

        if nomV == 'ID'  :
            continue

        value = st.sidebar.selectbox(nomV + " ? ", liste,)
        if value != '':
            try :
                r = dico_type [nomV]
            except:
                r = {}

            try:
                r ['format'] = value
                dico_type [nomV] = r
            except:
                display_message ("erreur #"+str(dico_type)+ ' '+ str(type(dico_type))+ ' r='+str(r) )

        value = ""
        continue

    display_message ("") # on fixe la position du message du warning


    col1, col2 = st.beta_columns(2)
    with col1:
        st.header("Variables")
        st.json(dico_position)

    with col2:
        st.header("Variable type")
        st.json(dico_type)
        
    return
    

if __name__ == "__main__":
    # execute only if run as a script
    T = Test ()
    page1 (T)



