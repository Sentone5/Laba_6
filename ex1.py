#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: создайте словарь, связав его с переменной school , и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.
from datetime import date
import sys

if __name__ == '__main__':
    school = {'1a': 20, '1б': 20, '9a': 22, '9б': 25, '10a': 13,
              '10б': 14, '11a': 17, '11б': 15}
    print(school)

    school['9a'] += 1
    school['11в'] = 10
    school.pop('11a', 17)

    s = 0
    for item in school.values():
        s += item
    print(school)
    print("Количество учеников во всех классах", s)
