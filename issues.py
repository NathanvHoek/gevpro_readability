import statistics

# This file is for analysing the text and providing the reader
# with potential issues


def language_checker(text):
    pass


# -------------- POTENTIAL WORD ISSUES --------------


def warning_long_word(text):
    words = []
    for word in text.split():
        if len(word) > 12:
            words.append(word)
    return words


def warning_difficult_word(text):
    words = []
    for word in text.split():
        if statistics.syll_count_word(word) >= 6:
            words.append(word)
    return words


def warning_rare_word(text):
    for word in text.split():
        if word == statistics.rare_words(word):
            return word


# -------------- POTENTIAL SENTENCE ISSUES --------------


def warning_long_sentences(text):
    sentences = statistics.sentences(text)
    for sentence in sentences:
        if len(sentence.split()) > 2:
            sentences.append(sentence)
    return sentences


def warning_passive_voice():
    pass  # kon alleen dingen met SpaCy vinden, dus moeten even kijken hoe belangrijk dit is.


def repeat_after_each_other(text):
    pass


def first_word_of_sent_repeat():
    pass


def negatives():
    pass


def adverbs():
    pass

