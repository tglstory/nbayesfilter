nbayesfilter
============

Naive bayes filter for Korean badchars. Written by Hyun Joon Seol (tglstory@gmail.com).

The Problem
-----------

Typographical errors are one of the most common problems in data driven processing in all languages. Unfortunately, Korean suffers from this error too. In a large corpus, even if a small portion is erroneous it can constitute a big problem if their counts are large enough to make it into the lexicon after pruning. It takes the place for less searched-for queries and may hinder from delivering correct results in a query search scenario. This project aims to detect these bad characters with a data-driven Bernoulli Naive Bayes methodology. It uses scikit-learn package and approaches the problem with character-based bigrams.

Training Corpus
---------------
The training corpus, named correct.txt and error.txt contains manually checked queries that seem to be wrong but are correct, and queries that seem to be wrong and is acutally wrong (with the help of two part-time employees). The initial training set before labeling comes from a quick script that detects uncommon characters in Korean (double end phonemes, uncommon dipthongs, etc). These characters are defined in the file bad.py.


