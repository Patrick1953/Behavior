# coding: utf-8
import os, time

class LockTimeError(Exception): pass

class Lock () :
    
    def __init__ (self, pathLock, time_out) :
        
        self.time_out = time_out
        self.pathLock = pathLock
        
        
    def acquire (self, ) :
        nombre = 0
        while (os.path.exists (self.pathLock)) :
            time.sleep (1)
            nombre += 1
            if nombre > self.time_out :
                self.release()
                raise LockTimeError ()
            continue
        
        with open(self.pathLock, 'w') as f :
            f.close ()
        return
    
    def release (self,):
        try :
            os.remove (self.pathLock)
        except:
            pass
        return
    
    def is_locked (self):
        
        if not os.path.exists(self.pathLock):
            return False
        else :
            return True
