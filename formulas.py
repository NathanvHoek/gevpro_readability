import math
import statistics


def Brouwer(avg_word_len_syll, avg_sent_len_word):
    """Returns the score of the readability formula from Brouwer"""
    score = 195 - (66.7 * avg_word_len_syll) - (2 * avg_sent_len_word)
    if score > 100:
        status = 'Makkelijk leesbaar'
    elif score > 50:
        status = 'Normale leesbare tekst'
    else:
        status = 'Moeilijk leesbare tekst'
    return score, status


def Flesch_Douma(avg_word_len_syll, avg_sent_len_word):
    """Returns the score of the readability formula from Flesch-Douma"""
    score = 206.7 - (77 * avg_word_len_syll) - (0.93 * avg_sent_len_word)
    if score > 90:
        status = 'Niveau groep 6 basisschool'
    elif score > 80:
        status = 'Niveau groep 7 basisschool'
    elif score > 70:
        status = 'Niveau groep 8 basisschool'
    elif score > 60:
        status = 'Niveau lager middelbaar onderwijs'
    elif score > 50:
        status = 'Niveau hoger middelbaar onderwijs'
    elif score > 30:
        status = 'Niveau studenten'
    else:
        status = 'Niveau academici'
    return score, status


def long_words_SMOG(text):
    """Returns the number of words that are longer than 2 syllables"""
    long_word_count = 0
    for word in statistics.words(text):
        if statistics.syll_count_word(word) > 2:
            long_word_count += 1
    return long_word_count


def SMOG(long_words_count, total_sent_count):
    """Returns the score of the readability formula from Brouwer"""
    if total_sent_count <= 10:
        return 0, 'You should have more than 10 sentences.'
    else:
        score = 1.043 * math.sqrt((total_sent_count * (30/long_words_count))) + 3.1291
        if score > 211:
            status = 'Extreem moeilijk om te lezen'
        elif score >= 183:
            status = 'Heel moeilijk om te lezen'
        elif score >= 91:
            status = 'Moeilijk om te lezen'
        elif score >= 43:
            status = 'Beetje moeilijk om te lezen'
        elif score >= 21:
            status = 'Prima te begrijpen'
        elif score >= 13:
            status = 'Redelijk makkelijk te lezen'
        elif score >= 7:
            status = 'Makkelijk om te lezen'
        else:
            status = 'Heel erg makkelijk om te lezen'
        return score, status
