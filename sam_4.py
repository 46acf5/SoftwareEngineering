import re

def load_forbidden_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        forbidden_words = file.read().split()
    return forbidden_words


def censor_text(text, forbidden_words):
    """Замена запрещенных слов на звездочки"""
    for word in forbidden_words:
        # Используем регулярные выражения для поиска слов независимо от регистра
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub('*' * len(word), text)
    return text


def main():
    # Загрузка запрещенных слов из файла
    forbidden_words = load_forbidden_words('input.txt')
    # Ввод предложения от пользователя
    input_text = input("Введите предложение: ")
    # Замена запрещенных слов
    censored_text = censor_text(input_text, forbidden_words)
    print(censored_text)

main()
