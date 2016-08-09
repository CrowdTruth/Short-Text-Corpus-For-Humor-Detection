# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 13:43:00 2016

@author: Sven
"""
import cPickle as pickle
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

def write_to_pickle(filename,list_of_sentences):
    print 'Creating new pickle file'
    f = open("%s.pickle"%filename, "wb")
    pickle.dump(list_of_sentences, f)
    f.close()
    print "The data was saved to %s.pickle. The file contains %d lines."%(filename, len(list_of_sentences))