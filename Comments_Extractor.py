import facebook
import requests

# Access Token
access_token = 'CAACEdEose0cBAMnG06gFP2RrQZBCB7b6MxhNVZCZCyulS1uQFEqxcTAUvSLbuGa61Y4r8IWMB3Y3nPeUcDCoQWjwNuk5Qfzq94m1AqKp8kBN7VGbdm7vnYQvNpI2O50Lb8LDbZAb7hMTdSKapy0dLZA8c56l3PwSED06P7v6mVBZBCwcdT6MbjkZArjLnSo0faVKAXhAhzGVwZDZD'

graph = facebook.GraphAPI(access_token)

# Post ID
post_id = '644817188920898_643794735689810'
comments = graph.get_object(post_id)['comments']

print comments

# Wrap this block in a while loop so we can keep paginating comments until
# exhausted.
while True:
    try:
        # Do what you want with each comment.  Here we just grab the message.
        for comment in comments['data']:
            print comment['message']

        comments = requests.get(comments['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break
