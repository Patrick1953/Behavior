# coding: utf-8
class Dico_ajout () :
    def __init__ (self, parametres) :
        
        self.parametres = parametres
        return
    
    def get_dico_ajout (self) :
        try :
            return self.parametres ['dico_ajout']
        except:
            return {}
    def put_ajout (self, ajout) :
        
        dico_ajout = self.get_dico_ajout ()
        if len(dico_ajout) == 0 :
            numero = 0
        else:
            liste_ajout = [nom_ajout for nom_ajout in dico_ajout.keys()]
            liste_ajout.sort()
            dernier_ajout = liste_ajout [len(liste_ajout) - 1]
            
            _ , numero = dernier_ajout.split ('_')
            numero = int(numero) + 1
            
                   
        numero_string = ("0000000000000000000"+str(numero) ) [-10:] 
        name_ajout = "ajout_" + numero_string
        dico_ajout [name_ajout] = ajout
        self.parametres ['dico_ajout'] = dico_ajout
               
        return
    
    def __getitem__ (self,cle) :
        return self.parametres [cle]
    
    def __setitem__ (self,cle, val) :
        self.parametres [cle] = val
        return
    
    def save (self) :
        self.parametres.save()
        return
    
    
    
        
    
    
    
    
   
