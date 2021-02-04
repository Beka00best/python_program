#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import config
from telebot import types
from telebot import apihelper

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def welcome(message):
	sti = open('/home/bekzat/python/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	bot.send_message(message.chat.id, 'Добро пожаловать! \n Я - {1.first_name}!, тестовый бот от Беки. \n Напиши что-нибудь и следуй за инструкциями \n (Напиши например: пп или че хоч)'.format(message.from_user, bot.get_me()), 
		parse_mode = 'html')

@bot.message_handler(commands = ['put'])
def question(message):
	moon = types.InlineKeyboardMarkup(row_width = 2)
	man1 = types.InlineKeyboardButton('Bekzat', callback_data = 'B')
	man2 = types.InlineKeyboardButton('BBB', callback_data = 'B')
	man3 = types.InlineKeyboardButton('Бэксо', callback_data = 'B')
	man4 = types.InlineKeyboardButton('Бека', callback_data = 'B')

	moon.add(man1, man2, man3, man4)

	bot.send_message(message.chat.id, u'Кто по твоему мнению твой самый лучший одногруппник?', reply_markup = moon)

@bot.message_handler(commands = ['gor'])
def goroskop(message):
	mik = types.InlineKeyboardMarkup(row_width = 1)
	mik1 = types.InlineKeyboardButton('Стрелец', callback_data = 'A')
	mik2 = types.InlineKeyboardButton('Козерог', callback_data = 'A')
	mik3 = types.InlineKeyboardButton('Водолей', callback_data = 'A')
	mik4 = types.InlineKeyboardButton('Рыбы', callback_data = 'A')
	mik5 = types.InlineKeyboardButton('Овен', callback_data = 'A')
	mik6 = types.InlineKeyboardButton('Телец', callback_data = 'A')
	mik7 = types.InlineKeyboardButton('Близнецы', callback_data = 'A')
	mik8 = types.InlineKeyboardButton('Рак', callback_data = 'A')
	mik9 = types.InlineKeyboardButton('Лев', callback_data = 'A')
	mik10 = types.InlineKeyboardButton('Дева', callback_data = 'A')
	mik11 = types.InlineKeyboardButton('Весы', callback_data = 'A')
	mik12 = types.InlineKeyboardButton('Скорпион', callback_data = 'A')

	mik.add(mik1, mik2, mik3, mik4, mik5, mik6, mik7, mik8, mik9, mik10, mik11, mik12)

	bot.send_message(message.chat.id, u'Кто ты по гороскопу? Я сделаю прогноз', reply_markup = mik)

name = ' '
surname = ' '
age = 0


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == u'Привет' or message.text == u'привет':
		bot.send_message(message.from_user.id, 'Привет, зарегайся тип напиши /reg')
	elif message.text == '/reg':
		bot.send_message(message.chat.id, 'Как тебя зовут?')
		bot.register_next_step_handler(message, get_name)
	else:
		bot.send_message(message.from_user.id, 'Напиши Привет')

def get_name(message):
	global name
	name = message.text
	bot.send_message(message.from_user.id, 'Сколько тебе лет? (в цифрах)')
	bot.register_next_step_handler(message, get_age)

def get_age(message):
	global age
	age = int(message.text)
   	if age != 0:

		keyboard = types.InlineKeyboardMarkup() 
		key_yes = types.InlineKeyboardButton('Да', callback_data = 'yes')
		key_no = types.InlineKeyboardButton('Нет', callback_data = 'no')

		keyboard.add(key_yes, key_no)

		bot.send_message(message.chat.id, u'Тебе '+str(age)+ u' лет,и тебя зовут ' + name + u'?', reply_markup = keyboard)
	


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes': 
        bot.send_message(call.message.chat.id, 'ЙЕеее я менталист, я угадал : ) \n Идем дальше напиши /put')
    elif call.data == 'no':
    	bot.send_message(call.message.chat.id, 'Блин, я не угадал : ( \n Идем дальше напиши /put')
    elif call.data == 'B':
    	bot.send_message(call.message.chat.id, u'Спасибо за твой выбор ахахаха! \n Ты тоже самый лучший ' + name + u' Я еще сделал гороскоп напиши /gor')
    elif call.data == 'A':
    	bot.send_message(call.message.chat.id, u'Блок Полосина пройдет хорошо и ВМК останется живым, Тих Тих будет спать, а Бобылева и Новикова надеемся будут учить, а Крицков будет мягким, и ты сдашь сессию хорошо \n На этом мой бот все')

#RUN
bot.polling(none_stop=True, interval = 0)