"""Частотный анализ слов"""

def analize(words):
    """
    Частотный анализ слов
    :param words: входной список слов
    :return: самое частое слово кортеж (слово, кол-во)
    """

    analyze = {}
    for word in words:
        # если слово уже есть в словаре
        if word in analyze:
            analyze[word] += 1
        else:
            analyze[word] = 1
    # сортируем словарь и получаем кортеж слово и самое большое кол-во
    result = sorted(analyze.items(), key=lambda item: item[1], reverse=True)
    # берем 1-ый элемент и слово - это будет тема
    theme = result[0]
    # возвращаем результат
    return theme[0]



