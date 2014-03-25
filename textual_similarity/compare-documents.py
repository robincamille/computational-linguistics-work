# Robin Camille Davis
# February 28, 2014
# Methods II
# Homework 1

# Section B: Open-ended programming problem

# This script compares one text to another text

from nltk.book import *
from math import log
import nltk.data
sentsplitter = nltk.data.load('tokenizers/punkt/english.pickle')


#
# Following compares word frequency distributions and returns
# the average difference in word frequencies and number of words
# not shared for sum of all words in both texts.
#

def getfreq(text):
    """Returns frequency distribution of a text, from NLTK"""
    fd = FreqDist(text)
    return fd

def lowertext(text):
    """Returns a text in all lowercase"""
    lowtext = []
    for w in text:
        w = w.lower()
        lowtext.append(w) 
    return lowtext

def comparefreq(textA, textB):
    """Returns average difference in word frequencies and number of words per text, for two texs"""
    textA = lowertext(textA)
    textB = lowertext(textB)
    
    fdA = getfreq(textA)
    fdB = getfreq(textB)

    freqdiffs = []
    notshared = [] #not used in final function, but left it in: words in A not B, or B not A

    for s in fdA:
        if s in fdB:
            freqdiff = abs((fdA.freq(s) - (fdB.freq(s))))
            #w.write(s + '\t' + str(freqdiff) + '\n')
            freqdiffs.append(freqdiff)
        else:
            notshared.append(s)

    for s in fdB:
        if s not in fdA:
            notshared.append(s)

    notshareddec = len(notshared) / float(len(textA) + len(textB))
        #number of words not shared, as a decimal

    freqsum = 0
    for i in freqdiffs:
        freqsum = freqsum + i
    freqavg = freqsum / len(freqdiffs) #average difference of frequencies

    return freqavg
    

#
# Following compares average word length.
#

def avgwordlength(text):
    """Returns average word length in a text (float)"""
    lowtext = lowertext(text)  
    textfreq = getfreq(lowtext)
    words = textfreq.keys() #dedupe
    totalchars = 0
    for s in words: #may include some punctuation
        totalchars = totalchars + len(s)
    textlength = len(words)
    return totalchars / float(textlength)

def compareavgwl(textA, textB):
    """Returns difference in average word length in a text"""
    wlA = avgwordlength(textA)
    wlB = avgwordlength(textB)
    return abs(wlA - wlB)
    
#
# Following compares average sentence length.
#

def avgsentlength(text):
    """Returns average sentence length in a text, in chars (float)"""
    textstring = ' '.join(text)
    sents = sentsplitter.tokenize(textstring)
    totalsentlength = 0
    for s in sents:
        totalsentlength = totalsentlength + len(s) #length in chars
    numsents = len(sents)
    return totalsentlength / float(numsents)

def compareavgsl(textA, textB):
    """Returns difference in average sentence length in a text"""
    slA = avgsentlength(textA)
    slB = avgsentlength(textB)
    return abs(slA - slB)

#
# Following combines word frequency difference, average word length difference,
# and average sentence length difference into one similarity score.
# A pair of texts that are exactly the same has a score of zero.
#

def scoresim(textA, textB):
    wf = comparefreq(textA, textB) * 10000 #heavy weight given to word freq
    wl = compareavgwl(textA, textB)
    slraw = compareavgsl(textA, textB)
    sl = log(slraw, 10) #decrease weight (log base 10)
    score = wf + wl + sl
    return score

#
# Find similarity scores between texts
#

textset = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
pairs = []

table = open('table.csv','w')
table.write('Text1,Text2,Score\n')

for t in textset:
    for t2 in textset:
        if t is not t2:
            if [t,t2] not in pairs: #dedupe
                if [t2,t] not in pairs:
                    pairs.append([t,t2])
                    print t, t2
                    table.write(str(t) + ',' + str(t2) + ',' + str(scoresim(t,t2)) + '\n')

table.close()

print 'Finished file: ', table
