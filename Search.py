import urllib
import json as m_json
Query = raw_input('Query: ')
Query = urllib.urlencode({'q': Query})
response = urllib.urlopen(
    'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + Query).read()
json = m_json.loads(response)
results = json['responseData']['results']
for result in results:
    title = result['title']
    url = result['url']
    print (title + '; ' + url)
