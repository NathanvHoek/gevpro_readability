def warning_sentences():
    text = ['hello', 'hello there', 'hello there yay']
    sentences = []
    for sentence in text:
        if len(sentence.split()) > 2:
            sentences.append(sentence)
    return sentences


def warning_long_word(text):
    words = []
    for word in text.split():
        if len(word) > 12:
            words.append(word)
    return words