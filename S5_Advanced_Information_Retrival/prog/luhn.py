#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import collections
import re
import string
from itertools import tee, izip
import urllib2
from argparse import ArgumentParser
try:
    import nltk
except:
    print('Please install nltk. After that run >python >import nltk >nltk.download()')
try:
    from BeautifulSoup import BeautifulSoup
except:
    print('Please install BeautifulSoup')


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", help="The url to the content")
    parser.add_argument("-b", "--bellcurve", type=int, help="The number of words that get cut of from both sides of the relevance distribution", default="15")
    return parser.parse_args()


def pair(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def get_webpage_paragraphs(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]  # wikipedia needs this
    resource = opener.open(url)
    data = resource.read()
    resource.close()
    soup = BeautifulSoup(data)

    # Getting all paragraphs (<p>blabla</p>) from wikipage.
    text = ''
    for sentence in soup.findAll('p'):
        text += str(sentence)

    # Remove HTML Tags
    text = re.sub(r'(<.*?>)', '', text)
    text = re.sub(r'(<\/.*?>)', '', text)

    # Removing Wiki links
    text = re.sub(r'\[.{1,3}\]', '', text)

    return text


def remove_fringe(text):
    # Clean up the strange acronyms and abrevations
    unstranged_text = ''
    for word0, word1 in pair(text.split(' ')):
        try:
            if (word0[-1] == '.' and len(word0) < 3
               and word1[-1] == '.' and len(word1) < 3):
                unstranged_text += ' %s%s' % (word0, word1[-1])
            elif word0[-1] == '.' and word0[0:-1].isdigit():
                unstranged_text += ' %s%s' % (word0, word1)
            else:
                unstranged_text += ' %s' % word0
        except:
            pass

    # Processing special cases.
    text = unstranged_text.replace('ca.', 'ca')

    return text


def get_significant_words(text, bell_cut):
    table = string.maketrans('', '')

    # Removing punctuation to count words
    word_string = text.translate(table, string.punctuation)

    # Creating list of seperate words
    word_list = word_string.split(" ")

    #Counting words
    cnt = collections.Counter()
    for word in word_list:
        cnt[word] += 1

    # Getting occurence distribution
    occurence_distribution = set()
    for word in cnt:
        occurence_distribution.add(cnt[word])

    # Cutting occurence distribution into bell curve (Simulating bell curve)
    bell_curve = list(occurence_distribution)[bell_cut:-bell_cut]

    # Creating list of significant words according to the words occurence in the bell curve
    significant_words = [word for word in cnt if cnt[word] in bell_curve]

    return significant_words


def get_sentences(text):
    # Split text into sentences
    sentences = nltk.sent_tokenize(text)
    return sentences


def get_significant_sentences(sentences, text, significant_words):
    auto_abstract = []
    for sentence in sentences:
        insignificance, insignificant = 0, False
        cut_sentence = sentence.split(' ')[2:-2]

        if len(cut_sentence) > 2:
            for word in cut_sentence:
                if word not in significant_words:
                    insignificance += 1
                    if insignificance == 4:
                        insignificant = True
                        break
                else:
                    insignificance = 0
            if not insignificant:
                auto_abstract.append(sentence)

    return ' '.join(auto_abstract)


def pipeline(url, bell_cut):
    web_content = get_webpage_paragraphs(url)
    clean_web_content = remove_fringe(web_content)
    significant_words = get_significant_words(clean_web_content, bell_cut)
    sentences = get_sentences(clean_web_content)
    significant_sentences = get_significant_sentences(sentences, clean_web_content, significant_words)
    return significant_sentences


if __name__ == '__main__':
    args = parse_arguments()

    if not args.input:
        args.input = "http://de.wikipedia.org/wiki/Mäusebussard"

    print(pipeline(args.input, args.bellcurve))
