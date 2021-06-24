# coding: utf-8
from Gestion_commandes import Gestion_commandes
from Gestion_commandes import Gestion_reponses
  
        


def test_gestion_messages () :
    
    
    
            
    G = Gestion_commandes ()
    G.clean_message()
    
    message = {"m" : "a", }
    G.put_message(message,)
    message = {"m" : "b"}
    G.put_message(message,)
    
    message = G.get_message()
    assert message ['m'] == 'a'
    message = G.get_message()
    
    assert message ['m'] == 'b'
    
    message = G.get_message()
    
    assert message  is None
    
    message = {"m" : "a",}
    G.put_message(message,)
    
    message = {"m" : "b"}
    G.put_message(message,)
    
    G.clean_message()
    message = G.get_message()
    assert message  is None
    
    R = Gestion_reponses ()
    R.clean_message()
    
    message = {"m" : "a",}
    R.put_message(message,)
    
    message = {"m" : "b"}
    R.put_message(message,)
    
    message = R.get_message()
    
    assert message ['m'] == 'a'
    
    message = R.get_message()
    assert message ['m'] == 'b'
    
    message = R.get_message()
    assert message  is None
    
    message = {"m" : "a",}
    R.put_message(message,)
    
    G = Gestion_commandes ()
    message = G.get_message()
    assert message  is None
    
    R = Gestion_reponses ()
    message = R.get_message()
    assert message ['m'] == 'a'
    R.clean_message()
    G.clean_message()

    return

if __name__ == '__main__' :
    test_gestion_messages ()
    print ('fin test_gestion_messages') 
    
  
    
    
