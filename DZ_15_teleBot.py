from warnings import filters

import telebot

import time
import pprint
import os
from skan import dom




TOKEN = 'token'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Здравствуйте !!! Я могу выводить некоторые данные из сайта «KLOKOV & BAZATEAM» ')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Я пока только учусь помогать !. Напишите /start')


@bot.message_handler(commands=['parser'])
def send_welcome(message):
    print(message.chat.id)
    text = message.text.split()
    print(text)
    chat_id = message.chat.id
    q = dom()
    for it in q:
        time.sleep(2)
        print(it)
        bot.send_message(chat_id, it)


@bot.message_handler(commands=['file1'])
def get_file_1(message):
    with open('Klokov_direction.txt', 'r', encoding='utf-8') as data:
        bot.send_document(message.chat.id, data)
    # или таким способом
    # bot.send_document(message.chat.id, document=open('Klokov_trenera.txt', 'r', encoding='utf-8'))


@bot.message_handler(commands=['file'])
def get_file_1(message):
    with open('Klokov_trenera.txt', 'r', encoding='utf-8') as data:
        bot.send_document(message.chat.id, data)



bot.polling()