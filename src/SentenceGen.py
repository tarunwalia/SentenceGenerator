'''
Created on Jun 10, 2017

@author: tarun.walia
'''
from random import randint
class SentenceGen:
    inputString = "Tarun bad is walia good and boy"
    def stringGenerator(self):
        stringSplit = self.inputString.split()
        len1 = len(stringSplit)
        print "len1: ", len1
        ranString=''
        for i in range(len1):
            num = randint(0,len1-1)
            print "num :", num
            word= stringSplit[num]
            if ranString.__contains__(word):
                print "if block"
                continue
            else:
                ranString += ''.join(word)+' '
            
                       
        print ranString             

        
if __name__=='__main__':
    sen = SentenceGen()
    sen.stringGenerator()        