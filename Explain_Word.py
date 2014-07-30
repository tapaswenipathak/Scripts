'''Using the Word API of WordNik
   Print the meaning and usage of word in sentences which the user enters'''

from wordnik import *
import urllib2
import json

input_word = raw_input ("Enter The Word : ")

#Get Meanings of the word
response = urllib2.urlopen ('http://api.wordnik.com:80/v4/word.json/' + input_word + '/definitions?limit=200&includeRelated=true&useCanonical=false&includeTags=false&api_key=d52b63b6880f17811310d0fbd3b0d3a8ef163a248f58dc831')
data_meaning = json.load (response)
data_len_meaning =  len (data_meaning)

#Get Senetences of the word
response = urllib2.urlopen ('http://api.wordnik.com:80/v4/word.json/' + input_word + '/topExample?useCanonical=false&api_key=d52b63b6880f17811310d0fbd3b0d3a8ef163a248f58dc831')
data_sentence = json.load (response)
data_len_sentence =  len (data_sentence)

#Get word of the day
response = urllib2.urlopen ('http://api.wordnik.com:80/v4/words.json/wordOfTheDay?date=2010-02-01&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5')
word_of_the_day = json.load (response)

#Print the Meanings
print "Meanings : "
for i in range (data_len_meaning) :
	print str (i + 1) + ". " + data_meaning[i]['text']

#A new line
print

#Print the sentences
print "Sentence : "
print data_sentence['text']

