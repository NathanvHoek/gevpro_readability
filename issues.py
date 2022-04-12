import statistics
from collections import Counter

# This file is for analysing the text and providing the reader
# with potential issues


def language_checker(text):
    """Checks if the language of the input is Dutch"""
    pass


# -------------- POTENTIAL WORD ISSUES --------------


def warning_long_word(text):
    """Returns words that are longer than 12 characters"""
    words = []
    for word in text.split():
        if len(word) > 12:
            words.append(word)
    return words


def warning_difficult_word(text):
    """Returns words that contain 5 syllables or more"""
    words = []
    for word in text.split():
        if statistics.syll_count_word(word) >= 5:
            words.append(word)
    return words


def warning_rare_word(text):
    """Returns words that are rarely used in Dutch"""
    words = []
    for word in text.split():
        if word == statistics.rare_words(word):
            words.append(word)
        return words


# -------------- POTENTIAL SENTENCE ISSUES --------------


def warning_long_sentences():
    """Returns the sentences which are too long"""
    text = ['hello', 'hello there', 'hello there yay']
    sentences = []
    for sentence in text:
        if len(sentence.split()) > 2:
            sentences.append(sentence)
    return sentences



def warning_passive_voice():
    """Returns the sentences that are used in the passive voice"""
    pass


def repeating_words(text):
    """Returns duplicate words directly after each other"""
    words = text.split()
    word_counts = Counter(words)
    for word, count in sorted(word_counts.items()):
        if count >= 5:
            print('"%s" is %d keer herhaald.' % (word, count))


def first_word_of_sent_repeat():
    """Returns the duplicate first words of two sentences after each other"""
    pass



def negatives():
    pass



def adverbs():
    pass

