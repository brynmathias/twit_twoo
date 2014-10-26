#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import re

def makeWordDict(sentance = None):
    # if not isinstance(sentance,str): sentance = str(sentance)
    d = {}
    # sentance = sentance
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', sentance)
    for url in urls:
        sentance = sentance.replace(url,"")
        print url, sentance , "\n_______________________________\n"
    sentance = sentance.replace("#", "")
    sentance = sentance.replace("@", "")
    sentance = sentance.split(" ")
    for word in sentance:
      if word in d: d[word] +=1
      else: d[word] = 1
    return d

def makePlot(bins = None, Labels = None):
	pos = np.arange(len(Labels))
	width = 1.0     # gives histogram aspect to the bar diagram

	ax = plt.axes()
	ax.set_xticks(pos+ 1/2)
	ax.set_xticklabels(Labels)
	plt.bar(pos, bins, 1, color='r')
	plt.show()
    
    
def bin(inputData = None, binWidth = 1):
    """docstring for bin"""
    n_bins = int(max(inputData)/binWidth)+1
    bins = [i*binWidth for i in range(n_bins+1)]
    counts = [ i * 0 for i in range(n_bins+1)]
    for value in inputData:
        counts[int(value/binWidth)]+=1
    return bins, counts