# coding: utf-8
import json, random
import streamlit as st
from Saisie_pas import page3


def page2 (dico, isCall = True) :
    if not isCall :
        st.set_page_config(
                            page_title="Execution parameters",
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
    def dico1 (dico) :
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
        return r1, r2, r3, r4
         

    
    @st.cache (allow_output_mutation = True)
    def save_dico ( dico, nameFile = "./Saisie.json",):
        data =  json.dumps (dico)
        f = open (nameFile, 'w')
        f.write (data)
        
        return
        
   


    def display_message (message) :
        st.write (message)
        return


    @st.cache (allow_output_mutation = True)
    def get_image (path = "./image/4x/Fichier 1@4x.png" ) :
        f = open (path, "rb" )
        image = f.read()
        f.close()
        return image



    dico_position, dico_type, dico_dictionnaire, dico_pas = dico1 ( dico) 
    image = get_image()
    
    
    
    

    agree2 = st.checkbox('Finish & Backup' , key = 'Finish & Backup')
    if agree2:
        
        st.warning('The systeme saves parameters on local disk.')
        dico_out = {}
        dico_out ['position'] = dico_position
        dico_out ['type']  = dico_type
        dico_out ['creation_dictionnaire'] = dico_dictionnaire
        dico_out ['pas'] = dico_pas
        save_dico (dico_out)
        page3(dico_out)
        st.stop()

    agree3 = st.checkbox('Finish & no backup', key = 'Finish & no backup')
    if agree3:
        dico_out = {}
        dico_out ['position'] = dico_position
        dico_out ['type']  = dico_type
        dico_out ['creation_dictionnaire'] = dico_dictionnaire
        dico_out ['pas'] = dico_pas
        page3 (dico_out)
        st.stop()


    st.title ('Parameters')
    st.sidebar.image(image)
    st.sidebar.header ('Execution parameters' )




    dicoAnalyse = {'date' : 'analyse_date','string' :'analyse_mot', 'numeric' : 'quantile'}
    for nomV in dico_type.keys():

        try:
            analyse = dico_type [nomV]  ['type']
        except:
            analyse = None
        if analyse is None :
            continue

        analyse = dicoAnalyse [analyse]
        try :
            r = dico_dictionnaire[nomV]
        except:
            r = {}
            r ['travail'] = analyse
            dico_dictionnaire[nomV] = r
        continue







    
    index = 0
    for nomV in dico_type.keys():
        if nomV == 'ID' :
            continue
        typeV = dico_dictionnaire[nomV] ['travail']
        if typeV == 'quantile' :
            liste1 = ['', 'quartile', 'quintile', 'decile', 'vingtile', 'cinquantile', 'centile','manual', 'CLEAR' ]
            value = st.sidebar.selectbox(nomV + " ? ", liste1, key = nomV)
            
            if value == 'CLEAR' :
                try :
                    resultat = dico_dictionnaire[nomV]
                except:
                    resultat = {}
                try:
                    l = resultat['parametres']
                except:
                    l = []
                l = []
                resultat['parametres'] = l
                dico_dictionnaire[nomV]
                continue
            
                
           
                
            if value == 'manual':
                nom_manuel = st.sidebar.text_input ('separation name =', value = "", )
                if not (nom_manuel == "") :
                    try :
                        resultat = dico_dictionnaire[nomV]
                    except:
                        resultat = {}
                    try:
                        l = resultat['parametres']
                    except:
                        l = []
                    isIn = False
                    i = 0
                    for resultat_old in l:
                        if not resultat_old ['type'] == 'manuel' :
                            i += 1
                            continue
                        if not 'nom_manuel'  in resultat_old :
                            i += 1
                            continue
                        if resultat_old ['nom_manuel'] == nom_manuel :
                            isIn = True
                            break
                        i += 1
                        continue
                    
                    if isIn :
                        resultat_manuel = l.pop(i)
                    else:
                        resultat_manuel = {'type': 'manuel', 'nom_manuel' : nom_manuel }
                    
                    separateur = st.sidebar.number_input ('separateur value =',
                                                      min_value= -100000.0,
                                                      max_value = 100000.0,
                                                      value = 0.0,
                                                      )
                    if separateur != 0.0:
                        try:
                            liste_separateurs = resultat_manuel  ['separateurs']
                        except:
                            liste_separateurs = []
                            
                        if not separateur in liste_separateurs :
                            liste_separateurs.append (separateur)
                            liste_separateurs.sort()
                        resultat_manuel  ['separateurs'] = liste_separateurs
                    l.append(resultat_manuel)
                    resultat['parametres'] = l
              
                continue
            
            if value == "" :
                continue
            
                
            try :
                resultat = dico_dictionnaire[nomV]
            except:
                resultat = {}
            try:
                l = resultat['parametres']
            except:
                l = []
            
            if value == 'CLEAR':
                l = []
                
            isIn = False
            for resultat_old in l:
                if resultat_old ['type'] == value :
                    isIn = True
                    break
                continue
                    
            if not isIn :
                l.append({'type': value})
            else:
                continue
            
            resultat['parametres'] = l
            dico_dictionnaire[nomV] = resultat
            continue
        
        ### pas quantile on réalise une saisie basique du type standard ou autre.....
                  
        elif typeV == 'analyse_date' :
            liste2 = ['', 'half_day', 'day', 'week', 'month', 'year', 'holiday', 'CLEAR']
            value = st.sidebar.selectbox(nomV + " ? ", liste2, key = nomV)
        else:
            liste3 = ['', 'standard', 'special_word', 'separator_string','CLEAR']
            value = st.sidebar.selectbox(nomV + " ? ", liste3, key = nomV)
            


        if value != '':
            try :
                r = dico_dictionnaire[nomV]
            except:
                r = {}
            try:
                l = r['parametres']
            except:
                l = []
                
            if value == 'CLEAR' :
                l = []
                r['parametres'] = l
                dico_dictionnaire[nomV] = r
                value = ''
                continue
            
            
            isIn = False
            for resultat_old in l:
                if resultat_old ['type'] == value :
                    isIn = True
                    break
                continue
                    
            if not isIn :
                l.append({'type': value})
            r['parametres'] = l
            dico_dictionnaire[nomV] = r


        value = ""
        continue


    st.sidebar.write ('Choose variable for execution delete ')
    option = st.sidebar.text_input('What would you like to get out from parameters ?   Warning always running (have to be blank/clear) ', value = "", key = 'execution')

    if option != '' and option != 'ID' and option != 'date_event' :
        if option in dico_dictionnaire :
            del dico_dictionnaire [option]
        option = ''


    display_message ("") # on fixe la position du message du warning


    col1, col2, col3  = st.beta_columns(3)

    with col1:
        st.header("Execution parameters")
        st.json(dico_dictionnaire)

    with col2:
        st.header("Variable type")
        st.json(dico_type)
    with col3:
        st.header("Variable position")
        st.json(dico_position)
        
    return

    
if __name__ == "__main__":
    
    # execute only if run as a script
    f = open("./Saisie.json" , 'r')
    data = f.read()
    f.close()
    dico = json.loads(data)
    page2 (dico, isCall = False)
    
    
    
    

    
    



