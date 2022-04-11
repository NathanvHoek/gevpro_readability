import re
import wordfreq
import nltk
from readability import langdata
from wordfreq import zipf_frequency
from collections import Counter

with open('nos001.txt', 'r') as file:
    text = file.read()


# -------- WORD STATISTICS ------------

def total_word_count(text):
    return len(text.split())

def unique_words(text):
    words = len(set(text.split()))
    return words

def average_word_length(text):
    words = text.split()
    average = sum(len(word) for word in words) / len(words)
    return average


def long_words(text):
    for word in text.split():
        if len(word):
            pass

def rare_words(word):
    if zipf_frequency(word, 'nl') < 3:
        print('This is a rare word')
        print(zipf_frequency(word, 'nl'))

def avg_char_per_word(text):
    return total_characters_count(text)/total_word_count(text)

def avg_syll_per_word():
    return total_syll_count() / total_word_count()


def syll_count_word(word):
    score = langdata.countsyllables_nlde(word)
    return score

######################################

def n_most_used_words():
    pass

def words_chars_over_avg():
    pass

# ------------- SENTENCES STATISTICS

def total_count_sentences():
    pass

def avg_word_count_per_sent():
    pass

def avg_syll_count_per_sent():
    pass

####################################

def longest_sentence():
    pass

def avg_char_count_per_sent():
    pass


# ------------- FULL TEXT STATISTICS
def total_characters_count():
    pass


def total_syll_count(text):
    hello = nltk.sent_tokenize(text)
    print(hello)

def sentences(text):
    """Splits a text into individual sentences and
    returns this as a list
    """
    sents = re.sub(r'([".!?]) ', r'\1\n', text)
    sents = re.split('\n+', sents)
    sentences = []
    for sentence in sents:
        sentences += [sentence]
    return sentences

print(sentences(text))