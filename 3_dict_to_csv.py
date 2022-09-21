"""
Домашнее задание №2
Работа csv
1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору.
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv
"""

import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    people = [
        {'name': 'Misha', 'age': '45', 'job': 'Blacksmith'},
        {'name': 'Nikolay', 'age': '35', 'job': 'Doctor'},
        {'name': 'Ivan', 'age': '42', 'job': 'Engineer'},
    ]

    with open('people.csv', 'w') as csv_file:
        fieldnames = ['name', 'age', 'job']
        write = csv.DictWriter(csv_file, fieldnames=fieldnames)
        write.writeheader()
        write.writerows(people)
        csv_file.close()


if __name__ == "__main__":
    main()
