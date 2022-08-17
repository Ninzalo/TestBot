import random
import sys

import vk_api
import requests
import datetime
import time
import socket
import urllib3
import os
import json
# from bs4 import BeautifulSoup
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from config import token_vk

vk_session = vk_api.VkApi(token=token_vk)
longpoll = VkBotLongPoll(vk_session, 207111894)

if not os.path.exists(f'{os.getcwd()}\\data.json'):
    with open(f'{os.getcwd()}\\data.json', "w") as f:
        f.write(r"[]")


def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


def chat_sender(id, text, keyboard=None, empty=None):
    # vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})

    post = {
        "chat_id": id,
        "message": text,
        "random_id": 0
    }

    if keyboard is not None:
        if empty is not None:
            post["keyboard"] = keyboard.get_empty_keyboard()
        else:
            post["keyboard"] = keyboard.get_keyboard()

    else:
        post = post

    vk_session.method("messages.send", post)


while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:

                msg = event.object.message['text'].lower()

                # global student_group
                # global subgrp
                # global engl

                if msg == "/начать" or "|назад|" in msg or msg == "/р" or msg == "/start" or msg == "/p" or msg == "/kon":
                    id = event.chat_id
                    text = '=P'
                    # text = "Выберите свою группу: "
                    # keyboard = VkKeyboard()
                    # keyboard.add_button("|АКб 2-1|", color=VkKeyboardColor.PRIMARY)
                    # keyboard.add_button("|АКб 2-2|", color=VkKeyboardColor.PRIMARY)
                    # chat_sender(id, text, keyboard)
                    chat_sender(id, text)

                if msg == "/Время".lower() or msg == "/time".lower():
                    id = event.chat_id
                    text = datetime.datetime.today()
                    chat_sender(id, text)

                # if msg == "/koff".lower():
                #     id = event.chat_id
                #     text = "Клавиатура отключена, введите /kon для включения"
                #     keyboard = VkKeyboard()
                #     keyboard.add_button("")
                #     chat_sender(id, text, keyboard, empty=1)

                if msg == "/Me".lower():
                    id = event.chat_id
                    text = f"@id{event.raw['object']['message']['from_id']} Пошел нахуй"
                    chat_sender(id, text)

                if msg == "/all".lower():
                    id = event.chat_id
                    text = f"@all пошли нахуй"
                    chat_sender(id, text)

                if msg == "/Гоша".lower():
                    id = event.chat_id
                    text = f"[id225066569|Гоша,] пошел нахуй"
                    chat_sender(id, text)

                if msg == "/Артем".lower() or msg == "/Артём".lower():
                    id = event.chat_id
                    text = f"[id191829622|Артем,] пошел нахуй"
                    chat_sender(id, text)

                if msg == "/Егор".lower():
                    id = event.chat_id
                    text = f"[id181441617|Егор,] пошел нахуй"
                    chat_sender(id, text)

                if msg == "/Владос".lower():
                    id = event.chat_id
                    text = f"[id206172011|Влад,] пошел нахуй"
                    chat_sender(id, text)

                if msg == "/Артемий".lower():
                    id = event.chat_id
                    text = f"[id290711560|Артемий,] пошел нахуй"
                    chat_sender(id, text)

                if msg == "/Лена".lower():
                    id = event.chat_id
                    text = f"[id254542377|Лена,] пошла нахуй"
                    chat_sender(id, text)

                if msg == "/Вика".lower():
                    id = event.chat_id
                    text = f"[id299665482|Вика,] пошла нахуй"
                    chat_sender(id, text)

                if msg == "/Серега".lower():
                    id = event.chat_id
                    text = "[id198970096|Серега,] пошел нахуй"
                    chat_sender(id, text)

                # добавление команд из чата
                if "/" in msg:
                    with open(f"{os.getcwd()}\\data.json", "r") as f:
                        commands = json.load(f)
                        for command in commands:
                            if msg == command["Command"].lower():
                                id = event.chat_id
                                text = f'{command["Text"]}'
                                chat_sender(id, text)

                if '/add "/' in msg.lower() or '/add “/' in msg.lower() or '/add «/' in msg.lower():
                    with open(f"{os.getcwd()}\\data.json", "r") as f:
                        commands = json.load(f)
                    f.close()

                    counter = 0
                    for item in commands:
                        try:
                            if msg.split('"')[1].split("#")[0].strip() in item["Command"]:
                                counter += 1
                        except:
                            pass

                    for item in commands:
                        try:
                            if msg.split('“')[1].split("#")[0].split("”")[0].strip() in item["Command"]:
                                counter += 1
                        except:
                            pass

                    for item in commands:
                        try:
                            if msg.split('«')[1].split("#")[0].split("»")[0].strip() in item["Command"]:
                                counter += 1
                        except:
                            pass

                    if counter == 0:
                        can_add = 0
                        command = ""
                        if can_add == 0:
                            try:
                                command = {
                                    "Command": msg.split('"')[1].split("#")[0].strip(),
                                    "Text": msg.split('"')[1].split("#")[1].strip()
                                }
                                can_add = 1
                            except:
                                can_add = 0

                        if can_add == 0:
                            try:
                                command = {
                                    "Command": msg.split('“')[1].split("#")[0].split("”")[0].strip(),
                                    "Text": msg.split('“')[1].split("#")[1].split("”")[0].strip()
                                }
                                can_add = 1
                            except:
                                can_add = 0

                        if can_add == 0:
                            try:
                                command = {
                                    "Command": msg.split('«')[1].split("#")[0].split("»")[0].strip(),
                                    "Text": msg.split('«')[1].split("#")[1].split("»")[0].strip()
                                }
                                can_add = 1
                            except:
                                can_add = 0
                        if can_add == 1:
                            id = event.chat_id
                            try:
                                commands.append(command)
                                with open(f"{os.getcwd()}\\data.json", "w") as f:
                                    json.dump(commands, f, indent=4, ensure_ascii=False)
                                f.close()
                                text = f"Команда добавлена"
                                chat_sender(id, text)
                            except:
                                text = "Произошла ошибка"
                                chat_sender(id, text)
                    else:
                        id = event.chat_id
                        text = "Такая команда уже добавлена"
                        chat_sender(id, text)

                if msg == "/list":
                    id = event.chat_id
                    with open(f"{os.getcwd()}\\data.json", "r") as f:
                        commands = json.load(f)
                    f.close()
                    if not len(commands) == 0:
                        list_of_commands = []
                        text = ""
                        for command in commands:
                            list_of_commands.append(f'{command["Command"]} => {command["Text"]}')
                        for item in list_of_commands:
                            text = text + str(item) + f"\n"
                        chat_sender(id, text)
                    else:
                        text = "Команд нет"
                        chat_sender(id, text)

                if msg == "/addhelp":
                    id = event.chat_id
                    text = f'Для добавления команды введите: /add "/команда # текст, который бот будет выводить"\nВведите /list, чтобы увидеть созданные команды'
                    chat_sender(id, text)

                # расписание

                # if "|акб 2-1|" in msg or "|акб 2-2|" in msg:
                #     if "|акб 2-1|" in msg:
                #         student_group = 1
                #     if "|акб 2-2|" in msg:
                #         student_group = 2
                #     id = event.chat_id
                #     text = "Выберите свою подгруппу по лабам: "
                #     keyboard = VkKeyboard()
                #     keyboard.add_button("|Лабы 1|", color=VkKeyboardColor.PRIMARY)
                #     keyboard.add_button("|Лабы 2|", color=VkKeyboardColor.PRIMARY)
                #     keyboard.add_button("|Назад|", color=VkKeyboardColor.PRIMARY)
                #     chat_sender(id, text, keyboard)
                #     print(f"Выбрана группа АКб 2-{str(student_group)}")
                #
                # if "|лабы 1|" in msg or "|лабы 2|" in msg:
                #     if "|лабы 1|" in msg:
                #         subgrp = 3
                #     if "|лабы 2|" in msg:
                #         subgrp = 4
                #     id = event.chat_id
                #     text = "Выберите свою подгруппу по английскому: "
                #     keyboard = VkKeyboard()
                #     keyboard.add_button("|Англ 1|", color=VkKeyboardColor.PRIMARY)
                #     keyboard.add_button("|Англ 2|", color=VkKeyboardColor.PRIMARY)
                #     keyboard.add_button("|Назад|", color=VkKeyboardColor.PRIMARY)
                #     chat_sender(id, text, keyboard)
                #     print(f"Выбрана подгруппа по лабам - {str(subgrp-2)}")
                #
                # if "|англ 1|" in msg or "|англ 2|" in msg:
                #     if "|англ 1|" in msg:
                #         engl = 1
                #     if "|англ 2|" in msg:
                #         engl = 2
                #     id = event.chat_id
                #     text = "На какой день смотрим расписание? "
                #     keyboard = VkKeyboard()
                #     keyboard.add_button("|Сегодня|", color=VkKeyboardColor.PRIMARY)
                #     keyboard.add_button("|Завтра|", color=VkKeyboardColor.PRIMARY)
                #     keyboard.add_button("|Послеавтра|", color=VkKeyboardColor.PRIMARY)
                #     keyboard.add_line()
                #     keyboard.add_button("|Назад|", color=VkKeyboardColor.PRIMARY)
                #     # keyboard.add_line()
                #     # keyboard.add_button("|убрать кнопки|", color=VkKeyboardColor.NEGATIVE)
                #     chat_sender(id, text, keyboard)
                #     print(f"Выбрана подгруппа по английскому - {str(engl)}")
                #
                # if "|сегодня|" in msg or "|завтра|" in msg or "|послеавтра|" in msg:
                #
                #     headers = {
                #         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.2.381 Yowser/2.5 Safari/537.36"
                #     }
                #
                #     try:
                #         url = f"https://sd.mstuca1.ru/d/full?fac=2&flow=171&grp={student_group}&lsubgrp={str(subgrp)}&esubgrp={engl}"
                #     except:
                #         student_group = 1
                #         subgrp = 1
                #         engl = 1
                #         id = event.chat_id
                #         text = f"Данные о группе, подгруппе по английскому и лабам не указаны\nНажмите \"Назад\" и укажите ваши данные\nПоказываем расписание для АКб 2-1 | Лабы 1 | Англ 1"
                #         keyboard = VkKeyboard()
                #         keyboard.add_button("|Сегодня|", color=VkKeyboardColor.PRIMARY)
                #         keyboard.add_button("|Завтра|", color=VkKeyboardColor.PRIMARY)
                #         keyboard.add_button("|Послеавтра|", color=VkKeyboardColor.PRIMARY)
                #         keyboard.add_line()
                #         keyboard.add_button("|Назад|", color=VkKeyboardColor.PRIMARY)
                #         # keyboard.add_line()
                #         # keyboard.add_button("|убрать кнопки|", color=VkKeyboardColor.NEGATIVE)
                #         chat_sender(id, text, keyboard)
                #         url = f"https://sd.mstuca1.ru/d/full?fac=2&flow=63&grp={student_group}&lsubgrp={str(subgrp)}&esubgrp={engl}"
                #
                #     r = requests.get(url=url, headers=headers)
                #
                #     soup = BeautifulSoup(r.text, "lxml")
                #     articles_cards = soup.find_all("tr", style="height: 60px;")
                #
                #     count_days = 0
                #     if "|сегодня|" in msg:
                #         count_days = 0
                #     if "|завтра|" in msg:
                #         count_days = 1
                #     if "|послеавтра|" in msg:
                #         count_days = 2
                #
                #     today = datetime.datetime.today()
                #     date = today + datetime.timedelta(days=count_days, hours=0)
                #
                #     month = date.strftime('%m')
                #     if month == "01":
                #         month = "Янв"
                #     elif month == "02":
                #         month = "Фев"
                #     elif month == "03":
                #         month = "Мар"
                #     elif month == "04":
                #         month = "Апр"
                #     elif month == "05":
                #         month = "Май"
                #     elif month == "09":
                #         month = "Сен"
                #     elif month == "10":
                #         month = "Окт"
                #     elif month == "11":
                #         month = "Ноя"
                #     elif month == "12":
                #         month = "Дек"
                #
                #     day = str(f"{date.strftime('%d')} {month} 20{date.strftime('%y')}")
                #     text = ""
                #     article_day = ""
                #     day_of_week = ""
                #
                #     for article in articles_cards:
                #         try:
                #             article_titles = article.find_all("td")
                #             article_day = article.find("span", style="color: #000000;").text.strip()
                #             if article_day == day:
                #                 print(f"Показано расписание на {article_day}")
                #                 text = f"{str(article_day)}\n \n"
                #                 for title in article_titles:
                #                     try:
                #                         lesson = title.find("b").text.strip()
                #                         name = title.find("small").text.strip()
                #                         place = title.find("u").text.strip()
                #                         href = "https://sd.mstuca1.ru/d/" + title.find("a").get("href")
                #                         lect_or_pr = title.get("class")
                #
                #                         time_lp = "0"
                #                         try:
                #                             req = requests.get(url=href, headers=headers)
                #
                #                             soup2 = BeautifulSoup(req.text, "lxml")
                #                             day_of_week = soup2.find_all("td")[-3].text.strip()
                #
                #                             number = soup2.find("tr").text.strip()[12]
                #
                #                             if number == "1":
                #                                 time_lp = "8:30 - 10:00"
                #                             if number == "2":
                #                                 time_lp = "10:10 - 11:40"
                #                             if number == "3":
                #                                 time_lp = "12:40 - 14:10"
                #                             if number == "4":
                #                                 time_lp = "14:20 - 15:50"
                #                             if number == "5":
                #                                 time_lp = "16:20 - 17:50"
                #                             if number == "6":
                #                                 time_lp = "18:00 - 19:30"
                #                         except:
                #                             pass
                #
                #                         if "day_prctic" in lect_or_pr:
                #                             lect_or_pr = "ПРАКТИКА"
                #                         elif "day_lection" in lect_or_pr:
                #                             lect_or_pr = "ЛЕКЦИЯ"
                #                         else:
                #                             lect_or_pr = "ЛАБА"
                #                         text = text + f"{time_lp}\n{lect_or_pr}\n{lesson}\n{place}\n\n"
                #
                #                     except:
                #                         pass
                #         except:
                #             pass
                #     try:
                #         text = f"{day_of_week}\nАКб 2-{str(student_group)} | Лабы {str(subgrp - 2)} | Англ {str(engl)}\n{text}"
                #         del day_of_week
                #         del time_lp
                #         del lect_or_pr
                #         del lesson
                #         del place
                #     except:
                #         text = f"{text}АКб 2-{str(student_group)} | Лабы {str(subgrp - 2)} | Англ {str(engl)}\nРасписания нет"
                #
                #     id = event.chat_id
                #     keyboard = VkKeyboard()
                #     keyboard.add_button("|Сегодня|", color=VkKeyboardColor.PRIMARY)
                #     keyboard.add_button("|Завтра|", color=VkKeyboardColor.PRIMARY)
                #     keyboard.add_button("|Послеавтра|", color=VkKeyboardColor.PRIMARY)
                #     keyboard.add_line()
                #     keyboard.add_button("|Назад|", color=VkKeyboardColor.PRIMARY)
                #     # keyboard.add_line()
                #     # keyboard.add_button("|убрать кнопки|", color=VkKeyboardColor.NEGATIVE)
                #     chat_sender(id, text, keyboard)
    except (requests.exceptions.ReadTimeout, socket.timeout, urllib3.exceptions.ReadTimeoutError, socket.gaierror, urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError, requests.exceptions.ConnectionError, vk_api.exceptions.ApiError):
        time.sleep(1)
        print('_______Timeout______')

