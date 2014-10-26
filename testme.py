#!/usr/bin/env python

from twython import Twython
from utils import makeWordDict, makePlot, bin
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts




import time



APP_KEY = '1cbFUR1QalNkZGzo5lbuw'
APP_SECRET = '8DnD2GDiZomefQIHwnrw33nfoeSjCbR5QugVeKUgk'



twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()



twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)







wordLength = []
mywords = []
n_scrapes = 10
for i in range(n_scrapes):
    tweets = twitter.search(q='#monday')
    time.sleep(3)
    print "we are on iteration %i of %i"%(i+1, n_scrapes)
    for key in tweets['statuses']:
        mywords.append(key['text'].encode("ascii","ignore"))
        for word in (key['text']).split():
            wordLength.append(len(word))

# mywords = mywords.encode("ascii", "ignore")
tags = make_tags(get_tag_counts(mywords), maxsize=80)

create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')

d = makeWordDict(mywords)
# print d
# for key in d:
#     print key , d[key]


# wordLength = sorted(wordLength)
a,b, = bin(inputData = wordLength, binWidth = 1)
# # print wordLength
# 
# 
makePlot(b,a)
# 
# a_1, b_1 = bin(inputData=wordLength, binWidth = 5)
# makePlot(b_1,a_1)
