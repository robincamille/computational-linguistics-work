# -*- coding: utf-8 -*-

# finds words in a text with ≥4 consonants
# uses a list comprehension
# outputs a text file with a list of the words

#from nltk.corpus import words
import re

text = "your text here" # <--------- change to the text you want to run this on, or
                        # uncomment line 7 and change to text = "words.words()"s
outfile = open("output.txt","w")

#list comprehension finds 4 consonants in a row within a word
#useful: http://www.nltk.org/book/ch03.html
#treats y as consonant

wordsWith4Consonants = [w for w in text if re.search('[bcdfghjklmnpqrstvwxz]{4}', w)]

for word in wordsWith4Consonants:
    outfile.write(word)
    outfile.write("\n")

outfile.close()
print "Your file has been written to %s" %(outfile)



# Robin Camille Davis
# March 17, 2014
# Methods II
# Homework 2
