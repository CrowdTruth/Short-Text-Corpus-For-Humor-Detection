# -*- coding: utf-8 -*-
"""
This file can be used to import sentences from a CSV file, and store them
 in two separate files based on sentence length.
"""
import write_functions as w
import cPickle as pickle
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

# The following code opens a CSV file and stores the lines in a variable of type list
filename = 'humorous_jokes.pickle'
sentences = []
sentences = pickle.load(open(filename))
print "File succesfully imported. The file contains %d sentences." %len(sentences)

# Count the number of letters in each sentence
short_jokes = []
long_jokes = []

for sent in sentences:
    letter_counter = 0
    for char in sent:
        if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
            letter_counter +=1
    if letter_counter <= 140:
        short_jokes.append(sent)
    else:
        long_jokes.append(sent)

# Some information on the data created
print "The short jokes file contains %d sentences."%len(short_jokes)
print "The longer jokes file contains %d sentences."%len(long_jokes)

# Write away the data to two separate pickle files
w.write_to_pickle('short_oneliners', short_jokes)
w.write_to_pickle('longer_jokes', long_jokes)