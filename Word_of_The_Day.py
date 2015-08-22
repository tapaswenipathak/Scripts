from wordnik import *
import urllib2
import json
import datetime

now = datetime.datetime.now()
todays_date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

# Get word of the day
URL = 'http://api.wordnik.com:80/v4/words.json/wordOfTheDay?date=' + \
    todays_date + '&api_key=d52b63b6880f17811310d0fbd3b0d3a8ef163a248f58dc831'
response = urllib2.urlopen(URL)
word_of_the_day = json.load(response)

# Print Details of Word of The Day
print "Word of The Day : " + word_of_the_day['word']
print "Meaning : " + word_of_the_day['definitions'][0]['text']
print "Sentence using " + word_of_the_day['word'] + " : " + word_of_the_day['examples'][0]['text']
