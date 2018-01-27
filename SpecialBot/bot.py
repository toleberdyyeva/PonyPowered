# FIRST ECHO BOT  " REPLIER "
# import configs from
# from bs4 import BeautifulSoup
import telebot
import configs
# import json
# from Predict import predict, get_reviews_from_array
# from telebot import types
# import os

bot = telebot.TeleBot(configs.token)
# import requests

# ANY TEXT HANDLER
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text , parse_mode='HTML')



# Bot Initial run
if __name__ == '__main__':
    bot.polling(none_stop=True)