from collections import Counter
import re
import wordfreq
import statistics


def language_is_dutch(text):
    """Checks if the language of the input is Dutch"""
    lower_text = text.lower()
    clean_text = re.sub(r'[^\w\s]', "", lower_text)
    word_freq_text = Counter(clean_text.split())
    top_10 = word_freq_text.most_common(10)
    sureness = 0
    for i in top_10:
        if i[0] in wordfreq.top_n_list(lang='nl', n=10):
            sureness += 1
    if sureness > 5:
        return True


def warning_long_word(word_list):
    """Returns words that contain 5 syllables or more"""
    words = []
    for word in word_list:
        if statistics.syll_count_word(word) > 3 and not re.search(r'\d', word):
            words += [word]
    return words


def warning_rare_word(text):
    """Returns words that are used less than 1 in 100.000.000 times"""
    rare_words = []
    for word in statistics.words(text):
        rarity = wordfreq.zipf_frequency(word, lang='nl')
        if rarity < 1:
            rare_words += [word]
    return set(rare_words)


def warning_long_sentences(text):
    """Returns the sentences which are longer than 20 characters"""
    long_sentences = []
    sentences = statistics.sentences(text)
    for sentence in sentences:
        if len(sentence.split()) > 20:
            long_sentences.append(sentence)
    return long_sentences


def warning_passive_voice(text):
    """Returns the sentences that are used in the passive voice"""
    passive_sentences = []
    reg_ex = r"(worden|werden|word|werd|wordt|is|was|zijn)" \
             r"[\w+ ]*?(ge[\w+]+[ntd])"
    for sentence in statistics.sentences(text):
        if re.search(reg_ex, sentence):
            passive_sentences += [sentence]
    return passive_sentences


def warning_first_word_of_sent_repeat(text):
    """Returns a list of the sentences that start with
    the same word with which the previous sentence starts
    """
    sentences_repeated = []
    for i in range(len(statistics.sentences(text)) - 1):
        sentence = statistics.sentences(text)[i]
        next_sentence = statistics.sentences(text)[i+1]
        if statistics.words(sentence)[0] == statistics.words(next_sentence)[0]:
            sentences_repeated += [next_sentence]
    return sentences_repeated
