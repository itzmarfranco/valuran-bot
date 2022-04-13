import os
from dotenv import load_dotenv
import telebot

if __name__ == '__main__':

  load_dotenv()
  API_KEY = os.getenv('API_KEY')

  bot = telebot.TeleBot(API_KEY)

  @bot.message_handler(commands=['schedule'])
  def schedule(message):
    bot.reply_to(message, 'Work In Progress')

  @bot.message_handler(commands=['hora'])
  def hora(message):
    bot.reply_to(message, 'Bro, solo te pregunté la hora')

  @bot.message_handler(commands=['masters'])
  def masters(message):
    bot.reply_to(message, '''https://www.vlr.gg/event/926/valorant-champions-tour-stage-1-masters-reykjav-k/group-stage''')
