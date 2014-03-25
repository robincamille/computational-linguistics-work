# -*- coding: utf-8 -*-

# Transform a word & text into Pig Latin
# Outputs all lowercase

import re

def pigWord(word):
    """Converts a single word into Pig Latin"""
    find_cons = re.search('^[bcdfghjklmnpqrstvwxz]*',word)
    slice_loc = len(find_cons.group())
    new_word = word[slice_loc:] + word[:slice_loc] + 'ay'
    return new_word

def pigText(text):
    """Converts a text entirely into Pig Latin. Ignores case & punctuation"""
    new_text = []
    text_split = re.findall(r'[\w]+', text)
    for word in text_split:
        new_text.append(pigWord(word.lower()))
    return ' '.join(new_text)

print 'To transform any text into Pig Latin, type pigText("your text here")'




# Robin Camille Davis
# March 17, 2014
# Methods in Computational Linguistics II (Andrew Rosenberg), Homework 2
