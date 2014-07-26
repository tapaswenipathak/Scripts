import urllib2
import json

location = raw_input ("Enter your location : ")
response = urllib2.urlopen ('http://api.openweathermap.org/data/2.5/weather?q=' + location)
data = json.load (response)
print str (data['main']['temp'] - 273) + "C" 

