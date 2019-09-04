import telebot
from telebot import types
import time

bot = telebot.TeleBot("809372188:AAFwBQiGzX9jRn8gG_Pr-M3kaNFnPnCeBzs")

# [ [предмет], [часы],[минуты], [неделя] ]
# 1 - нижняя, 0 - верхняя, 2 - в обе
schedule = [

    # ПОНЕДЕЛЬНИК
    [
        ["ДОПОЛНИТЕЛЬНЫЕ ГЛАВЫ ВЫСШЕЙ МАТЕМАТИКИ (семинар), \nФедюков А.А. \n515 кабинет в 7:30", 7, 30, 2],
        ["МАТЕМАТИЧЕСКАЯ ЛОГИКА И ТЕОРИЯ АЛГОРИТМОВ (семинар), \nСорочан С.В. \n515 кабинет в 9:10", 9, 10, 2]
    ],

    # ВТОРНИК
    [
        ["АРХИТЕКТУРА ВЫЧИСЛИТЕЛЬНЫХ СИСТЕМ (семинар), \nМартынова Е.М. \n113/1 кабинет в 7:30", 7, 30, 1],
        ["ЛИНЕЙНОЕ ПРОГРАММИРОВАНИЕ (семинар), \nМокеев Д.Б. \n509 кабинет в 9:10", 9, 10, 0],
        ["ЛИНЕЙНОЕ ПРОГРАММИРОВАНИЕ (лекция), \nЗолотых Н.Ю. \n502 кабинет в 9:10", 9, 10, 1],
        ["ФИЗКУЛЬТУРА, \nМакс Корж в 10:50", 9, 10, 2],
        ["АЛГОРИТМЫ И СТРУКТУРЫ ДАННЫХ (семинар), \nШагбазян Д.В. \n509 кабинет в 13:00", 9, 10, 2],
        ["АЛГОРИТМЫ И СТРУКТУРЫ ДАННЫХ (практика), \nШагбазян Д.В. \n509 кабинет в 13:00", 9, 10, 2]
    ],

    # СРЕДА
    [
        ["АРХИТЕКТУРА ВЫЧИСЛИТЕЛЬНЫХ СИСТЕМ (лекция), \nМартынова Е.М. \n314 кабинет в 7:30", 7, 30, 2],
        ["АРХИТЕКТУРА ВЫЧИСЛИТЕЛЬНЫХ СИСТЕМ (семинар), \nМартынова Е.М. \n314 кабинет в 9:10", 7, 30, 0]
    ],

    # ЧЕТВЕРГ
    [
        ["ДОПОЛНИТЕЛЬНЫЕ ГЛАВЫ ВЫСШЕЙ МАТЕМАТИКИ (семинар), \nФедюков А.А. \n404 кабинет в 7:30", 7, 30, 2],
        ["МАТЕМАТИЧЕСКАЯ ЛОГИКА И ТЕОРИЯ АЛГОРИТМОВ (лекция), \nСорочан С.В. \n324(2) кабинет в 9:10", 9, 10, 2],
        ["ФИЗКУЛЬТУРА, \nМакс Корж в 10:50", 9, 10, 2]
    ],

    # ПЯТНИЦА
    [
        ["АЛГОРИТМЫ И СТРУКТУРЫ ДАННЫХ (семинар), \nШагбазян Д.В. \n403 кабинет в 10:50", 9, 10, 2],
        ["АЛГОРИТМЫ И СТРУКТУРЫ ДАННЫХ (практика), \nШагбазян Д.В. \n107 кабинет в 10:50", 9, 10, 2],
        ["АЛГОРИТМЫ И СТРУКТУРЫ ДАННЫХ (лекция), \n	Гергель В.П. \n114(2) кабинет в 14:40", 9, 10, 2],
        ["ДОПОЛНИТЕЛЬНЫЕ ГЛАВЫ ВЫСШЕЙ МАТЕМАТИКИ (семинар), \nМахрова  Е.Н.(сука ахуевшая) \n515 кабинет в 16:20", 7,
         30, 2],
    ],

    # СУББОТА
    [
        ["ИНТЕРНЕТ ВЕЩЕЙ (лекция), ноунейм препод \n324(2) кабинет в 10:50", 7, 30, 0],
        ["ИНТЕРНЕТ ВЕЩЕЙ (практика), ноунейм препод \n324(2)кабинет в 10:50", 7, 30, 0],
        ["ИНТЕРНЕТ ВЕЩЕЙ (практика), ноунейм препод \n324(2) кабинет в 14:40", 7, 30, 0],
    ],

]

text = time.strftime("Today is %B %d, %Y.", time.localtime())
text2 = time.strftime("%w", time.localtime())


def get_week():
    if (int(time.strftime("%d", time.localtime())) - (int(time.strftime("%w", time.localtime())) - 1)) % 2 == 0:
        return 1
    else:
        return 0


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup = telebot.types.ReplyKeyboardMarkup(True, True)
    itembtn1 = types.KeyboardButton('На сегодня')
    itembtn2 = types.KeyboardButton('На завтра')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Какое тебе расписание?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_schedule(message):
    if message.text == "На сегодня" and (int(time.strftime("%w", time.localtime())) - 1) != 0:

        for elem in schedule[int(time.strftime("%w", time.localtime())) - 1]:
            if elem[3] == get_week() or elem[3] == 2:
                bot.send_message(message.from_user.id, elem)
    elif message.text == "На завтра" and (int(time.strftime("%w", time.localtime())) - 1) != 0:
        for elem in schedule[int(time.strftime("%w", time.localtime()))]:
            bot.send_message(message.from_user.id, elem)
    elif (int(time.strftime("%w", time.localtime())) - 1) == 0:
        bot.send_message(message.from_user.id, "Брат, по воскресеньям мы не учимся")
    else:
        bot.send_message(message.from_user.id, "Напиши /start.")


bot.polling(none_stop=True)
