# -*- coding: utf-8 -*-

# finds all words in Moby Dick ending in -ly in freq distribution

#from nltk.book import *
import re

text1 = "your text here" #<----- change this or else uncomment
                         # line 5 to use Moby Dick

outfile = open("homework2_1f_output.txt","w")

#find all the words in given text that end in -ly
ly_words = [w.lower() for w in text1 if re.search('.*ly$',w)]

#put them in frequency distribution 
ly_words_freq = FreqDist(ly_words)
top_ly_words = ly_words_freq.keys()

#write the top 5 to an output file
for word in top_ly_words[:5]:
    ind = top_ly_words.index(word) + 1
    outfile.write(str(ind) + ' ' + word + '\n')

outfile.close()

print "Your file has been written to %s" %(outfile)


# Robin Camille Davis
# March 17, 2014
# Methods II
# Homework 2
