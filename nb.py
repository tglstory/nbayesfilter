#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB

with open("correct.txt") as fp:
    correct = fp.readlines()

with open("error.txt") as fp:
    error = fp.readlines()

correct = map(lambda x: unicode(x.rstrip()), correct)
error = map(lambda x: unicode(x.rstrip()), error)

bigram_vectorizer = CountVectorizer(analyzer="char_wb", ngram_range=(2,2), min_df=1)

total = correct+error
target = [1]*len(correct)+[0]*len(error)
training_data = bigram_vectorizer.fit_transform(total)

bnb = BernoulliNB()
bnb.fit(training_data, target)

