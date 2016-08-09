'''Authentication step'''
# If its the first time you use this script, First run the following statement in your
# commandline: pip install twitter
import twitter 
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = '' # to get the oauth credentials, you need to click on the 'Create my access token' button and wait a moment
OAUTH_TOKEN_SECRET = ''
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
print "Authentication sent"

'''Tweet scraping, stripping (URLS) and saving step'''

import re
import write_functions as w

#Define the user you wish to gather the latest tweets from
user = 'ReutersScience'

latest_status_id = 987796177497096200 #Arbitrary high number. NOTE: Make sure the latest tweet sent by your user is below this threshold
complete_statuses_list = []
amount_of_tweets_desired = 3200 #The number of tweets you want to gather from the respective user. This includes rts in its count. 
#Add extra on accounts that Retweet a lot. Twitter allows you to request a maximum of 3200 of the latest tweets per user account and 200 per request
for i in range(amount_of_tweets_desired/200):
    statuses = twitter_api.statuses.user_timeline(screen_name=user, count=201, max_id= (latest_status_id-1),
                                                  include_entities=False, include_rts=False) 
    #if you want to include retweets by the user, include_rts should be set to True
    status_ids = [status['id']
        for status in statuses ]
    
    # Use "[re.sub(....)" if you need all links to be removed from the tweet and "[status['text']" if not.
    complete_statuses_list +=  [re.sub(r"http\S+", "",status['text']) #[status['text']
        for status in statuses]

    latest_status_id = status_ids[-1] #is used to iterate to next tweet
    print "Scraped the %d latest tweets with an ID lower than %d"% (len(status_ids), latest_status_id)
print "Total number of tweets found: %d." %len(complete_statuses_list)

# Write away the data
savename = "%s"%user
w.write_to_pickle(savename,complete_statuses_list)