import telebot
import sqlite3
import sys
import config
import functions
from telebot import types
from telebot import apihelper
sys.path.insert(0, 'C:/Users/Кирилл/PycharmProjects/Tokens/')
import mytokens
bot = telebot.TeleBot(mytokens.music_bot_token)

@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    song_list = types.KeyboardButton(config.item1)
    markup.add(song_list)
    bot.send_message(message.chat.id, config.meeting_message, reply_markup=markup)
@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, config.help_message)

@bot.message_handler(commands=['songs'])
def print_song(message):
    sqlite_connection = sqlite3.connect('songs.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from song_list"""
    cursor.execute(sqlite_select_query)
    records = str(cursor.fetchall())
    records = functions.fix_list(records)
    print(records)
    bot.send_message(message.chat.id, records)

@bot.message_handler(commands=['add'])
def add_song(message):
    new_song = str(functions.get_song(message.text))
    sqlite_connection = sqlite3.connect('songs.db')
    cursor = sqlite_connection.cursor()
    cursor.execute("INSERT INTO song_list(name) VALUES(?);", (new_song,))
    print('Кто-то добавил: ' + new_song)
    sqlite_connection.commit()

@bot.message_handler(commands=['del'])
def delete_song(message):
    song = str(functions.get_song(message.text))
    sqlite_connection = sqlite3.connect('songs.db')
    cursor = sqlite_connection.cursor()
    cursor.execute("DELETE from song_list where name = ?", (song,))
    sqlite_connection.commit()
    print('Кто-то удалил: ' + song)
@bot.message_handler(content_types=['text'])
def message_reply(message):
    if config.print_keys.count(message.text) > 0:
        print_song(message)
    elif config.helper_keys.count(message.text) > 0:
        helper(message)
    #elif (message.text.find('бот')) or (message.text.find('Бот')) or (config.unemployed_keys.count(message.text)>0):
      #  joke = functions.get_random_joke(message)
      #  bot.send_message(message.chat.id, joke)
bot.infinity_polling()


