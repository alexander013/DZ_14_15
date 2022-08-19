# Encoding: utf-8
import json
import pickle
import re


import requests
from bs4 import BeautifulSoup
import pprint
from csv import DictWriter

'''
работа с сайтом https://klokovbaza.ru/. 
Исследуемые направления:
1. Тренеры: спортивные достижения (разряды) +
2. Направления тренировок: название дисциплины, описание +
3. Расписание
4. Контакты
5. Дисциплина: название дисциплины, картинка

'''
def dom():
    list_href = []
    res = {}
            # Вывод достижений тренерского состава и ссылок на тренера
    url_trener = 'https://klokovbaza.ru/trainer'
    response_url_trener = requests.get(url_trener)

    soup_trener = BeautifulSoup(response_url_trener.text, 'html.parser')
    all_url_trener = soup_trener.find_all('a', class_='ttbase-trainer-item-image')
    for all_trener in all_url_trener:
            url_all = all_trener.get('href')
            name = all_trener.get('title')
            url_trener_opisanie = requests.get(url_all)
            soup_url_trener_opisanie = BeautifulSoup(url_trener_opisanie.text, 'html.parser')
            trener_opisanie = soup_url_trener_opisanie.find_all('p')
            res[name] = [url_all, trener_opisanie]
            # tag_list = []
            # for tag in trener_opisanie:
            #     title = tag
            #     tag = title.get_text()
            list_href.append(url_all)
            with open('Klokov_trenera.txt', 'w', encoding="utf-8") as f:
                for key, value in res.items():
                    f.write('%s:%s\n' % (key, value))





    # Получение данных по направлениям тренировок

    url_3 = 'https://klokovbaza.ru/trainings/'
    response_3 = requests.get(url_3)

    soup_3 = BeautifulSoup(response_3.text, 'html.parser')
    # print(soup_3)

    direction = soup_3.find_all('a', class_='ttbase-class-item-image')
    # print(direction)
    napr_dict = {}
    for direction_title in direction:

        # # print(direction_title)
        direction_name = direction_title.get('title')
        # print(direction_name)
        url_3 = direction_title.get('href')
        # # print(url_3)
        direction_items = requests.get(url_3)
        soup_direction = BeautifulSoup(direction_items.text, 'html.parser')
        items_direction = soup_direction.find_all('p')
        napr_dict[direction_name] = items_direction
        with open('Klokov_direction.txt', 'w', encoding="utf-8") as f:
            for key, value in napr_dict.items():
                f.write('%s:%s\n' % (key, value))
    return list_href
