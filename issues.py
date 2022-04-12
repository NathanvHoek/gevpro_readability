
# This file is for analysing the text and providing the reader
# with potential issues


def language_checker():
    """Returns whether the file is dutch or not"""
    pass

# -------------- POTENTIAL WORD ISSUES --------------


def warning_long_word(text):
    words = []
    for word in text.split():
        if len(word) > 12:
            words.append(word)
    return words


def warning_difficult_word():
    pass


# less frequency words
def warning_rare_word():
    pass



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


def repeat_after_each_other():
    """Returns duplicate words directly after each other"""
    pass


def first_word_of_sent_repeat():
    """Returns the duplicate first words of two sentences after each other"""
    pass



def negatives():
    pass



def adverbs():
    pass

