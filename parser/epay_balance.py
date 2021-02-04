#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import config
import requests

#bot = telebot.TeleBot('1074652578:AAEwQ0ccKPKkYtk0yTuyQpXFb2XSuBZCH6c')

#@bot.message_handler(commands = ['start'])
#def welcome(message):
#	bot.send_message( message.chat.id, 'Добро пожаловать! \n Я - {1.first_name}!, ЛРТ баланс бот от Беки. \n Напиши /chain'.format(message.from_user, bot.get_me()),
#		parse_mode = 'html')

#@bot.message_handler(commands = ['chain'])
#def get_balance(message):
#	url = 'https://epay.transcard.kz/card-info/' + quote(message.text)
#	response = requests.get(url)
#	balance_data = response.json()
#	bot.send_message(call.message.chat.id, str(balance_data))

import requests

url = 'https://epay.transcard.kz/card-info/payment'
response = requests.get(url)

print(response.json())
