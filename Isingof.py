#!/usr/bin/env python
from __future__ import division
"I sing of"
__author__ = "Erik Stayton"
__copyright__ = "Copyright 2014 Erik Stayton"
__license__ = "CC-BY-SA"
__version__ = "0.0.1"
__status__ = 'Development'

import random;
import sys;
import os;
import nltk;
import string;
from nltk.corpus import wordnet as wn;

def join(array1,array2): #join two arrays and return the result
    output = array1
    for item in array2:
        output.append(item)
    return output

def captitle(word): #capitalize the first letter of a word
    return word[0].title()+word[1:]

def replacer(phrase):
    newphrase = ""
    for word in phrase.split():
        w = word.lower()
        syns = wn.synsets(w)
        hypo = []
        hyper = []
        if len(syns) > 0: hypo = syns[0].hyponyms()
        if len(syns) > 0: hyper = syns[0].hypernyms()
#        print hypo
#        print hyper
#TODO we want to ensure ~the same number of words, but have them
#change, so we'll need a way to allow for longer phrases and perhaps
#skip the next couple of words to keep it within 0/+1
        if len(syns) > 1 and len(word) > 3 and random.random() > 0.5:
#            print syns
#            print random.choice(syns).lemma_names()[0]
            newphrase += random.choice(syns[1:]).lemma_names()[0];
        elif len(hypo) > 0 and len(word) > 3 and random.random() > 0.5:
            newphrase += random.choice(hypo).lemma_names()[0];
        elif len(hyper) > 0 and len(word) > 3 and random.random() > 0.5:
            newphrase += random.choice(hyper).lemma_names()[0];
        else: newphrase += word;
        newphrase += " "
    return newphrase

def verse():
    return "arms and the man who of old from the coasts of Troy came, an exile of fate, to Italy and to the shore of Lavinium; hard driven on land and on the deep by the violence of heaven, for cruel Juno's unforgetful anger, and hard bestead in war also ere he might found a city and carry his gods into Latium; from whom is the Latin race, the lords of Alba, and the stately city Rome."

def templater(current):
    ver = replacer(current)
    return ver 

def repeatfilter(verse):
    derepeat = []
    words = verse.split()
    for k in range(len(words)):
        if k > 0 and words[k] != words[k-1]:
            derepeat.append(words[k])
    return string.join(derepeat)

def printverse(current):
    verse = templater(current)
#TODO we may want to filter successive identical words
    verse = repeatfilter(verse)
    verse += "\n"
    return verse.replace("_"," ");

if __name__ == '__main__':
    print "I sing of " + verse() + "\n"
    current = verse()
    for i in range(0,624):
        nextv = printverse(current)
        print "I sing of " + nextv
#        print "I sing of " + nextv
        current = nextv

