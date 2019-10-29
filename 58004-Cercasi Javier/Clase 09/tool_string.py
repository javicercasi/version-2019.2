
import string
class ToolString():

    def is_palindromo(self,frase):
        c=0
        self.frase= frase.replace(" ", "") 
        for i in range (len(self.frase)):

            if self.frase[i] == self.frase[-i-1]:
                c+=1    
        return(len(self.frase)== c)
    
     
    def is_upper(self, palabra):
        c=0
        self.palabra=palabra.replace(" ", "") 
        for m in range(len(self.palabra)):
        
            if self.palabra[m].isupper():
                c+=1
     
        return(len(self.palabra)== c)
    




       
        

