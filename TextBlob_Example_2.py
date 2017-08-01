# this code connects to the DynamoDB API to run a textblob sentiment analysis on an article in the DB

# up to 10 articles pertaining to a given ticker are queried. Desired ticker should be entered at the end of the
# url variable on line 29 (example: in http://ec2-174-129-144-17.compute-1.amazonaws.com:8184/sbcmanager/articles/ROM,
# ROM is ticker being returned)

# the code returns (in order):
# Article title (key value)
# Article sentiment: polarity and subjectivity
# Article break down by sentence, sentence polarity

import textblob
import json
import sys
import urllib.request
import urllib.parse
from textblob import TextBlob
import html


def tb(article):
    # pass article into TextBlob
    blob = TextBlob(article)
    print("\n"'ARTICLE:', title)
    print('Sentiment Results -')
    print("Polarity:", blob.sentiment.polarity)
    print("Subjectivity:", blob.sentiment.subjectivity)

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
count = 0
for a in articles:
    for key, values in articles.items():
        title = key
        print(title)
    count = count + 1
    tb(html.unescape(articles[a].replace("\n", "\n")))

print('Total Number of Articles Analyzed:', count)
# end of script
