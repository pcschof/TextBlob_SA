# this code connects to the DynamoDB API to run a textblob sentiment analysis on an article in the DB

# up to 10 articles pertaining to a given ticker are queried. Desired ticker should be entered at the end of the
# url variable on line 29 (example: in http://ec2-174-129-144-17.compute-1.amazonaws.com:8184/sbcmanager/articles/ROM,
# ROM is ticker being returned)

# the code returns (in order):
# - article 1 full text
# - article 1 broken down by sentence
# - article 1 polarity score by sentence
# - article 2 full text
# - article 2 broken down by sentence
# - article 2 polarity score by sentence
# - article 3.....

import textblob
import json
import sys
import urllib.request
import urllib.parse
from textblob import TextBlob
import html


def tb(article):
    # prints article
    print(article)
    # pass article into TextBlob
    blob = TextBlob(article)

# for loop to print out each sentence and its polarity
    for sentence in blob.sentences:
         print(sentence)
         print('Sentence Polarity Score:', sentence.sentiment.polarity)

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
# transform decoded text from string to JSON dictionary
json_format = json.loads(resp_data)
# parse dictionary by individual articles
articles = json_format["articles"]
# format articles to replace unwanted character with a new line
for a in articles:
    tb(html.unescape(articles[a].replace("\n", "\n")))


# end of script
