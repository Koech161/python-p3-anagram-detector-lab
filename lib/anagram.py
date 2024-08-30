# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word

    def match(self,word_list):
        sorted_word = ''.join(sorted(self.word))  
        anagrams =[word for word in word_list if ''.join(sorted(word)) == sorted_word]   
        return anagrams

listen = Anagram('listen')
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
