import re


def tokenize_sentences(text):
    pass


def average_word_length(text):
    words = text.split()
    average = sum(len(word) for word in words) / len(words)
    return average


def count_words(text):
    return len(text.split())


def unique_words(text):
    words = len(set(text.split()))
    return words


def reading_time_minutes(text):
    read_speed = 250
    total_words = count_words(text)
    return total_words/read_speed