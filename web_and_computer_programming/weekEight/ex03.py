import random

#List of words to guess
wordList = ["profets", "alma", "testimony", "jerusalem", "Jews", "children", "family"]

#Word choosed by random method
chosenWord = random.choice(wordList)

#Character spaces 
underScore = "_" * len(chosenWord)

