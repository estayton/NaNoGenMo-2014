#!/usr/bin/env python
from __future__ import division
"I sing of"
__author__ = "Erik Stayton"
__copyright__ = "Copyright 2014 Erik Stayton"
__license__ = "CC-BY-SA"
__version__ = "0.0.2"
__status__ = 'Development'

import random;
import sys;
import os;
import nltk;
import string;
import math;
from nltk.corpus import wordnet as wn;

def join(array1,array2): #join two arrays and return the result
    output = array1
    for item in array2:
        output.append(item)
    return output

def captitle(word): #capitalize the first letter of a word
    return word[0].title()+word[1:]

#TODO consider a more intelligent way to trim, or a move back to
#keeping wordnet "words" like british_west_africa together as one
def trimphrase(phrase,length):
    splitphrase = phrase.replace("_"," ").split()
#    newlength = len(splitphrase)
    splitphrase.reverse()
#    print "SPLITPHRASE: " + str(splitphrase)
#    print "LENGTH: " + str(length)
    splitphrase = splitphrase[:length]
#    print "SPLITPHRASE: " + str(splitphrase)
    splitphrase.reverse()
    return string.join(splitphrase) + " "

def replacer(phrase):
    newphrase = ""
    length = len(phrase.split())
#    skipcounter = 0
    for word in phrase.split():
#        if skipcounter > 0:
#            skipcounter = skipcounter - 1
#        else: 
            w = word.lower()
            syns = wn.synsets(w)
            hypo = []
            hyper = []
            if len(syns) > 0: hypo = syns[0].hyponyms()
            if len(syns) > 0: hyper = syns[0].hypernyms()
#        print hypo
#        print hyper
#TODO check if we need to add back in len(word) > 2 conditions!
            wordset = []
            newword = ""
            if len(hypo) > 0 and random.random() > 0.5:
                wordset = hypo
            elif len(hyper) > 0 and random.random() > 0.5:
                wordset = hyper
            elif random.random() > 0.2:
#            print syns
#            print random.choice(syns).lemma_names()[0]
                wordset = syns
            if len(wordset) > 0:
#            print "REP"
                newword = random.choice(random.choice(wordset).lemma_names());
            else: newword = word;
#        print "NEW "+newword
        
#            newlength = len(newword.split("_"))
#            if newlength > 1:
#                skipcounter = newlength - 1 - math.floor(random.random() + 0)
            newphrase += newword
            newphrase += " "
    newphrase = trimphrase(newphrase,length)
#    print "NEWPHRASE: "+ str(newphrase)
    return newphrase

def interleave(tupleArrays):
    (first,second) = tupleArrays;
    final = first + second
    final[::2] = first
    final[1::2] = second
    return final

def verse():
#    return "arms and the man who of old from the coasts of Troy came, an exile of fate, to Italy and to the shore of Lavinium; hard driven on land and on the deep by the violence of heaven, for cruel Juno's unforgetful anger, and hard bestead in war also ere he might found a city and carry his gods into Latium; from whom is the Latin race, the lords of Alba, and the stately city Rome."
#    return "arms and the man"
    return (["arms ", "man ", "of old ", "coasts of Troy ", "exile ", "fate, ","Italy ","shore ", "hard driven ", "land ", "deep ", "violence ", "heaven, ", "cruel Juno's unforgetful anger, ","hard bestead ", "war ", "city ", "carry his gods ", "whom ", "Latin race, ", "lords ", "stately city Rome."],["and the ","who ","from the ","came, an ","of ", "to ", "and to the ", "of Lavinium; ", "on ","and on the ","by the ","of ","for ","and ","in ","also ere he might found a ","and ", "into Latium; from ","is the ", "the ", "of Alba, and the "])


def templater(current):
    ver = replacer(current)
    return ver 

def printer(start, verse):
    return "" + start + string.join(interleave(verse),'') + "\n"

def repeatfilter(verse):
#    print "VERSE: "+str(verse)
#    print "TYPE: "+str(type(verse))
    derepeat = []
    words = verse.split()
#    print "VER"+ verse
    for k in range(len(words)):
        if k == 0: derepeat.append(words[k])
        elif k > 0 and words[k] != words[k-1]:
            derepeat.append(words[k])
    return string.join(derepeat)+" "

def nextverse(current):
    (tochange,fixed) = current;
    changed = []
    for item in tochange:
        changed.append(repeatfilter(templater(item)).replace("_"," "))
    return (changed,fixed);

if __name__ == '__main__':
    print printer("I sing of ", verse())
    current = verse()
    for i in range(0,624):
        nextv = nextverse(current)
        print printer("I sing of ", nextv)
#        print "I sing of " + nextv
        current = nextv

