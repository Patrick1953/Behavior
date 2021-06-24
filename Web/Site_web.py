# coding: utf-8
import subprocess

from Interface_parametres import Interface_parametres

class Site_web () :
    
    def __init__ (self,) :
        
        self.process = None
        
        return
    
    def lancement_site (self, bashCommand = "streamlit run page0.py") :
        self.process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        return
    
    def arret_site (self,) :
        if self.process is None :
            return
        self.process.terminate ()
        return
    
    
    
    
