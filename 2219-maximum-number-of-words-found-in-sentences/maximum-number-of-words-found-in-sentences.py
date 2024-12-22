class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length = 0
        for i in sentences:
            a = i.split()
            newlen = len(a)   
            if(newlen>length):
                length = newlen    
                         
        return length
            

        
        