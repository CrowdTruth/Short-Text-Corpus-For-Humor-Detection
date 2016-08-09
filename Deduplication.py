# Imports
import cPickle as pickle
import write_functions as w
import nltk
import nltk.corpus
import nltk.tokenize.punkt
import string
import nltk.data
import nltk.stem.snowball
from collections import OrderedDict
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

# Declare variables
unprocessed_sentences = []

# Import the sentences that need processing in pickle
filename = "onelinefun.pickle"
unprocessed_sentences = pickle.load(open(filename))
print "File succesfully imported. The file contains %d sentences." %len(unprocessed_sentences)

#in case more pickle files need to be imported
filename2 = 'goodriddlesnow.pickle'
unprocessed_sentences2 = pickle.load(open(filename2))
print "File succesfully imported. The file contains %d sentences." %len(unprocessed_sentences2)
for i in unprocessed_sentences2:
    unprocessed_sentences.append(i)
    
filename3 = 'funnyshortjokes.pickle'
unprocessed_sentences3 = pickle.load(open(filename3))
print "File succesfully imported. The file contains %d sentences." %len(unprocessed_sentences3)
for i in unprocessed_sentences3:
    unprocessed_sentences.append(i)

filename4 = 'laughfactory.pickle'
unprocessed_sentences4 = pickle.load(open(filename4))
print "File succesfully imported. The file contains %d sentences." %len(unprocessed_sentences4)
for i in unprocessed_sentences4:
    unprocessed_sentences.append(i)

filename5 = 'humorous_oneliners_undoubled.pickle'
unprocessed_sentences5 = pickle.load(open(filename5))
print "File succesfully imported. The file contains %d sentences." %len(unprocessed_sentences5)
for i in unprocessed_sentences5:
    unprocessed_sentences.append(i)
   
file_object = open('Danoah_oneliners_60.txt','r')
textfile_oneliners = file_object.readlines()
unprocessed_sentences += textfile_oneliners


print "%d lines were imported and are ready for deduplication!"%len(unprocessed_sentences)
# In[19]:

# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

def is_ci_token_stopword_set_match(tokenset_a, tokenset_b, threshold=0.9): 
    """Check if a and b are matches, using jaccard coefficient."""
    ratio = len(set(tokenset_a).intersection(tokenset_b)) / (float(len(set(tokenset_a).union(tokenset_b)))+0.00000000000000001)
    return (ratio >= threshold)

def generate_bow(sentence):
    tokenset = [token.lower().strip(string.punctuation) for token in nltk.word_tokenize(sentence)\
                if token.lower().strip(string.punctuation) not in stopwords]
    return tokenset

# declare variables
remove_items = []
keep_sentences = []
tokensets = []

#Generate all bows
for i in unprocessed_sentences:
    tokensets.append(generate_bow(i))

print "Finished creating bow representations."

# Compare all sentences s for similarity with the sentences on index > s
for i in range(len(unprocessed_sentences)+1):
    if i not in remove_items:
        for item in range(i+1,len(unprocessed_sentences)):
            if is_ci_token_stopword_set_match(tokensets[i], tokensets[item]) == True:
                remove_items.append(item)
    if i%50 == 0: # Used to track progress of the deduplication
        print "processed %d sentences"%i
        
remove_items = list(OrderedDict.fromkeys(remove_items))
print "Removed items:"
print remove_items

for item in range(len(unprocessed_sentences)):
    if item not in remove_items:
        keep_sentences.append(unprocessed_sentences[item])

print "Amount of kept items: %d"%len(keep_sentences)
# Write away processed data
w.write_to_pickle("humorous_jokes",keep_sentences)