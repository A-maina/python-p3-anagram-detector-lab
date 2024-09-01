# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word
        
    def match (self,words_ist ):
        sorted_word = sorted(self.word)
        return [word for word in words_ist if sorted(word) == sorted_word]
        
    
    