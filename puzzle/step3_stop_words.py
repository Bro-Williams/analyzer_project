"""Убираем стоп слова"""
# pip install nltk
import nltk
# скачиваем стопслова
nltk.download('stopwords')
from nltk.corpus import stopwords

def no_stop(words):
    """
    Убираем из списка стоп слова
    :param words: входной список слов со стоп словами
    :return: новый список слов без стоп слов
    """
    # получаем русские стоп слова
    stop_words = stopwords.words('russian')

    without_stop = []
    for word in words:
        if word not in stop_words:
            without_stop.append(word)
    # возвращаем слова без стоп слов
    return without_stop


