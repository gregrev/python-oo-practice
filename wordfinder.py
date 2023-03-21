"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:

    def __init__(self, path):
        # open the path whichi s words.txt
        file = open(path)
        # parse the file to get individual words list
        self.words = self.parse(file)
        
    def parse(self, file):
        # slpit and remove extra white space in that files
        return [word.strip() for word in file]
    
    def random(self):
        # return random words from the file
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    def parse(self, file):
        # slpit and remove extra white space in that files
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]

