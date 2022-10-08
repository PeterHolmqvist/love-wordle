#Imports
import random
import sys
from termcolor import colored
from list import word_list

#for loop to iterate words of words_list and return lowercase
for i in range(len(word_list)):
    word_list[i] = word_list[i].lower()


# function that chooses random word from the words list
words = word_list
word = random.choice(words)
print(word)
