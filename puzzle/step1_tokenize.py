"""Разбиваем текст на слова"""
import re
import string

def hands_re(text):
    """
    Разбивает текст на слова регулярками
    :param text: Входной текст
    :return: список слов
    """
    # собираем символы которые будем отбрасывать
    punctuation = string.punctuation + '\u2014\u2013\u2012\u2010\u2212' + '«»‹›‘’“”„`'
    word_tokenize = re.compile(r"([^\w_\u2019\u2010\u002F-]|[+])")
    words = []
    for token in word_tokenize.split(text):
        # если слово не попадает в те которые мы исключаем
        if token and not token.isspace() and not token in punctuation:
            words.append(token.lower())
    return words
