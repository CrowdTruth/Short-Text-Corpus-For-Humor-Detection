# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:41:10 2016

@author: Sven
"""

from lxml import html
import requests
import write_functions as w

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

uri_string = ''
output1 = []
tree = html.fromstring(requests.get('http://www.funnyshortjokes.com/c/animal-jokes/page/1').content)
#print html.tostring(tree)
def find_categories(tree,name_category_class):      
    categories = tree.find_class('cat-item')
    url_c_names = []
    for c in categories:
        c_name = c.text_content().lower()
        stripped_c_name = ''.join(c for c in c_name if c not in '()0123456789')
        split_c_name = stripped_c_name.split()
        url_c_names.append('-'.join(s for s in split_c_name))
    return url_c_names
    
def find_page_max(tree,name_page_number_class):
    pages = tree.find_class(name_page_number_class)
    largest_value = 0
    for i in pages:
        is_number = False
        amount_of_numbers = 0
        pagenumber = i.text_content()
        for number in pagenumber:
            if number in '0123456789':
                amount_of_numbers +=1
        if amount_of_numbers == len(pagenumber):
            is_number = True
        if is_number == True and int(pagenumber) > largest_value:
            largest_value = int(pagenumber)
    return int(largest_value)

def scrape_webpages(url,upper_bound_page_no, name_text_class):
    elements = []
    
    for p in range(1, int(upper_bound_page_no)):
        #request_page = requests.get('%s%s'%(url,p))
        tree = html.fromstring(requests.get('%s%s'%(url,p)).content)
        elements += tree.find_class(name_text_class)
        
    print "Found %d lines"%len(elements)
    return elements

def scrape_user_ratings(tree, pos_classname,neg_classname):
    thumbs_up = tree.find_class(pos_classname)
    pos_ratings = []
    single_rating = []
    for t in thumbs_up:
        single_rating = [str(i) for i in t.text_content() if i in '0123456789']
        pos_no = ''
        for s in single_rating:
            pos_no = pos_no + s
        pos_ratings.append(int(pos_no))
    #print pos_ratings
    #Negative ratings
    thumbs_down = tree.find_class(neg_classname)
    neg_ratings = []
    single_rating = []
    for t in thumbs_down:
        single_rating = [str(i) for i in t.text_content() if i in '0123456789']
        neg_no = ''
        for s in single_rating:
            neg_no = neg_no + s
        neg_ratings.append(int(neg_no))
    #print neg_ratings
    #Calculate and return overall score
    scores = []
    if len(pos_ratings) == len(neg_ratings):
        for i in range(len(pos_ratings)):
            scores.append(pos_ratings[i]-neg_ratings[i])
    else:
        print 'Missing a positive or negative vote'
    return scores
    
text_class_name = 'post-text'
category_class_name = 'cat-item'
page_number_class_name = 'page-numbers'
pos_classname = 'thumbs-rating-up'
neg_classname = 'thumbs-rating-down'

#tree = html.fromstring(requests.get('http://www.funnyshortjokes.com/c/animal-jokes/page/1').content)
categories = find_categories(tree, category_class_name)

lines = []
for c in categories:
    found_lines = []
    tree = html.fromstring(requests.get('http://www.funnyshortjokes.com/c/%s/page/1'%c).content)
    page_max = find_page_max(tree,page_number_class_name)
    category_scores = []
    for p in range(1,page_max):
        tree = html.fromstring(requests.get('http://www.funnyshortjokes.com/c/%s/page/%d'%(c,p)).content)       
        category_scores = category_scores + scrape_user_ratings(tree, pos_classname,neg_classname)
    found_lines += scrape_webpages('http://www.funnyshortjokes.com/c/%s/page/'%(c),page_max,text_class_name)
    # Filter out not funny jokes.  
    keep_lines = []
    if len(category_scores) == len(found_lines):
        print '%d scores and %d lines found'%(len(category_scores), len(found_lines))
        for i in range(len(found_lines)):
            if category_scores[i] >= 0:
                #print category_scores[i]
                keep_lines.append(found_lines[i].text_content())
    else:
        print 'The number of scores and the number of lines are imbalanced'
        print '%d scores found'%len(category_scores)
        print '%d lines found'%len(found_lines)
    
    print "Finished processing %s.\n It contained %d Funny lines."%(c,len(keep_lines))
   
    lines.append(keep_lines)

for cat_lines in lines:
    for l in cat_lines:
        strip1 = l.strip('\n')
        strip2 = strip1.strip(' ')
        output1.append(strip2.strip('\n'))
        
print len(output1)

w.write_to_pickle("funnyshortjokes",output1)