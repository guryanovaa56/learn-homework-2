"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    date_format = '%d.%m.%Y'
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    days_ago_30 = today - timedelta(days=30)
    result = f'Сегодняшняя дата - {today.strftime(date_format)} \nВчерашняя дата - {yesterday.strftime(date_format)} \n30 дней назад дата - {days_ago_30.strftime(date_format)}'

    return result


def str_2_datetime(date_string):

    str_to_datetime = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return str_to_datetime

if __name__ == "__main__":
    print(print_days())
    print(str_2_datetime("15/09/22 11:40:03.234567"))
