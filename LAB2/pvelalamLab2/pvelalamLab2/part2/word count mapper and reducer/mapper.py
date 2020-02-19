#!/usr/bin/env python
"""mapper_stop.py"""

import sys
import re
import string
from stemming.porter2 import stem

keywords = ['baseball', 'basketball', 'tennis', 'nfl', 'soccer', 'football']

stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'ago',
             'very', 'having', 'with', 'they', 'own', 'an', 'be', 'purposes', 'happy', 'experience', 'web', 'href', 'id',
             'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 'am', 'say', 'think','want',
             'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'improve', 'technologies', 'purposes', 'false',
             'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'rel', 'know',
             'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'happiness', 'happiest', 'accept', 'nd', 'could',
             'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'mr', 'st', 'also',
             'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'person', 'purpose', 'last', 'advertisementsupport',
             'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you',
             'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'website', 'cookie', 'cookies', 'said', 'index',
             'those', 'i', 'after', 'few', 'whom', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'abbreviation',
             'how', 'further', 'was', 'here', 'than', 'rt', 'de', 'advertisement', 'advertise', 'advertising', 'like', 'make', 'go', 'would', 's',
             't', 'like', 'get', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'doo',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'http', 'com', 'better', 'help', 'en', 'us', 'links', 'site']
# increase counters

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = re.sub(r"N.F.L.", "NFL",line)
    line = re.sub(r"http\S+", ' ', line)
    line = re.sub(r"[^a-zA-Z]+", ' ', line)
    line = line.lower()
    # split the line into words
    words = line.split()

    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if word not in keywords:
	    #if not word in nltk.corpus.stopwords.words('english'):
            if word not in stopwords:
	            sw = stem(word)
	            if sw not in stopwords:
	                print '%s\t%s' % (sw, 1)
        else:
            print '%s\t%s' % (word, 1)
