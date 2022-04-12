import re
from readability import langdata
from collections import Counter
import nltk
import wordfreq


def paragraphs(text):
    """Returns a list of all the paragraphs in a text"""
    para_list = re.split('\n\n+', text)
    return para_list


def sentences(text):
    """Returns a list of all the sentences in a text"""
    sents = re.sub(r'([".!?]) ', r'\1\n', text)
    sents = re.split('\n+', sents)
    sentences = []
    for sentence in sents:
        if sentence != "":
            sentences += [sentence]
    return sentences


def words(text):
    """Returns a list of all the individual words in a text"""
    punctuation = '"".?!\'\'•: ,``()'
    word_list = [word for word in nltk.tokenize.word_tokenize(text)
                 if word not in punctuation or ""]
    return word_list


def characters(text):
    """Returns a string of text with puncutation removed"""
    all_chars = re.sub(r"[ .!?,'\"`;:()]", "", text)
    all_chars = all_chars.replace("\n", "")
    return all_chars


def total_syll_count(text):
    syllable_count = 0
    for word in words(text):
        syllable_count += syll_count_word(word)
    return syllable_count


def syll_count_word(word):
    return langdata.countsyllables_nlde(word)


def total_word_count(text):
    """Returns the total amount of words"""
    return len(words(text))


def unique_words_count(text):
    """Returns the total amount of unique words"""
    return len(set(words(text)))


def average_word_length_char(text):
    """Returns the average length of words"""
    return len(characters(text)) / len(words(text))


def n_most_used_words(text, freq):
    """Returns a list of the 10 most used keywords in the text"""
    ignore = wordfreq.top_n_list(lang='nl', n=100)
    lower_text = text.lower()
    clean_text = re.sub(r'[^\w\s]', "", lower_text)
    word_freq_text = Counter(word for word in clean_text.split()
                             if word not in ignore)
    return word_freq_text.most_common(freq)


def words_chars_over_avg(text):
    """Returns a number of the words that are longer than the average word"""
    over_avg = 0
    for word in text.split():
        if len(word) > average_word_length_char(text):
            over_avg += 1
    return over_avg


def longest_word(text):
    """Returns the longest word in a text"""
    longest_word_str = ""
    for word in words(text):
        if len(word) > len(longest_word_str):
            longest_word_str = word
    return longest_word_str


def avg_syll_per_word(text):
    """Returns the average amount of syllables per word"""
    return total_syll_count(text) / total_word_count(text)


# -------------- SENTENCE STATISTICS ------------------
def total_count_sentences(text):
    """Returns the amount of sentences"""
    return len(sentences(text))


def avg_word_count_per_sent(text):
    """Returns the average amount of words per sentence"""
    return total_word_count(text) / total_count_sentences(text)


def avg_syll_count_per_sent(text):
    """Returns the average amount of syllables per sentence """
    return total_syll_count(text) / total_count_sentences(text)


def avg_char_count_per_sent(text):
    """Returns the average amount of characters per sentence"""
    char_count = 0
    for sentence in sentences(text):
        char_count += len(sentence)
    return char_count / len(sentences(text))


def longest_sentence(text):
    """Returns the longest sentence in a text"""
    longest_sent = ""
    for sentence in sentences(text):
        if len(sentence.split()) > len(longest_sent.split()):
            longest_sent = sentence
    return longest_sent
