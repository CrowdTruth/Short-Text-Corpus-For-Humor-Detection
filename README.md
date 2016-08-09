# Short text corpus with focus on humor detection
This repository was created for publication of the datasets useful for humor recognition in one-liners. This repository contains six datasets and the python code used in the process of gathering the datasets. 
The six datasets are the following:

## 1. Humorous Jokes

    Filename: humorous_jokes
    Filetype: .pickle
    Size: 11743 items
    Sources: Twitter.com, www.textfiles.com/humor/, http://www.funnyshortjokes.com/, http://www.laughfactory.com/jokes, http://goodriddlesnow.com/jokes/, http://onelinefun.com and several other, smaller contributors
    Short description: This dataset contains all humorous jokes that were gathered in the process, which can be used as positive samples for humor recognition tasks. Jokes that had a Jaccard similarity coefficient higher than or equal to 0.9 were removed  in the deduplication process (Deduplication.py). This dataset was used to compile datasets 1.1 and 1.2. The first contains just the jokes in this dataset shorter than 140 characters, whereas the latter consists of all jokes containing more than 140 letters. Disclaimer: Some of the jokes may be racist, homophobic or insulting in another way.

## 1.1. Oneliners

    Filename: short_oneliners
    Filetype: .pickle
    Size: 10076 items
        
## 1.2. Longer jokes

    Filename: longer_jokes
    Filetype: .pickle
    Size: 1667 items
    
## 2. Reuters Headlines

    Filename: reuters
    Filetype: .pickle
    Size: 10142 items
    Sources: Twitter
    Short description: This dataset contains headlines tweeted by international press agency Reuters. Retweets were excluded for pre-processing purposes and to ensure the original source is known. Since the Twitter API only allows us to retrieve up to 3200 tweets (including retweets) from a single user account, we scraped tweets from multiple Reuters Twitter accounts: "reuters", "ReutersWorld", "ReutersUK" and "ReutersScience". The first covers Reuters' top news, the second one news from all over the world, the third one news from the UK and the last one covers science. The tweets from Reuters were gathered between 18-07-2016 and 05-08-2016. The headlines that had a Jaccard similarity coefficient higher than or equal to 0.9 in comparison to other headlines in the set were removed in the deduplication process (Deduplication.py).

## 3. English Proverbs

    Filename: proverbs
    Filetype: .pickle
    Size: 1019 items
    Sources: http://www.citehr.com/32222-1000-english-proverbs-sayings-love-blind.html, http://www.english-for-students.com/Proverbs.html
    Short description: This dataset contains a large part of existing English proverbs. Deduplication has been applied to remove duplicate proverbs (Deduplication.py).

## 4. Wikipedia sentences

    Filename: short_wiki_sentences
    Filetype: .pickle
    Size: 10076 items
    Sources: http://www.cs.pomona.edu/~dkauchak/simplification/
    Short description: Visit source URL for information on the data itself. This file contains a random selection of wikipedia sentences from the source file (the unsimplified one, to be specific) that were shorter than - or equal to- 140 characters. The random selection was done using "wiki_sentence_selector.py".

#The Python files:
These files are primarily here so that anyone can repeat the data gathering process and/or understand it.

##Deduplication.py

This python program can be used to merge two files into one, deleting all (near-) duplicate sentences. It creates a Bag-of-Words representation of the input sentences and calculates the overlap in informative words that remain (jaccard-coefficient). If you only wish to remove duplicate sentences that have an exact match when represented as a bag-of-words, change the threshold from the default 0.9, to 1.0.

## Extract_from_twitter.py

This program can be used to retrieve up to the latest 3200 tweets that were sent from a twitter account. Note that by default, this code does not store retweets by the user.
    
## separate_by_sent_length.py

This program was used to separate the oneliners in two groups: Short ones and long ones.
    
## web_scraper.py

This program contains only an example, basic web scraper for retrieving sentences. As each website is designed differently, a lot of changes have to be made before it works for another source website.
    
## write_functions.py

This file just contains a ready to go python function for saving a list of strings to a pickle file
