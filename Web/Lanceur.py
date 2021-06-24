# coding: utf-8
import multiprocessing




class Lanceur () :
    
    def __init__ (self, job, name = 'travail') :
        
        self.job = multiprocessing.Process(target=job, name=name)
        self.exitcode = None
        
    def start (self,) :
        self.job.start()
        
    def is_alive (self,) :
        try :
            is_alive = self.job.is_alive ()
        except:
            return False
            
        if is_alive :
            return True
        self.job.join ()
        self.exitcode = self.job.exitcode
        return False
    def get_exitcode (self,) :
        return self.exitcode
    
    
        
