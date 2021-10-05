# Этот бот - консультант магазина Мвидео. Он поможет выбрать телефон
# 😀👌😘😂👋😍😊😁🆘😢

import config
import telebot
from telebot import types
import time

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands = ['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	markup.row('до 5.000 руб', '5.000- 10.000 руб')
	markup.row('10.000- 15.000 руб', '15.000-20.000 руб')
	markup.row('20.000-30.000 руб', '30.000-40.000 руб')
	markup.row('Больше 40.000 руб')
	bot.send_message(message.chat.id, 'Привет 👋👋👋, я консультант Мвидео ')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Я помогу тебе выбрать смартфон')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Выбери ценовую  категорию', reply_markup = markup)


	# photo = open('C:/Users/никита/Desktop/ТГ БОТ/TelegramBot/advicer_bot/Apple iPhone 12 128GB ( 74 990 ).jpg', 'rb')
	# bot.send_photo(message.chat.id, photo)



@bot.message_handler(commands = ['inline'])
def inline(message):
	markup = types.InlineKeyboardMarkup(row_width = 1)
	item = types.InlineKeyboardButton('Apple iPhone 12 128GB за 74.990 руб.', callback_data = 'ph_1')
	item_2 = types.InlineKeyboardButton('Samsung Galaxy S21 128GB за 68.990 руб.', callback_data = 'ph_2')
	item_3 = types.InlineKeyboardButton('Xiaomi Mi 11 256 GB за 85.990 руб( и такие бывают)', callback_data = 'ph_3')
	markup.add(item, item_2, item_3)

	bot.send_message(message.chat.id, 'Выбирай!!!', reply_markup = markup)


@bot.message_handler(content_types = ['text'])
def text(message):
	if message.text == 'до 5.000 руб':
		bot.send_message(message.chat.id, '😢Извиняемся, но телефонов такой ценовой категории нет в наличии')

	elif message.text == '5.000- 10.000 руб':
		bot.send_message(message.chat.id, 'Советую Xiaomi Redmi 9A за 7990 руб.')

	elif message.text == '10.000- 15.000 руб':
		bot.send_message(message.chat.id, 'Советую Vivo Y20 за 11.990 руб.')

	elif message.text == '15.000-20.000 руб':
		bot.send_message(message.chat.id, 'Бери Samsung Galaxy A32 за 18.990 руб.')
	
	elif message.text == '20.000-30.000 руб':
		bot.send_message(message.chat.id, 'Бери Xiaomi Redmi Note 10 Pro за 28.990 руб.')
	
	elif message.text == '30.000-40.000 руб':
		bot.send_message(message.chat.id, 'Ты здесь успеваешь отхватить Apple iPhone SE 64 GB за 39.990 руб.')
	
	elif message.text == 'Больше 40.000 руб':
		bot.send_message(message.chat.id, 'Ни фа ты богатый, выбирай тогда из 3-ех вариантов, нажав /inline ')


@bot.callback_query_handler(func = lambda call:True)
def data(call):
	if call.message:
		if call.data == 'ph_1':
			photo = open('C:/Users/никита/Desktop/ТГ БОТ/TelegramBot/advicer_bot/Apple iPhone 12 128GB ( 74 990 ).jpg', 'rb')
			bot.send_photo(call.message.chat.id, photo)
			bot.send_message(call.message.chat.id, 'Хороший выбор👌👌👌' )

		elif call.data == 'ph_2':
			photo = open('C:/Users/никита/Desktop/ТГ БОТ/TelegramBot/advicer_bot/Samsung Galaxy S21 128GB ( 68 990 ).jpg', 'rb')
			bot.send_photo(call.message.chat.id, photo)
			bot.send_message(call.message.chat.id, 'Хороший выбор👌👌👌' )

		elif call.data == 'ph_3':
			photo = open('C:/Users/никита/Desktop/ТГ БОТ/TelegramBot/advicer_bot/Xiaomi Mi 11 256GB ( 85 990 ).jpg', 'rb')
			bot.send_photo(call.message.chat.id, photo)
			bot.send_message(call.message.chat.id, 'Хороший выбор👌👌👌' )




bot.polling()

