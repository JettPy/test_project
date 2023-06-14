import random
import telebot
import os
import dotenv

dotenv.load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

words = ['лиса', 'зима', 'лето']
used = set()
word = ''
answer = ''
hp = 0


@bot.message_handler(commands=['start'])
def start(message):
    global word, hp, answer
    word = random.choice(words)
    hp = 5
    answer = "-" * len(word)
    bot.send_message(message.chat.id, "Это виселица! Начинаем!")
    bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['text'])
def get_text(message):
    print(word)
    global hp, answer
    data = message.text
    if not(0 < len(data) < 2):
        bot.send_message(message.chat.id, "Введи русскую букву")
        return
    data = data.lower()
    if not (data in word and data not in used):
        hp -= 1
        if hp == 0:
            bot.send_message(message.chat.id, "Вы проиграли!")
        else:
            bot.send_message(message.chat.id, "Повторите еще раз!")
    used.add(data)
    tmp_answer = ''
    for letter in word:
        if letter == data:
            tmp_answer += data
        else:
            tmp_answer += answer
    answer = tmp_answer
    bot.send_message(message.chat.id, answer)


bot.infinity_polling()