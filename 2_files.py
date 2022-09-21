"""
Домашнее задание №2
Работа с файлами
1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r') as open_file_read:
        read_file = open_file_read.read()

    words = read_file.split()
    amount_words = len(words)

    len_str = len(read_file)

    replace_dot = read_file.replace('.', '!')

    print(read_file)
    print(f'\nКоличество слов в файле - {amount_words}')
    print(f'\nДлина строки в в файле - {len_str}')

    with open('referat2.txt', 'w') as open_file_wrie:
        open_file_wrie.write(replace_dot)


if __name__ == "__main__":
    main()
