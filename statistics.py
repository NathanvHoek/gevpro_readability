import re
from readability import langdata
from wordfreq import zipf_frequency
from collections import Counter

with open('nos001.txt', 'r') as file:
    text = file.read()

# -------- BASIC VARIABLES ------------


def sentences(text):
    """Splits a text into individual sentences and
    returns this as a list"""
    sents = re.sub(r'([".!?]) ', r'\1\n', text)
    sents = re.split('\n+', sents)
    sentences = []
    for sentence in sents:
        sentences += [sentence]
    return sentences


def words(text):
    """Splits a text into individual words and
    returns this as a list"""
    return re.split("\s|(?<!\d)[,.](?!\d)", text)


def characters():
    words = words(text)
    return words.split()

# -------- WORD STATISTICS ------------


def total_word_count(text):
    """Returns the total amount of words"""
    return len(text.split())


def total_unique_words(text):
    """Returns the total amount of unique words"""
    unique_words = len(set(text.split()))
    return unique_words


def total_repeat_words():
    """Returns the total amount of repeated words"""
    pass


def average_word_length(text):
    """Returns the average length of words"""
    words = text.split()
    average = sum(len(word) for word in words) / len(words)
    return average


def long_words(text):
    """Returns words that are regarded as long"""
    for word in text.split():
        if len(word):
            pass


def rare_words(word):
    """Returns words that are rarely used in Dutch"""
    if zipf_frequency(word, 'nl') < 3:
        print('This is a rare word')
        print(zipf_frequency(word, 'nl'))


def avg_char_per_word(text):
    """Returns the average amount of characters per word"""
    return total_characters_count(text)/total_word_count(text)


def avg_syll_per_word():
    """Returns the average amount of syllables per word"""
    return total_syll_count() / total_word_count()


def syll_count_word(word):
    score = langdata.countsyllables_nlde(word)
    return score


def n_most_used_words(text):
    """Returns the 10 most used words in the text"""
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

    word_counter = Counter(wordcount)
    return word_counter.most_common(10)


def words_chars_over_avg(text):
    """Returns words that are longer than the average word length"""
    too_long = 0
    for word in text.split():
        if len(word) > average_word_length(text):
            too_long += 1
        else:
            too_long = 1
    return too_long


# ------------- SENTENCES STATISTICS


def total_count_sentences(text):
    """Returns the total amount of sentences in the text"""
    return re.split(r'[.!?]+', text)


def avg_word_count_per_sent(text):
    """Returns the average amount of words per sentence"""
    parts = [len(line.split()) for line in re.split(r'[?!.]', text) if line.strip()]
    return sum(parts) / len(parts)


def avg_syll_count_per_sent():
    """Returns the average amount of syllables per sentence"""
    return total_syll_count() / total_count_sentences()


def longest_sentence(text):
    """Returns the longest sentence in the text"""
    sentences = re.split("\s|(?<!\d)[,.](?!\d)", text)
    longest_sent = ""
    for sent in sentences:
        if len(sent) > len(longest_sent):
            longest_sent = sent
    return longest_sent


def avg_char_count_per_sent(text):
    """Returns the average amount of characters per sentence"""
    sentences = re.split("\s|(?<!\d)[,.](?!\d)", text)

    char_count = 0
    for sent in sentences:
        char = sent.split()
        char_count += len(char)

    return char_count / len(sentences)


# ------------- FULL TEXT STATISTICS
def total_characters_count(text):
    """Returns the total amount of characters in the text"""
    count = 0
    for words in text:
        for char in words:
            count += 1
    return count


def total_syll_count(text):
    """Returns the total amount of syllables in the text"""
    words = text.split()
    return countsyllables_nlde(words) #import andreas' module



