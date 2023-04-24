#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if month == 2:
    days = 28
elif month in [4, 6, 9, 11]:
    days = 30
elif month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
else:
    print("Некорректный номер месяца")
    days = None

if days is not None:
    print(f"В месяце номер '{month}' {days} дней")
