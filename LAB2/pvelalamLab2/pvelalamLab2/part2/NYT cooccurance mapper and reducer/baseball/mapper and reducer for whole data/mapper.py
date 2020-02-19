#!/usr/bin/env python
"""pair_mapper.py"""

import sys
import re
import string
from stemming.porter2 import stem

keywords = ['baseball', 'basketball', 'tennis', 'nfl', 'soccer', 'football']

stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'ago',
             'very', 'having', 'with', 'they', 'own', 'an', 'be', 'purposes', 'happy', 'experience', 'web', 'href', 'id',
             'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 'am',
             'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'improve', 'technologies', 'purposes', 'false',
             'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'rel',
             'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'happiness', 'happiest', 'accept', 'nd',
             'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'mr', 'st',
             'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'person', 'purpose', 'last', 'advertisementsupport',
             'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you',
             'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'website', 'cookie', 'cookies', 'said', 'index',
             'those', 'i', 'after', 'few', 'whom', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'abbreviation',
             'how', 'further', 'was', 'here', 'than', 'rt', 'de', 'advertisement', 'advertise', 'advertising', 'like', 'make', 'go', 'would', 's',
             't', 'like', 'get', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'doo',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'http', 'com', 'better', 'help', 'en', 'us', 'links', 'site']

top20 = ['year', 'team', 'game', 'one', 'time', 'season', 'player', 'new', 'first', 'play', 'two', 'leagu', 'sport', 'state', 'peopl', 'baseball', 'even', 'point', 'day', 'work']

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = re.sub(r"N.F.L.", "NFL",line)
    line = re.sub(r"http\S+", ' ', line)
    line = re.sub(r"[^a-zA-Z]+", ' ', line)
    line = line.lower()
    # split the line into words
    words = line.split()

    for i in range(0,len(words)-1):
        if words[i] not in keywords:
            if words[i] not in stopwords:
                sw1 = stem(words[i])
                if sw1 in top20:
                    if sw1 not in stopwords:
                        for j in range(i+1,(len(words))):
                            if words[j] not in keywords:
                                if words[j] not in stopwords:
                                    sw2 = stem(words[j])
                                    if sw2 not in stopwords:
                                        print "%s|%s\t%s" % (sw1,sw2, 1)
                            else:
                                print "%s|%s\t%s" % (sw1, words[j], 1)
        else:
            for j in range(i+1, (len(words))):
                if words[j] not in keywords:
                    if words[j] not in stopwords:
                        sw2 = stem(words[j])
                        if sw2 not in stopwords:
                            print "%s|%s\t%s" % (words[i], sw2, 1)
                else:
                    print "%s|%s\t%s" % (words[i], words[j], 1)


