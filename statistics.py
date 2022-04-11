import re
import wordfreq
import nltk
from wordfreq import word_frequency, tokenize
import collections
#
# with open('nos001.txt', 'r') as file:
#     text = file.read()


# -------- WORD STATISTICS ------------
def total_word_count(text):
    return len(text.split())


def unique_words(text):
    words = len(set(text.split()))
    return words


def total_repeat_words():
    pass


def average_word_length(text):
    words = text.split()

    average = sum(len(word) for word in words) / len(words)
    return average


def long_words():
    pass


def rare_words():
    pass


def avg_char_per_word():
    pass


def avg_syll_per_word():
    pass


def syll_count_word():
    pass


## doe ik


def n_most_used_words(text):
    stopwords = ['en', 'maar', 'of', 'want', 'dus', 'nog', 'een', 'het', 'de']
    wordcount = {}

    for word in text.lower().split():
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace(":", "")
        word = word.replace("\"", "")
        word = word.replace("!", "")
        word = word.replace("â€œ", "")
        word = word.replace("â€˜", "")
        word = word.replace("*", "")
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

    word_counter = collections.Counter(wordcount)
    return word_counter.most_common(10)


def words_chars_over_avg(text):
    too_long = 0
    for word in text.split():
        if len(word) > average_word_length(text):
            too_long += 1
        else:
            too_long = 1
    return too_long


# ------------- SENTENCES STATISTICS


def total_count_sentences(text):
    return re.split(r'[.!?]+', text)


def avg_word_count_per_sent(text):
    parts = [len(line.split()) for line in re.split(r'[?!.]', text) if line.strip()]
    return sum(parts) / len(parts)


def avg_syll_count_per_sent():
    return total_syll_count() / total_count_sentences()

## tot dit


def longest_sentence():
    pass


def avg_char_count_per_sent():
    pass


# ------------- FULL TEXT STATISTICS
def total_characters_count():
    pass


def total_syll_count():
    pass

