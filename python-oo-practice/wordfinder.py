"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    def __init__(self, file):
        """sees how many words read from doc"""
        self.file = file
        self.words = self.list_of_words()
        print(f"{len(self.words)} words read")

    def list_of_words(self):
        """isolates words line by line from doc"""
        dict = open(self.file)
        return [line.strip() for line in dict] 
    
    def random(self):
        """return random word from list"""
        return choice(self.words)
    
    def __repr__(self):
        return f"<File name={self.file}>"
    

class RandomWordFinder(WordFinder):
    def list_of_words(self):
        dict = open(self.file)
        return [line.strip() for line in dict if not line.startswith("#")] 



            


