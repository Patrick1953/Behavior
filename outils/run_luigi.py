# coding: utf-8
# Filename: run_luigi.py
import luigi, os
 

                
class Seconde_couche (luigi.Task):
    
    texte = luigi.Parameter(default = "")
 
    def requires(self):
        return []
 
    def output(self):
        self.outPut_file = self.texte + "_appel.txt"
        return luigi.LocalTarget(self.outPut_file)
 
    def run(self):
        
        with self.output().open('w') as f:
            for i in range(1, 11):
                f.write(self.texte  + "{}\n".format(i))
                

                
class Premiere_couche(luigi.Task):
    
    texte = luigi.Parameter (default = "")
 
    def requires(self):
        # nous demandons 2 appels (seconde couche) et on voit que les parametres sont different
        # ce qui permet à chaque appel d'avoir une sortie (par fichier) de nom different,
        # fourni par self.ouput (fichier unique)
        self.nombre_appel = 2
        return [Seconde_couche(texte = self.texte + '_toto'), Seconde_couche(texte =self.texte +'_titi')]
    
    
    def output(self):
        self.output_file = self.texte + "_resultat.txt"
        return luigi.LocalTarget(self.output_file)
    
 
    def run(self):
        
        '''
        il faut que le nom des fichier emis par les appels changent pour chaque appel
        mais on recupere les fichiers dans l'ordre des appels par la fonction self.input [n]
        
        '''
        for i in range(0, self.nombre_appel) :
            with self.input()[0].open() as fin :
                print ('resultat =')
                for line in fin:
                    print (line)    
                        
            with self.output().open("w") as out:
                out.write("fini")
                 
        print ('\nFIN\n')
        return

def detruire (name_file) :
    if os.path.exists(name_file) :
        print (name_file)
        os.remove(name_file)
    else :
        print ("######" + name_file)
    return

    
if __name__ == '__main__':
    luigi.build([Premiere_couche(texte = "alfred"),
                 Premiere_couche(texte = "patrick")],
                 workers=1, local_scheduler = True)
    
    print ('\nDESTRUCTION car sinon luigi considere que le travail est fait\n')
    
    print ("### niveau resultat deuxieme couche d'appel")
    n = "alfred_toto.txt" 
    detruire (n)
    
    n = "alfred_titi.txt"
    detruire (n)    
        
    n = "patrick_toto.txt"
    detruire (n)  
    
    n = "patrick_titi.txt"
    detruire (n)  
    
    print ("\n### niveau appellant")
    
    n = "alfred_resultat.txt"
    detruire (n)
    n = "patrick_resultat.txt"
    detruire (n)
    
    
    
        
    
