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


def warning_long_sentences(text):
    sentences = statistics.sentences(text)
    for sentence in sentences:
        if len(sentence.split()) > 2:
            sentences.append(sentence)
    return sentences


def warning_passive_voice():
    pass  # kon alleen dingen met SpaCy vinden, dus moeten even kijken hoe belangrijk dit is.


def repeating_words(text):
    words = text.split()
    word_counts = Counter(words)
    for word, count in sorted(word_counts.items()):
        if count >= 5:
            print('"%s" is %d keer herhaald.' % (word, count))


def first_word_of_sent_repeat():
    pass


def negatives():
    pass


def adverbs():
    pass

