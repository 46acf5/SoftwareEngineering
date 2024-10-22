from collections import Counter
import re


def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # Удаление символов пунктуации
    words = re.findall(r'\b\w+\b', text)

    # Подсчет количества слов
    word_count = len(words)

    # Используем Counter для подсчета частоты слов
    word_freq = Counter(words)

    most_common_word, frequency = word_freq.most_common(1)[0]

    print(f"Общее количество слов: {word_count}")
    print(f"Самое частое слово: '{most_common_word}' встречается {frequency} раз(а)")


count_words('article.txt')
