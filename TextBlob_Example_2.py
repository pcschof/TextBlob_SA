import textblob
import json
import sys
import urllib.request
import urllib.parse
from textblob import TextBlob
import html


def tb(article):
    # print results
    print(article)
    # pass results through textblob
    blob = TextBlob(article)

# for loop to print out the sentence, its polarity, and noun phrases within each sentence
    for sentence in blob.sentences:
         print(sentence)
         print(sentence.sentiment.polarity)
         print(sentence.noun_phrases)

<<<<<<< HEAD

=======
>>>>>>> f77f74a5c3bf56b2150a418cfc19f84e2a0ed765
# initialize endpoint connection
url = 'http://ec2-174-129-144-17.compute-1.amazonaws.com:8184/sbcmanager/articles/ROM'
# request connection
req = urllib.request.Request(url)
# open url
resp = urllib.request.urlopen(req)
# read text in url
resp_data = resp.read()
# decode text in utf-8 format
resp_data = resp_data.decode("utf-8")
json_format = json.loads(resp_data)
articles = json_format["articles"]
for a in articles:
<<<<<<< HEAD
    tb(html.unescape(articles[a].replace("\n", "\n")))

'''
titles = articles.keys()
for  i in range (len(titles)):
    content = articles[title]
    print("Content: " + contentarticles[a].replace("\n", "")
    tb(content)
'''
=======
    tb(html.unescape(articles[a].replace("\n", "")))
>>>>>>> f77f74a5c3bf56b2150a418cfc19f84e2a0ed765


