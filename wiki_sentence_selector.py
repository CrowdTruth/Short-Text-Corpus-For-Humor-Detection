# Required library imports
import cPickle as pickle
from random import randrange
import write_functions as w
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

# Import wikipedia dataset
file_object = open('wiki.txt' ,'r')
all_wiki_sentences = file_object.readlines()
print "File successfully opened. It contains %d sentences."%(len(all_wiki_sentences))

# Import dataset of oneliners
filename = "humorous_jokes.pickle"
oneliners = pickle.load(open(filename))

# Randomly pick as much sentences from the wikipedia dataset as there are jokes in the oneliner dataset
random_index = []
while len(random_index) < len(oneliners):
    random_no = randrange(len(all_wiki_sentences))
    if random_no not in random_index: # This statement ensures no random sentences are picked twice
        random_index.append(random_no)

wiki_sents = []
for i in random_index:
    wiki_sents.append(all_wiki_sentences[i])
w.write_to_pickle("wiki_sentences", wiki_sents)